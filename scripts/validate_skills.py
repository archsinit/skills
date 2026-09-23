#!/usr/bin/env python3
"""Lightweight local validation for Agent Skill frontmatter.

This is not a replacement for the official `skills-ref validate` command.
It catches the naming/frontmatter errors most likely to occur while editing this repo.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    try:
        _, raw, _ = text.split("---", 2)
    except ValueError as exc:
        raise ValueError("unterminated YAML frontmatter") from exc

    values: dict[str, str] = {}
    for line in raw.strip().splitlines():
        if not line.strip() or line.startswith(" "):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def validate_skill(path: Path) -> list[str]:
    errors: list[str] = []
    skill_md = path / "SKILL.md"
    if not skill_md.exists():
        return [f"{path}: missing SKILL.md"]

    try:
        fm = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
    except ValueError as exc:
        return [f"{skill_md}: {exc}"]

    name = fm.get("name", "")
    description = fm.get("description", "")

    if not name:
        errors.append(f"{skill_md}: missing name")
    elif name != path.name:
        errors.append(f"{skill_md}: name '{name}' does not match directory '{path.name}'")
    elif len(name) > 64 or not NAME_RE.fullmatch(name):
        errors.append(f"{skill_md}: invalid Agent Skills name '{name}'")

    if not description:
        errors.append(f"{skill_md}: missing description")
    elif len(description) > 1024:
        errors.append(f"{skill_md}: description exceeds 1024 characters")

    return errors


def main() -> int:
    errors: list[str] = []
    for path in sorted(p for p in SKILLS.iterdir() if p.is_dir()):
        errors.extend(validate_skill(path))

    if errors:
        print("Validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Local validation passed.")
    print("For spec-level validation, also run: skills-ref validate <skill-directory>")
    return 0


if __name__ == "__main__":
    sys.exit(main())
