#!/usr/bin/env python3
"""Generate static/llms.txt — a plain-text, LLM/agent-readable index of the site.

Run from the repository root after changing publications, talks or projects:

    python3 scripts/gen_llms.py

The output is committed and served at /llms.txt. Nothing here affects the
human-facing website.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content"
BASE = "https://adityamanglik.github.io"

SLUG_OVERRIDES = {
    "genpip_MICRO2022": "genpip_micro2022",
    "DRAM_Minesh": "dram_minesh",
    "MATSA": "matsa",
    "NEON": "neon",
    "revamp3d": "revamp3d",
    "adaptive_gait_ICPEICES_2016": "adaptive_gait_icpeices_2016",
}


def front_matter(path: Path) -> dict[str, str]:
    """Minimal YAML front-matter reader for the scalar keys we need."""
    text = path.read_text(encoding="utf-8", errors="ignore")
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end == -1:
        return {}
    block = text[3:end]
    out: dict[str, str] = {}
    for line in block.splitlines():
        m = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if not m:
            continue
        key, val = m.group(1), m.group(2).strip()
        if not val:
            continue
        if (val.startswith("'") and val.endswith("'")) or (
            val.startswith('"') and val.endswith('"')
        ):
            val = val[1:-1]
        out[key] = val
    return out


def clean(s: str) -> str:
    """Strip lightweight markdown emphasis used in venue names."""
    return re.sub(r"[*_`]", "", s).strip()


def slug_for(directory: Path, meta: dict[str, str]) -> str:
    name = directory.name
    return SLUG_OVERRIDES.get(name, name.lower())


def collect(section: str) -> list[tuple[str, dict[str, str], Path]]:
    base = CONTENT / section
    if not base.is_dir():
        return []
    items = []
    for d in sorted(base.iterdir()):
        index = d / "index.md"
        if d.is_dir() and index.exists():
            items.append((d.name, front_matter(index), d))
    items.sort(key=lambda t: t[1].get("date", ""), reverse=True)
    return items


def main() -> int:
    pubs = collect("publication")
    talks = collect("event")
    projects = collect("project")

    lines: list[str] = []
    lines.append("# Aditya Manglik")
    lines.append("")
    lines.append(
        "> Senior Engineer at Qualcomm Technologies and researcher in sustainable\n"
        "> computing, DRAM and memory systems, and operating-system energy and carbon\n"
        "> attribution. Co-host of The Week in Green Software (Green Software\n"
        "> Foundation). Green Software Champion."
    )
    lines.append("")
    lines.append(f"Homepage: {BASE}/")
    lines.append(f"Canonical entity: {BASE}/#person")
    lines.append("")
    lines.append("## Profiles")
    lines.append("")
    lines.append("- LinkedIn: https://www.linkedin.com/in/adityamanglik/")
    lines.append(
        "- Google Scholar: https://scholar.google.com/citations?user=hEy3GXAAAAAJ&hl=en"
    )
    lines.append("- GitHub: https://github.com/adityamanglik")
    lines.append(
        "- Green Software Champions: "
        "https://champions.greensoftware.foundation/champions/aditya-manglik/"
    )
    lines.append("")

    lines.append("## Publications")
    lines.append("")
    for name, meta, _ in pubs:
        year = meta.get("date", "")[:4]
        venue = clean(meta.get("publication_short") or meta.get("publication") or "")
        doi = meta.get("doi", "")
        bits = [f"- {clean(meta.get('title', name))}"]
        if year:
            bits.append(f"({year}).")
        if venue:
            bits.append(f"{venue}.")
        if doi:
            bits.append(f"doi:{doi}")
        bits.append(f"{BASE}/publication/{slug_for(Path(name), meta)}/")
        lines.append(" ".join(bits))
    lines.append("")

    lines.append("## Talks")
    lines.append("")
    for name, meta, _ in talks:
        date = meta.get("date", "")[:10]
        title = clean(meta.get("title", name))
        event = clean(meta.get("event", ""))
        location = clean(meta.get("location", ""))
        bits = [f"- {date} — {title}."]
        if event:
            bits.append(f"{event}.")
        if location:
            bits.append(f"{location}.")
        bits.append(f"{BASE}/event/{name.lower()}/")
        lines.append(" ".join(bits))
    lines.append("")

    lines.append("## Projects")
    lines.append("")
    for name, meta, _ in projects:
        title = clean(meta.get("title", name))
        summary = clean(meta.get("summary", ""))
        lines.append(f"- {title}: {summary} {BASE}/project/{name.lower()}/")
    lines.append("")

    lines.append("## Pages")
    lines.append("")
    lines.append(f"- Publications: {BASE}/publication/")
    lines.append(f"- Talks: {BASE}/event/")
    lines.append(f"- Projects: {BASE}/project/")
    lines.append(f"- Honors & Awards: {BASE}/honors/")
    lines.append(f"- Experience: {BASE}/experience/")
    lines.append("")

    out = ROOT / "static" / "llms.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {out} ({len(pubs)} publications, {len(talks)} talks, {len(projects)} projects)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
