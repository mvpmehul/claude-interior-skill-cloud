#!/usr/bin/env bash
# Plan (or, with --execute APPROVAL_ID, run) one hall view through the banana skill.
# Usage: designs/hall/plan.sh VIEW PHOTO [--execute APPROVAL_ID]
#   VIEW is living | dining_kitchen | dining_mandir
#   PHOTO is the cleaned living/dining-kitchen photo, or the original dining-end photo.
# Without --execute it only plans (no Google call, no cost) and prints the plan JSON.
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
skill="$here/../../.claude/skills/banana/scripts"
view="$1"; photo="$2"; shift 2
case "$view" in
  living) alias="living room photo (man removed)" ;;
  dining_kitchen) alias="dining and kitchen photo" ;;
  dining_mandir) alias="dining end photo" ;;
  *) echo "unknown view: $view" >&2; exit 2 ;;
esac
extra=()
if [[ "${1:-}" == "--execute" ]]; then extra=(--execute --confirm "$2"); fi
python3 "$skill/edit.py" \
  --image "$photo" --reference-name "$alias" --reference-role object \
  --reference-purpose "preserve room architecture, openings and camera viewpoint" \
  --reference-subject-id hall --brief-file "$here/brief_$view.json" \
  --prompt "$(cat "$here/prompt_$view.txt")" \
  --model gemini-nano-banana-2.1 --aspect-ratio 4:3 --resolution 1K \
  --output-dir "${HALL_OUT:-$HOME/hall-designs}" --label "hall-${view//_/-}" "${extra[@]}"
