Buttons carry one action each; `icl-btn--primary` (league-purple) for the main action on a view, `icl-btn--go` (imama-green) only for live/"watch now" actions, `icl-btn--ghost` for secondary ones.

- Consumer provides: a `<button>` or `<a>` with `icl-btn` plus one modifier, and a verb label ("Buy tickets", "Watch live").
- One primary per view. Never put two green buttons side by side.
- Labels in sentence case, not tracked caps; tracked caps are reserved for badges and eyebrows.
- Focus: 2px solid `focus` ring, 2px offset (from bundle.css).
