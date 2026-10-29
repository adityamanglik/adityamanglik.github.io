#!/usr/bin/env bash
# Toggle the DRAM Timing Reference Guide between private and public.
#
#   bash scripts/dram-visibility.sh hide   # private (default): /dram/ is not
#                                          # rendered, listed, or published
#   bash scripts/dram-visibility.sh show   # public: /dram/ is fully published
#
# What it changes:
#   1. content/dram/_index.md  — `build:` + `cascade:` options (Hugo build
#      options cascade to every descendant page of the section).
#   2. config/_default/menus.yaml — comments out the "DRAM Timings" navbar
#      entry while hidden so visitors never see a dead link.
#
# Nothing under content/dram/ is deleted or modified in either mode.
set -euo pipefail

MODE="${1:?usage: dram-visibility.sh hide|show}"
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
INDEX="$ROOT/content/dram/_index.md"
MENU="$ROOT/config/_default/menus.yaml"

if [[ "$MODE" == "hide" ]]; then
  LIST=never;  RES=false; RENDER=never
elif [[ "$MODE" == "show" ]]; then
  LIST=always; RES=true;  RENDER=always
else
  echo "unknown mode: $MODE (use hide or show)" >&2
  exit 1
fi

python3 - "$INDEX" "$MENU" "$LIST" "$RES" "$RENDER" "$MODE" <<'PY'
import re
import sys

index_path, menu_path, list_v, res_v, render_v, mode = sys.argv[1:]
text = open(index_path).read()

# Rewrite the three build-option values in both the section's own `build:`
# block and the indented `cascade:` block. Indentation is flexible, and the
# substitutions are confined to the front matter so body text is untouched.
pairs = [
    (r"(?m)^(\s*list: )(?:never|always)$", rf"\g<1>{list_v}"),
    (r"(?m)^(\s*publishResources: )(?:false|true)$", rf"\g<1>{res_v}"),
    (r"(?m)^(\s*render: )(?:never|always)$", rf"\g<1>{render_v}"),
]
head, sep, body = text.partition("\n---\n")
if not sep:
    sys.exit(f"ERROR: front matter delimiter not found in {index_path}")
for pattern, repl in pairs:
    head, n = re.subn(pattern, repl, head)
    if n != 2:  # once in `build:`, once in `cascade:`
        sys.exit(f"ERROR: expected 2 matches for {pattern!r} in {index_path}, got {n}")
open(index_path, "w").write(head + sep + body)

menu = open(menu_path).read()
if mode == "hide":
    menu = re.sub(
        r"(?m)^  - name: DRAM Timings\n    url: 'dram/'\n    weight: 35\n",
        "# DRAM guide hidden — restore with: bash scripts/dram-visibility.sh show\n"
        "#   - name: DRAM Timings\n#     url: 'dram/'\n#     weight: 35\n",
        menu,
    )
else:
    menu = re.sub(
        r"# DRAM guide hidden[^\n]*\n"
        r"#   - name: DRAM Timings\n#     url: 'dram/'\n#     weight: 35\n",
        "  - name: DRAM Timings\n    url: 'dram/'\n    weight: 35\n",
        menu,
    )
open(menu_path, "w").write(menu)
print(f"DRAM guide is now {mode.upper()}: build options = list:{list_v}, "
      f"publishResources:{res_v}, render:{render_v}")
PY
