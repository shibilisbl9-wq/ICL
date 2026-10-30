# ICL Season 2 team reveal posters

- `team-01-blue-tick.png` … `team-06-brothers-untd.png`: one 1080×1350 post per team. Three square frames: icon, owner (highlighted), manager.
- `teams-all-six.png`: all six teams on one 1080×1350 post.
- `preview-contact-sheet.png`: the six team posters side by side (for review, not for posting).

Real photos only, shown in black and white. Anyone without a photo gets a "PHOTO SOON" placeholder.

## Updating a photo or name

1. Put the photo in `source/photos/raw/`.
2. In `source/teams.json`, set that person's `"photo"` to the file name and `"crop"` to `[x, y, size]`: a square in the photo's own pixels, around head and chest.
3. Run `python3 source/make_team_reveal.py` (needs `rsvg-convert`, Pillow, Montserrat and Montserrat Alternates installed).

## Photos still missing

| Team | Missing |
|---|---|
| Yazbatheel | Rishal Kannikkad (icon), Mammu Kodiyamma (manager) |
| Enhance Royals | Sinan Nekraje (icon), Mahroof MA (manager) |
| Smart Pass | Shuhaib (icon), Sayyid Hashir (manager) |
| Brothers Untd. | Azad AK (icon), Mohd. Usama (manager) |

People were matched to photos by eye against the Season 2 auction posters. Check every face before posting.
