# ICL Season 2 moodboard v3: "Powerplay" (red and blue)

**This is the Season 2 visual direction.** It replaces the earlier "Second Innings" board (on branch
`ccr-a6b0e9e5-tjflul`) and the `brand/design-system/` poster rules (Montserrat, lowercase, purple-led).
Season 1 posters were deliberately not used as a reference.

- `ICL-Season2-Moodboard.html`: the board. One self-contained file (fonts, logo, images embedded); open it in any browser, offline included.
- `ICL-Season2-Moodboard-preview.jpg`: full-page preview at 1200px wide, for sharing in chats.
- `tokens.css`: colour, type and frame tokens for production.
- `src/`: board source. Edit `moodboard.src.html` or the lists in `build.py`, then run `python3 src/build.py`.
  - `generated/*.webp`: 21 frames generated in Higgsfield (GPT Image 2.5, 2k) in the final palette.
  - `cutouts/*.webp`: three stand-in players (Higgsfield + background remover) used by the live templates.
  - `references/r01–r23.jpg`: the only inputs. R01–R20 set layouts and devices; R21–R23 set the final red and blue.
    Third-party posters: direction only, never trace, crop or post them.
  - `fonts/`: Archivo, Instrument Serif, JetBrains Mono, Mr Dafoe (all OFL, from Google Fonts).

## The system in one screen
| | |
|---|---|
| Grounds | Crease `#F5F3EE` (day), Ball Red `#E92D3C` (match day, countdown, awards), Electric Blue `#1234F9` (team sheets), Navy `#061433` (night, signal) |
| Type colour | Ink `#0B0C14` on light grounds, white on red, blue and navy. Never red on blue (1.7:1) |
| Type | Archivo ExtraCondensed Black caps (display, numerals) · Archivo Expanded ExtraBold Italic (tags) · Instrument Serif (names) · Mr Dafoe (one script word, loud posts) · JetBrains Mono (all data) |
| Frame | 1080×1350, 64px sides, 54px top, single-colour logo top left at 168px, mono meta top right, mono footer rule |
| Devices | Giant numbers · ribbons & streaks · break the frame · grids, circles & team sheets · duotone & scanlines · heat plates · loud & quiet |

## Still open
- Team kits: every frame uses one stand-in kit (electric blue, red and white trim). Swap in the real Season 2 team colours.
- Players: all faces are AI stand-ins. Shoot real players full body on a plain light-grey wall with hard light.
- Logo: the green and purple lockup sits outside this palette. Posters use it single colour (Ink or white) until a red and blue variant is decided.
- Generated frames contain AI-set words and invented placeholder names. Reset all copy in the real fonts before posting.
