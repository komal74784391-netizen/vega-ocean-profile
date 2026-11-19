#!/usr/bin/env python3
"""Minimal renderer for the Quillmark site starter."""
from pathlib import Path

SITE = Path("site")
OUT = Path("_site")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "index.html").write_text("<!-- rendered -->\n", encoding="utf-8")
    print("Rendered", OUT)


if __name__ == "__main__":
    main()
