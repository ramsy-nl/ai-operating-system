#!/usr/bin/env bash
# Validate that commit subjects in a range follow Conventional Commits.
# Usage: check-commits.sh <git-range>   e.g. check-commits.sh base..head
# Merge commits are skipped. Exits non-zero on any non-conforming subject.
set -euo pipefail

range="${1:-}"
if [ -z "$range" ]; then
  echo "usage: check-commits.sh <git-range>" >&2
  exit 2
fi

pattern='^(feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert)(\([a-z0-9._/-]+\))?!?: .+'
fail=0

for sha in $(git rev-list "$range"); do
  # Skip merge commits (more than one parent).
  if [ "$(git rev-list --parents -n 1 "$sha" | wc -w)" -gt 2 ]; then
    continue
  fi
  subject="$(git log -1 --format=%s "$sha")"
  if ! printf '%s' "$subject" | grep -qE "$pattern"; then
    echo "  - ${sha:0:8}: non-conventional subject: $subject"
    fail=1
  fi
done

if [ "$fail" -ne 0 ]; then
  echo "Commit message check FAILED (expected: type(scope): summary)."
  exit 1
fi
echo "Commit messages OK."
