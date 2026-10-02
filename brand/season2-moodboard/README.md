# ICL Season 2 moodboard v4: "Powerplay" (navy, green and blue)

**This is the Season 2 visual direction.** It replaces the earlier "Second Innings" board (on branch
`ccr-a6b0e9e5-tjflul`) and the `brand/design-system/` poster rules (Montserrat, lowercase, purple-led).
Season 1 posters were deliberately not used as a reference.

- `ICL-Season2-Moodboard.html`: the board. One self-contained file (fonts, logo, images embedded); open it in any browser, offline included.
- `ICL-Season2-Moodboard-preview.jpg`: full-page preview at 1200px wide, for sharing in chats.
- `tokens.css`: colour, type and frame tokens for production.
- `src/`: board source. Edit `moodboard.src.html` or the lists in `build.py`, then run `python3 src/build.py`.
  - `generated/*.webp`: 21 frames generated in Higgsfield (GPT Image 2.5, 2k) in navy, green and blue.
  - `cutouts/*.webp`: three stand-in players (Higgsfield + background remover) used by the live templates.
  - `references/r01–r23.jpg`: the only design inputs. R01–R20 set layouts and devices; R21–R23 add the team sheet, signal and grain looks.
    Third-party posters: direction only, never trace, crop or post them.
  - `fonts/`: Archivo, Instrument Serif, JetBrains Mono, Mr Dafoe (all OFL, from Google Fonts).

## The system in one screen
| | |
|---|---|
| Palette | Navy `#061433` (default ground, kits), Deep `#030916` (portraits, results, signal), Imama Green `#1FCB62` (hero: numerals, headlines, trim, match-day grounds), Electric Blue `#1234F9` (ribbons, shards, team sheets), Chalk `#EEF2F7` (type only) |
| Rules | Dark grounds on most posts, no white grounds. Deep text on green; never chalk on green (1.9:1) or blue text on navy (2.5:1). Kits navy with green trim, never blue with orange/saffron (reads as India) |
| Type | Archivo ExtraCondensed Black caps (display, numerals) · Archivo Expanded ExtraBold Italic (tags) · Instrument Serif (names) · Mr Dafoe (one script word, loud posts) · JetBrains Mono (all data) |
| Frame | 1080×1350, 64px sides, 54px top, single-colour logo top left at 168px, mono meta top right, mono footer rule |
| Devices | Giant numbers · ribbons & streaks · break the frame · grids, circles & team sheets · duotone & scanlines · heat plates · loud & quiet |

## Still open
- Team kits: every frame uses one stand-in kit (navy with green trim). Swap in the real Season 2 team colours; keep green as trim, since an all-green kit reads as Pakistan or Bangladesh.
- Players: all faces are AI stand-ins. Shoot real players full body on a plain light-grey wall with hard light.
- Logo: posters use the lockup single colour (white, or Deep on green). Its green fits this palette; its purple does not.
- Generated frames contain AI-set words and invented placeholder names. Reset all copy in the real fonts before posting.
