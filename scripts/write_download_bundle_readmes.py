#!/usr/bin/env python3
"""Write README_EXTRACT.txt and readme.md for split-zip download folders (GitHub Actions).

readme.md lists raw.githubusercontent.com links for every file in the bundle directory.
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from urllib.parse import quote


def _encode_path_for_raw_url(relpath_posix: str) -> str:
    return "/".join(quote(segment, safe="") for segment in relpath_posix.split("/"))


def _resolve_ref(explicit: str | None) -> str:
    if explicit:
        return explicit
    ref = os.environ.get("GITHUB_REF_NAME", "").strip()
    if ref:
        return ref
    full = os.environ.get("GITHUB_REF", "").strip()
    if full.startswith("refs/heads/"):
        return full[len("refs/heads/") :]
    if full.startswith("refs/tags/"):
        return full[len("refs/tags/") :]
    return "main"


def _write_readme_extract(dest: Path, archive_base: str) -> None:
    text = f"""This directory contains a split ZIP archive.
Files are generated in standard multi-part ZIP format:
- {archive_base}.z01
- {archive_base}.z02
- ...
- {archive_base}.zip

How to extract:
1) Keep all parts in the same directory.
2) Open/extract ONLY {archive_base}.zip with 7-Zip/WinRAR/unzip.
"""
    dest.joinpath("README_EXTRACT.txt").write_text(text, encoding="utf-8", newline="\n")


def _write_markdown_raw_list(
    *,
    workspace: Path,
    dest: Path,
    repo_full: str,
    ref: str,
) -> None:
    try:
        rel_dest = dest.relative_to(workspace).as_posix()
    except ValueError as e:
        raise SystemExit(f"dest-dir must be inside workspace ({workspace}): {dest}") from e

    if "/" not in repo_full or repo_full.count("/") != 1:
        raise SystemExit(
            "Invalid repo slug; expected OWNER/NAME. "
            "Set GITHUB_REPOSITORY or pass --github-repository.",
        )

    entries: list[tuple[str, str]] = []
    for path in sorted(dest.iterdir(), key=lambda p: p.name.lower()):
        if path.is_file():
            rel_file = path.relative_to(workspace).as_posix()
            encoded = _encode_path_for_raw_url(rel_file)
            url = f"https://raw.githubusercontent.com/{repo_full}/{ref}/{encoded}"
            entries.append((path.name, url))

    readme_path = dest / "readme.md"
    readme_rel = readme_path.relative_to(workspace).as_posix()
    readme_encoded = _encode_path_for_raw_url(readme_rel)
    readme_url = f"https://raw.githubusercontent.com/{repo_full}/{ref}/{readme_encoded}"
    entries.append((readme_path.name, readme_url))
    entries.sort(key=lambda pair: pair[0].lower())

    lines = [
        "# Download bundle - direct file links",
        "",
        "Raw URLs (GitHub `raw.githubusercontent.com`) for files in this folder:",
        "",
    ]
    for name, url in entries:
        lines.append(f"- [{name}]({url})")
    lines.append("")

    readme_path.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Write README_EXTRACT.txt and readme.md with raw GitHub links.",
    )
    parser.add_argument(
        "--dest-dir",
        required=True,
        help="Bundle directory relative to repo root (e.g. download/my_video).",
    )
    parser.add_argument(
        "--archive-base",
        required=True,
        help="Archive stem used for split zip parts (e.g. my_video).",
    )
    parser.add_argument(
        "--workspace",
        default=os.environ.get("GITHUB_WORKSPACE", os.getcwd()),
        help="Repository root (default: GITHUB_WORKSPACE or cwd).",
    )
    parser.add_argument(
        "--github-repository",
        default=os.environ.get("GITHUB_REPOSITORY", ""),
        metavar="OWNER/REPO",
        help="Override GITHUB_REPOSITORY for raw URLs.",
    )
    parser.add_argument(
        "--github-ref",
        default=None,
        help="Branch or tag name for raw URLs (default: GITHUB_REF_NAME / GITHUB_REF).",
    )
    args = parser.parse_args()

    workspace = Path(args.workspace).resolve()
    dest = (workspace / args.dest_dir).resolve()
    if not dest.is_dir():
        print(f"Not a directory: {dest}", file=sys.stderr)
        return 1

    repo_full = (args.github_repository or "").strip()
    if not repo_full:
        print(
            "Missing GITHUB_REPOSITORY (or --github-repository); cannot build raw URLs.",
            file=sys.stderr,
        )
        return 1

    ref = _resolve_ref(args.github_ref)

    _write_readme_extract(dest, args.archive_base)
    _write_markdown_raw_list(workspace=workspace, dest=dest, repo_full=repo_full, ref=ref)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
