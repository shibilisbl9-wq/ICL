The Imama Cricket League (ICL) is a UAE IMAMA cricket event. Season 2 keeps the original identity exactly and adds one line to it: **SEASON 2**, set in the same tracked caps as the **UAE IMAMA** line at the top of the logo. Everything here is built from that logo: its two gradients, its tracked caps, its lowercase geometric wordmark, and the ball's speed-line trail.

## Voice

- Talk like the league announcer, not a corporation: short, warm, direct. "Gates open 6:30 pm. Bring the noise."
- Write facts as facts: scores, targets and times are plain sentences. "Strikers need 25 from 22."
- Headlines in lowercase in `display-*` styles, echoing the wordmark ("final day", "match 14"). Tracked caps (`label-caps`) only for 1–4 word eyebrows, badges and table headers, echoing "UAE IMAMA" and "SEASON 2".
- Say "Season 2", never "S2" or "Season II" in public copy.
- No emoji in official graphics. Numbers always as numerals.

## Colour

- `league-purple` is the primary brand colour: primary buttons, headings, active states, the SEASON line. `imama-green` is the second voice: live, "watch now", wins, qualification.
- The two logo gradients are part of the identity. Build them only from these stops and only on large display type or big graphic shapes:
  - imama gradient: `imama-green-bright` → `imama-green-deep`, top-left to bottom-right.
  - league gradient: `league-purple-bright` → `league-purple-mid` → `league-purple-deep`, top-left to bottom-right.
- Never put small text in a gradient, and never place `league-purple-bright` or `imama-green-bright` text on light grounds; they fail contrast.
- `night` is the broadcast ground: match-day graphics, social posts, the reversed logo. It stays dark in both themes.
- `boundary-gold` is rare and earned: 4s, 6s, fifties, hundreds, five-fors, the trophy. It is a fill with `night` text; it is never text on light grounds.
- `live` is only for LIVE and wicket (W) states, always with the word, never as decoration.
- Text pairs: `ink` and `ink-muted` on `surface`/`surface-raised`/`surface-sunken`; `on-league-purple` on `league-purple`; `on-imama-green` on `imama-green`; `on-night` on `night`. All meet 4.5:1 in both themes.

## Type

- Display face: **Montserrat Alternates** 600–700 (`--font-display`). It is the closest free match to the wordmark's single-storey "a" and "g"; it is not the logo's original font, so never re-set the logo in it: always use the logo files.
- Everything else: **Montserrat** 500–700 (`--font-sans`), which also matches the logo's tracked caps.
- Scale: `display-xl` 72, `display-l` 48, `score` 56, `heading` 28, `title` 20, `body` 16, `small` 14, `label-caps` 12 with 0.32em tracking.
- Scores, overs, run rates and tables always use tabular numerals.

## Layout, shape, depth

- Spacing steps `space-1`…`space-8` (4 to 64px). Cards pad `space-4` on phones, `space-5` on desktop; sections sit `space-7` apart.
- Corners: `radius-md` for cards and buttons, `radius-sm` for small elements, `radius-pill` for badges. The logo's letters have soft corners, so nothing is fully square and nothing is bubbly.
- Borders over shadows: cards use a 1px `hairline` border. Only score cards take `shadow-card`.
- Focus: 2px solid `focus` ring with 2px offset on every interactive element.

## Graphics and motion

- The one graphic motif is the ball's speed-line trail: 2–6 rounded streaks at 45°, running up-right. Use it on posters, social templates and section breaks; never more than one cluster per layout.
- Photos: real players and real grounds, floodlights welcome. Overlay the reversed logo on a `night` gradient band, not directly on the photo.
- Motion: score updates tick with a quick 150ms fade; nothing bounces.

## Social templates

- Square 1080×1080 and story 1080×1920 on `night`. Logo top-left at 220px wide (square) with clear space; `display-l` headline lowercase; `label-caps` eyebrow in `imama-green` (dark-theme value `#6fd08f`) above it.
- Match-day card: team names in `title`, score in `score`, one `boundary-gold` badge maximum.

## Logo

See the Logos asset group. Use the files; never retype the logo.
