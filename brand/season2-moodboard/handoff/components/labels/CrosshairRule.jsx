/** Hairline rule with "+"-separated mono items — every poster's footer strip. */
export function CrosshairRule({ items = [], color = "currentColor", size = 20, style }) {
  const parts = [];
  items.forEach((it, i) => { if (i) parts.push(<span key={"p" + i}>+</span>); parts.push(<span key={i}>{it}</span>); });
  return (
    <div style={{ display: "flex", alignItems: "center", gap: size, fontFamily: "var(--font-mono)", fontSize: size, letterSpacing: "var(--tracking-mono)", textTransform: "uppercase", color, whiteSpace: "nowrap", ...style }}>
      <span style={{ flex: 1, height: 1, background: color }} />{parts}<span style={{ flex: 1, height: 1, background: color }} />
    </div>
  );
}
