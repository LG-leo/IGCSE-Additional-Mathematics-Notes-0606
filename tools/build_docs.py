#!/usr/bin/env python3
"""Stage the root chapter Markdown files into ``docs/`` for the MkDocs build.

The repository keeps its notes at the repository root (``IG0606 CompletelyNotes2_*.md``)
so that GitHub renders them directly.  MkDocs needs a single ``docs_dir``; this script
copies each chapter into ``docs/cn/chNN.md`` / ``docs/en/chNN.md``, removes the repeated
boilerplate header (title + duplicated table of contents) and adds unique front matter
(``title`` + ``description``) so that every page has a distinct <title> and meta
description for search engines.

Run from the repository root:

    python tools/build_docs.py
"""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

# "# 第 1 章：…” / "## 第10章 综合应用" / "# Chapter 1: …"
CHAPTER_RE = re.compile(
    r"^(?P<hashes>#{1,3})\s+(?:第\s*(?P<cn_num>\d+)\s*章|Chapter\s*(?P<en_num>\d+))"
    r"\s*[:：]?\s*(?P<title>.*?)\s*$"
)
HEADING_RE = re.compile(r"^(?P<hashes>#{1,6})\s+(?P<text>.*)$")

CN_SOURCES = "IG0606 CompletelyNotes2_ch*.md"
EN_SOURCES = "IG0606 CompletelyNotes2_en*.md"

MAX_DESCRIPTION = 160

_MD_NOISE = re.compile(r"[*_`>#\[\]]")
_INLINE_MATH = re.compile(r"\$\$?.+?\$\$?", re.DOTALL)


def _clean_inline(text: str) -> str:
    """Turn a Markdown paragraph into a plain-text meta description."""
    text = _INLINE_MATH.sub("", text)
    text = _MD_NOISE.sub("", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def _first_paragraph(lines: list[str], start: int) -> str:
    """Return the first ordinary paragraph that follows the chapter heading."""
    for line in lines[start:]:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith(("#", "|", "-", ">", "---", "```", "$$")):
            continue
        cleaned = _clean_inline(stripped)
        if cleaned:
            return cleaned[:MAX_DESCRIPTION]
    return ""


def _shift_headings(lines: list[str], shift: int) -> list[str]:
    """Shift every heading level by ``shift`` (e.g. -1 promotes H2 -> H1)."""
    if shift == 0:
        return lines
    shifted: list[str] = []
    for line in lines:
        match = HEADING_RE.match(line)
        if match:
            level = max(1, min(len(match.group("hashes")) + shift, 6))
            shifted.append("#" * level + " " + match.group("text"))
        else:
            shifted.append(line)
    return shifted


def parse_chapter(path: Path) -> tuple[int, str, str, str]:
    """Return ``(chapter_number, title, description, body)`` for one source file."""
    lines = path.read_text(encoding="utf-8").splitlines()
    for index, line in enumerate(lines):
        match = CHAPTER_RE.match(line)
        if not match:
            continue
        number = int(match.group("cn_num") or match.group("en_num"))
        title = match.group("title").strip()
        description = _first_paragraph(lines, index + 1)
        # Drop the repeated site header (title + duplicated table of contents)
        body_lines = _shift_headings(lines[index:], 1 - len(match.group("hashes")))
        body = "\n".join(body_lines).strip() + "\n"
        return number, title, description, body
    raise SystemExit(f"ERROR: no chapter heading found in {path.name}")


def write_page(target: Path, title: str, description: str, body: str) -> None:
    escaped_title = title.replace('"', '\\"')
    escaped_description = description.replace('"', '\\"')
    front_matter = (
        "---\n"
        f'title: "{escaped_title}"\n'
        f'description: "{escaped_description}"\n'
        "---\n\n"
    )
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(front_matter + body, encoding="utf-8")


def stage(language: str, pattern: str, label_cn: str, label_en: str) -> list[tuple[int, str]]:
    pages: list[tuple[int, str]] = []
    for source in sorted(ROOT.glob(pattern)):
        number, title, description, body = parse_chapter(source)
        if not description:
            description = (
                f"IGCSE Additional Mathematics (0606) notes — {title}"
                if language == "en"
                else f"IGCSE 附加数学（0606）笔记 — {title}"
            )
        if language == "cn":
            display_title = f"第 {number} 章：{title}"
            description = f"{description}"
        else:
            display_title = f"Chapter {number}: {title}"
        target = DOCS / language / f"ch{number:02d}.md"
        write_page(target, display_title, description, body)
        pages.append((number, display_title))
        print(f"  staged {source.name} -> {target.relative_to(ROOT)}")
    return pages


def main() -> int:
    for generated in (DOCS / "cn", DOCS / "en"):
        if generated.exists():
            shutil.rmtree(generated)

    print("Staging Chinese chapters:")
    cn_pages = stage("cn", CN_SOURCES, "第 {n} 章", "Chapter {n}")
    print("Staging English chapters:")
    en_pages = stage("en", EN_SOURCES, "第 {n} 章", "Chapter {n}")

    expected = list(range(1, 11))
    for language, pages in (("cn", cn_pages), ("en", en_pages)):
        numbers = sorted(number for number, _ in pages)
        if numbers != expected:
            print(
                f"WARNING: {language} chapters are {numbers}, expected 1..10",
                file=sys.stderr,
            )

    print(f"Done: {len(cn_pages)} Chinese + {len(en_pages)} English pages in docs/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
