# Handoff: ICL Season 2 — "Second Innings" poster system

## Overview
Visual system + poster templates for Imama Cricket League Season 2 social content: Instagram feed (1080×1350), stories (1080×1920), occasional print. Includes moodboard, tokens, poster-device components and a poster studio (pick template, edit copy live).

Full brand rules (voice, colour proportions, grid, imagery, logo use) are in `DESIGN_SYSTEM.md` — read it first.

## About the Design Files
These are **design references in HTML/JSX**, not production code. Recreate them in the target environment. If none exists, use React + Vite: render each poster as a fixed 1080×1350 DOM node, export PNG via `html-to-image` or Playwright.

## Fidelity
High-fidelity, except: fonts are Google stand-ins, team colours are estimates, dates/names/venues/cutouts are placeholders.

## Screens
### Poster studio — `ui_kits/social/index.html`, `posters.jsx`
- 3 columns: template list | preview | copy form. Side panels scroll independently. Preview = 1080×1350 node with `transform: scale(availableWidth/1080)`, never cropped.
- Selected template = ink fill `#0E100D`, floodlight text. No hover motion.
- Templates (`<Template w={displayWidth} d={data}/>`):
  1. Season announcement — giant "02", "Second Innings" script over "WE GO AGAIN"
  2. Countdown — Pitch Night ground, day numeral, halftone, "DAYS TO GO"
  3. Match day — team vs team, mono line (date · time · ground)
  4. Player of the match — cutout over numeral, StatBlock ("64* (31)")
  5. Squad/walkout — collage gradient + frosted WalkoutCard
  6. Fixtures — 1px-ruled rows, mono meta
  7. Thank-you — Quiet ground `#07130D`
- Frame: 72px side margins, 64px top, 54px grid; logo top-left, mono meta top-right; crosshair rule at bottom.

### Moodboard — `ICL Season 2 Moodboard.dc.html`
Narrative reference (open in browser; needs `support.js`). Reference photos in `uploads/` not included.

### Specimens — `guidelines/*.card.html`, `components/*/*.card.html`
Visual specs per foundation/component.

## Components (`components/`)
Each has `.jsx` (reference), `.d.ts` (props), `.prompt.md` (rules).
- graphics: `Numeral` (~65% poster height, −0.04em, leading .8), `ScriptCaps` (script −8° crossing caps), `TornTape`, `Ribbon`, `PlayerCutout` (PNG + contact shadow; dashed placeholder)
- labels: `CrosshairRule`, `RoleBadge` (BAT/BWL/AR/WK), `HandCircle` (flare, −8°), `TeamTag`, `StatBlock`
- cards: `WalkoutCard` (86% floodlight, 16px blur, r24), `JerseyTile`
- poster: `PosterFrame`, `PosterHeader`

## Behaviour & State
- Template click swaps preview; inputs update live; preview rescales on resize (ResizeObserver).
- State: `templateId`, per-template `data` (headline, script, numeral, teams, date/time/venue, player, stats, cutout src).
- Posters static. Reels: scale-punches/wipes, no bounce, script draws last.
- Suggested: cutout upload, PNG export, 1080×1920 story variant.

## Design Tokens (`tokens/*.css` via `styles.css`)
Colours:
- Green `#19C571` / bright `#1ED67C` / deep `#0E8A4E` — numerals, script, highlights
- Violet `#5B2A92` (on light), Orchid `#C86AE8` (on dark)
- Floodlight `#F2F1EC`, White `#FFFFFF` — grounds
- Flare `#FF5B24` — circled dates, finals, LIVE; ≤4%
- Pitch Night `#0A2A1C`, Quiet `#07130D`
- Ink `#0E100D`, `#33352F`, `#55574F`; lines `#D8D6CE`, `#CFCDC4`; ghost `#E4E2DA`
- Teams (placeholder): Blue Titans `#1F6FE5`, Enhance Royals `#2BCB86`, First Legends `#D63441`, Desert Devils `#E9C23A`, Bizpoint Strikers `#A54FD6`, Nahda Super Kings `#E39A2A`, Sky `#8DB6F5`
- Only gradient: `linear-gradient(165deg,#1ED67C 0%,#0E8A4E 50%,#0A2A1C 100%)`

Type:
- Big Shoulders Display 900/800, leading .82, caps
- Mrs Saint Delafield script, −8°
- Outfit 300–700 body
- JetBrains Mono, caps, +0.14em
- Poster px: numeral 860, h1 250, script 170, h2 150, name 104, h3 76, team 38, body 32, mono 20/18
- Screen px: 300, 88, 48, 22, 16, 13, 11

Spacing: 4, 8, 12, 16, 24, 32, 48, 64, 80. Radii: poster 4, tile 6, card 24, pill 999, hand-circle `52% 48% 55% 45% / 58% 46% 54% 42%`.

Effects: contact shadow `radial-gradient(ellipse, rgba(14,16,13,.35), transparent 70%)`; grid texture 1px @7% ink, radially faded; halftone green 2px dots @14px. No drop shadows on type/cards.

## Assets (`assets/`)
- `icl-logo-ink/white/green.png` — single-colour logo cutouts. Ink on light, white on dark, green only on Pitch Night. Never redraw.
- `icl-logo-colourways.jpg` — master; `s1-*.png` — Season 1 refs.
- No icons; marks are typographic (+ · × *).

## Open items
Season 2 kit colours, vector logo, brand fonts, 2–3 player cutouts.
