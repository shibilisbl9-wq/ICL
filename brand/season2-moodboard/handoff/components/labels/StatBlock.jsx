/** Big display stat with a mono detail line. */
export function StatBlock({ value, detail, size = 130, align = "left", color = "inherit", accent, style }) {
  return (
    <div style={{ textAlign: align, color, ...style }}>
      <div style={{ fontFamily: "var(--font-display)", fontWeight: 900, fontSize: size, lineHeight: .85, color: accent || "inherit" }}>{value}</div>
      {detail ? <div style={{ fontFamily: "var(--font-mono)", fontSize: Math.max(12, Math.round(size * 0.14)), letterSpacing: ".12em", textTransform: "uppercase", marginTop: Math.round(size * 0.09) }}>{detail}</div> : null}
    </div>
  );
}
