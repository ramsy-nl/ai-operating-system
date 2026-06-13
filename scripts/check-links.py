#!/usr/bin/env python3
"""Verify that relative markdown links resolve to real files.

Scans every *.md / *.mdc file (excluding .git) for inline links of the form
`](target)`, skips external/anchor/mailto links, strips any anchor or title,
and checks the target exists relative to the file. Exits non-zero on any break.
"""
import pathlib
import re
import sys

LINK = re.compile(r"\]\(([^)]+)\)")
SKIP_PREFIXES = ("http://", "https://", "mailto:", "#")


def main() -> int:
    root = pathlib.Path(".")
    files = [
        f
        for ext in ("*.md", "*.mdc")
        for f in root.rglob(ext)
        if ".git/" not in str(f)
    ]
    errors: list[str] = []

    for f in sorted(files):
        for match in LINK.finditer(f.read_text(encoding="utf-8")):
            raw = match.group(1).strip()
            if raw.startswith(SKIP_PREFIXES):
                continue
            # Drop an optional "title" and any #anchor.
            target = raw.split()[0].split("#", 1)[0]
            if not target:
                continue
            if not (f.parent / target).resolve().exists():
                errors.append(f"{f}: broken link -> {raw}")

    if errors:
        print("Link check FAILED:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"Links OK ({len(files)} files scanned).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
