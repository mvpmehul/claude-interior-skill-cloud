# Hall design: Warm Modern

Interior design concept for the living + dining hall (drawing 11'6" x 19'0",
dining 9'6" x 13'3", open kitchen 11'0" x 10'9"), made with the `banana` skill.
Photos of the flat are deliberately **not** stored here because this repository
is public. Re-attach them in the session that runs the designs.

## Concept

Calm, sunlit modern Indian home: warm ivory limewash, walnut, soft brushed brass,
with sage and terracotta accents. The existing beige marble-look floor tiles stay.

- **Living:** TV wall with a backlit honey-onyx-look panel framed by full-height
  walnut fluting and a floating walnut console; curved oatmeal boucle 3-seater,
  36" round travertine coffee table on an 8x10 ft wool rug, cognac lounge chair
  with brass floor lamp; ripple-fold ivory linen sheers (plus blackout) on the
  sliding doors; perimeter cove ceiling at 3000K with slim spotlights; olive tree.
- **Dining + kitchen:** 6-seat oval (about 72" x 36") travertine-top table on a
  walnut base, curved oatmeal chairs, three amber-glass pendants; central column
  clad in walnut fluting with a brass inlay; handleless warm-greige and walnut
  kitchen with quartz counter, existing dark grey tiles kept as backsplash;
  walnut vanity, cream stone basin and round brass mirror at the wash basin.
- **Mandir:** on the dining-end wall (where the builder poster display was): a
  wall-mounted walnut mandir about 4 ft wide, arched top, softly backlit brass
  lotus jaali, two drawers, flanked by slim walnut fluting. Vastu: northeast is
  ideal, facing east or north while praying; confirm with a compass.

## Views

| View | Photo to attach | Brief | Prompt |
|---|---|---|---|
| `living` | IMG_8799 (sliding doors left, bedroom door right), cleaned | `brief_living.json` | `prompt_living.txt` |
| `dining_kitchen` | IMG_8791 (kitchen opening in the middle), cleaned | `brief_dining_kitchen.json` | `prompt_dining_kitchen.txt` |
| `dining_mandir` | IMG_8793 (poster wall, glass doors right), as is | `brief_dining_mandir.json` | `prompt_dining_mandir.txt` |

The owner confirmed these are their own photos and approved sending them to
Google Gemini for private design previews (not for publication). They asked for
the man standing by the glass in IMG_8799 to be removed **before** sending.

## Run it in a new cloud session

Needs `GEMINI_API_KEY` set as an environment variable in the cloud environment.

1. Attach IMG_8799, IMG_8791 and IMG_8793 to the message.
2. Remove people locally:
   `pip install opencv-python-headless && python3 designs/hall/clean_photos.py IMG_8799 IMG_8791 OUT_DIR`
3. Plan each view (free, no Google call):
   `designs/hall/plan.sh living OUT_DIR/living_clean.jpg` (and `dining_kitchen`
   with `OUT_DIR/dining_clean.jpg`, `dining_mandir` with IMG_8793).
4. Show the owner the plan and get approval for the paid call, then run
   `designs/hall/plan.sh VIEW PHOTO --execute APPROVAL_ID`. Approvals expire
   after 30 minutes. Model Nano Banana 2.1 at 1K, about $0.034 per image
   (nominal estimate, not a cap). Outputs go to `$HALL_OUT` (default `~/hall-designs`),
   outside the repo.
5. Review every image against its brief before showing it.

Do not commit photos or generated designs to this public repository.
