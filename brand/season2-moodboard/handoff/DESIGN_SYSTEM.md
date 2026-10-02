# ICL Season 2 — Design System

Visual system for **Imama Cricket League (ICL) Season 2** — a community cricket league run by UAE Imama (Dubai). Its only "product" is social content: Instagram feed posts (1080×1350), stories (1080×1920) and occasional print, posted across the season (announcement → auction/team reveal → countdown → match days → results → awards → thank-you).

Direction name: **Second Innings.** Season 1 lived under night lights (green washes, stadium skies, framed photo cards). Season 2 steps into the floodlight: white grounds, giant numerals, motion ribbons and the script-over-caps signature, louder.

## Sources
- Season 1 final posters, 13 files (`uploads/Final/*.jpg`): coming soon, owners intro, team reveal, auction, countdowns 4→1, match day, fixtures, results, man of the series.
- ICL logo colourways master (`uploads/Final/Logo_Colourways.jpg` → `assets/icl-logo-colourways.jpg`).
- 22 Season 2 reference images (`uploads/*.jpg`), sorted into 7 device groups in `ICL Season 2 Moodboard.dc.html`.
- The moodboard (`ICL Season 2 Moodboard.dc.html`) is the narrative version of this system.

No codebase, Figma or font files were provided.

## Index
- `styles.css` — entry point (imports only). Link this one file.
- `tokens/` — `colors.css`, `typography.css`, `spacing.css`, `effects.css`, `fonts.css`
- `assets/` — `icl-logo-ink.png`, `icl-logo-white.png`, `icl-logo-green.png` (single-colour cutouts of the lockup), `icl-logo-colourways.jpg` (master), `s1-*.png` (Season 1 references)
- `guidelines/` — 19 foundation specimen cards
- `components/`
  - `graphics/` — `Numeral`, `ScriptCaps`, `TornTape`, `Ribbon`, `PlayerCutout`
  - `labels/` — `CrosshairRule`, `RoleBadge`, `HandCircle`, `TeamTag`, `StatBlock`
  - `cards/` — `WalkoutCard`, `JerseyTile`
  - `poster/` — `PosterFrame`, `PosterHeader`
- `ui_kits/social/` — poster studio with 7 templates
- `ICL Season 2 Moodboard.dc.html` — moodboard
- `SKILL.md` — agent skill wrapper

### Component rationale
No source defined a component inventory. Because the output is posters, not app UI, the set is poster devices rather than a standard form/UI kit (no Button/Input/Tabs). Each maps to a device from the moodboard: Numeral (02.A), ScriptCaps (02.B), Ribbon (02.C), WalkoutCard + JerseyTile (02.D), CrosshairRule/RoleBadge/HandCircle (02.E), TornTape + halftone (02.F), quiet ground (02.G).

## Content fundamentals
- **Voice:** a hype-man with a scorecard — short, loud, confident, then precise. Headlines shout; detail lines are dry facts.
- **Headlines:** 1–3 words, ALL CAPS display. "WE GO AGAIN", "MATCH DAY", "DAYS TO GO", "FIXTURES", "FINAL".
- **Script phrase:** one per poster, title case, names the moment: "Second Innings", "Match Day", "Countdown", "Group Stage", a player's first name.
- **Data lines:** mono, ALL CAPS, "+" or "·" separated: "SAT · DEC 12 + 09:00 + GROUND 01". Scores cricket-style: "64* (31)", "3/18 (4)", "4×6", "SR 206.4".
- **Person:** none on posters — no "you", no "we" except set phrases ("WE GO AGAIN", "THANK YOU TO EVERY PLAYER & FAN").
- **Names:** team names in full caps ("BLUE TITANS"); abbreviations only in mono meta ("BT vs DD", "M07").
- **No emoji, no hashtags on the artwork,** no exclamation marks — energy comes from scale, not punctuation.

## Visual foundations
- **Colour:** Imama Green #19C571 is the hit (numerals, script, highlights). Royal Violet #5B2A92 carries tape and script on light; Orchid #C86AE8 replaces it on dark. Floodlight #F2F1EC / White are the default grounds; Pitch Night #0A2A1C for countdowns/finals; Quiet #07130D for tributes. Flare #FF5B24 is new — circled dates, the final, LIVE — ≤4% of a poster. Light-poster proportion ≈ 55 ground / 18 ink / 15 green / 8 violet / 4 flare. Team kit colours appear only in panels, swatches and ribbons.
- **Gradient:** exactly one — `--gradient-collage` (green → deep green → pitch, 165°), for UI collage posters only. No other gradients except contact shadows and texture masks.
- **Type:** Big Shoulders Display 900 for caps and numerals (leading 0.82, numerals −0.04em). Mrs Saint Delafield for the script, always rotated −8° and crossing caps. Outfit for sans body/UI (echoes the logo's geometric lowercase). JetBrains Mono for all data, +0.14em tracking, caps.
- **Layout:** 1080×1350 canvas, 72px side margins, 64px top, 54px grid. Logo top-left + mono meta top-right; crosshair footer rule along the bottom. One giant numeral ≈65% of poster height, player cutout in front with feet below the numeral baseline.
- **Imagery:** player cutouts (transparent PNG) on hard contact shadows — no framed photo cards, no stock stadium skies, no lens flares. Action photos only inside collage tiles. Colour photography as shot; no duotone on players.
- **Backgrounds/textures:** graph-paper grid (radially faded on light), green halftone dots on night grounds (masked, ≤50%), torn violet tape. All CSS — no texture files.
- **Motion (reels/stories):** ribbons and streaks show motion statically; when animating, use quick scale-punches and wipes, no bounce. Script draws on last.
- **Borders:** 1px hairline #D8D6CE on board/specimen panels; posters themselves have none. Calendar grids and fixture rows use 1px rules.
- **Shadows:** only contact shadows under cutouts (`--shadow-contact`). No drop shadows on type or cards.
- **Transparency/blur:** only on WalkoutCard (frosted 86% floodlight, 16px blur) over collage grounds.
- **Radii:** posters 4, tiles 6, UI cards 24, pills/role circles round. The hand-drawn circle uses an irregular radius and −8° rotation.
- **Cards:** mostly absent — posters are compositions, not card grids. The one card is the frosted WalkoutCard.
- **Hover/press:** not applicable to posters. In the poster studio UI, selection = ink fill; no scale effects.

## Iconography
No icon set exists in the sources and none is used. Graphic marks are typographic: "+" as separator and crosshair, "·" as divider, "×" in stats ("4×6"), "*" for not-out. Role codes (BAT/BWL/AR/WK) in outlined circles stand in for role icons. Play/pause glyphs in WalkoutCard are CSS shapes. No emoji. If icons become necessary (e.g. a live-score story), use Lucide via CDN at 2px stroke and flag it.

## Logo
`assets/icl-logo-*.png` were cut from the colourways master, so they are single-colour (ink, white, green). Never redraw or recolour beyond these. Ink on light grounds, white on night/gradient/violet, green allowed on Pitch Night.

## Caveats
- Fonts are Google Fonts chosen to match Season 1's look (no font files were provided).
- Team colours are estimated from Season 1 posters — confirm against Season 2 kits.
- Dates, venue, times and names in templates are placeholders.
