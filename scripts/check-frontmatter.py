#!/usr/bin/env python3
"""Validate the when-to-use frontmatter on prompts/ and guardrails/ files.

Each file must open with a YAML frontmatter block that:
  - parses as a YAML mapping,
  - has non-empty `name` (matching the filename stem) and `description`,
  - has the directory's selector field (`phase` for prompts, `enforcement`
    for guardrails).
Exits non-zero on any violation.
"""
import pathlib
import sys

import yaml

REQUIRED = ("name", "description")
SELECTOR = {"prompts": "phase", "guardrails": "enforcement"}


def main() -> int:
    errors: list[str] = []
    targets = sorted(
        p for d in SELECTOR for p in pathlib.Path(d).glob("*.md")
    )

    for path in targets:
        text = path.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            errors.append(f"{path}: missing frontmatter (must start with '---')")
            continue
        end = text.find("\n---", 4)
        if end == -1:
            errors.append(f"{path}: frontmatter not closed with '---'")
            continue
        try:
            data = yaml.safe_load(text[4:end])
        except yaml.YAMLError as exc:
            errors.append(f"{path}: invalid YAML frontmatter: {exc}")
            continue
        if not isinstance(data, dict):
            errors.append(f"{path}: frontmatter is not a mapping")
            continue

        for key in REQUIRED:
            if not str(data.get(key, "")).strip():
                errors.append(f"{path}: missing or empty '{key}'")
        selector = SELECTOR[path.parts[0]]
        if selector not in data:
            errors.append(f"{path}: missing '{selector}' field")
        if data.get("name") and data["name"] != path.stem:
            errors.append(
                f"{path}: name '{data['name']}' != filename stem '{path.stem}'"
            )

    if errors:
        print("Frontmatter check FAILED:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"Frontmatter OK ({len(targets)} files).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
