/** Square ink tile with a jersey number — collage anchor. */
export function JerseyTile({ number = "07", size = 400, color = "var(--icl-ink)", textColor = "var(--text-on-dark)", style }) {
  return <div style={{ width: size, height: size, borderRadius: "var(--radius-tile)", background: color, color: textColor, display: "flex", alignItems: "center", justifyContent: "center", fontFamily: "var(--font-display)", fontWeight: 900, fontSize: size * 0.9, lineHeight: 1, ...style }}>{number}</div>;
}
