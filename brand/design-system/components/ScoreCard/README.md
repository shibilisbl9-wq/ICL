The live or final score for one match: two team rows, runs/wickets in the display face, overs, and a one-line status.

- Consumer provides: match label, both team names, `runs/wickets` and overs per team, the status sentence, and whether the match is live.
- Mark the team at the crease with `icl-score__team--batting` (its score turns `imama-green`).
- Runs are always `tabular-nums` so scores don't jump as they update.
- Status line states the equation plainly: "Strikers need 25 runs from 22 balls", "Falcons won by 24 runs".
- Team names in examples are placeholders.
