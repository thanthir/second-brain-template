#!/usr/bin/env python3
"""fetch-url.py — fetch a web page and write cleaned plain text to .tmp/.

Stdlib-only: no `pip install`, no secrets. This is the deterministic execution
layer of the [[digest-url]] workflow — Claude orchestrates, this script does the
fetching/cleaning. Intermediate output goes to .tmp/ (disposable); the actual
deliverable (an atomic note) is authored by Claude in Knowledge/.

Usage (run from the project root):
    python3 tools/fetch-url.py "https://example.com/some-article"

Writes: .tmp/<slug>.txt  and prints the slug + path.
"""

import re
import sys
import pathlib
from html.parser import HTMLParser
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

TMP_DIR = pathlib.Path(__file__).resolve().parent.parent / ".tmp"
SKIP_TAGS = {"script", "style", "noscript", "head", "svg"}


class TextExtractor(HTMLParser):
    """Collect visible text, dropping script/style/etc. and the <title>."""

    def __init__(self):
        super().__init__()
        self._skip_depth = 0
        self._in_title = False
        self.title = ""
        self.chunks = []

    def handle_starttag(self, tag, attrs):
        if tag in SKIP_TAGS:
            self._skip_depth += 1
        if tag == "title":
            self._in_title = True

    def handle_endtag(self, tag):
        if tag in SKIP_TAGS and self._skip_depth:
            self._skip_depth -= 1
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._skip_depth:
            return
        if self._in_title:
            self.title += data
            return
        text = data.strip()
        if text:
            self.chunks.append(text)


def slugify(text, fallback="page"):
    text = re.sub(r"[^\w\s-]", "", (text or "").lower()).strip()
    text = re.sub(r"[\s_-]+", "-", text)
    return text[:60].strip("-") or fallback


def fetch(url):
    req = Request(url, headers={"User-Agent": "second-brain-research-digest/1.0"})
    with urlopen(req, timeout=30) as resp:  # noqa: S310 (trusted, user-supplied URL)
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.read().decode(charset, errors="replace")


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: python3 tools/fetch-url.py <url>")
    url = sys.argv[1]

    try:
        html = fetch(url)
    except (HTTPError, URLError) as e:
        sys.exit(f"fetch failed for {url}: {e}")

    parser = TextExtractor()
    parser.feed(html)

    title = parser.title.strip()
    body = "\n".join(parser.chunks)
    # collapse runs of blank lines
    body = re.sub(r"\n{3,}", "\n\n", body)

    slug = slugify(title or url.rstrip("/").split("/")[-1])
    TMP_DIR.mkdir(exist_ok=True)
    out_path = TMP_DIR / f"{slug}.txt"
    out_path.write_text(
        f"SOURCE: {url}\nTITLE: {title}\n\n{body}\n", encoding="utf-8"
    )

    print(f"slug: {slug}")
    print(f"wrote: {out_path}")
    print(f"chars: {len(body)}")

    # --- Optional LLM-summary step (off by default) ---------------------------
    # To auto-summarize, load SUMMARY_API_KEY from the project .env (by name,
    # never inline the value) and POST `body` to your LLM of choice here, then
    # write the summary alongside the raw text. Kept out of the default path so
    # the sample runs with zero install and zero secrets.
    #   import os; key = os.environ.get("SUMMARY_API_KEY")  # loaded from .env


if __name__ == "__main__":
    main()
