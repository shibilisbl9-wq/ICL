/** Team name with its kit-colour swatch. */
export function TeamTag({ name, color, size = 38, side = "left", pill = false, style }) {
  const sw = <span style={{ width: size * 0.53, height: size * 0.53, flex: "none", background: color, borderRadius: pill ? "50%" : 0 }} />;
  const txt = <span style={{ fontFamily: "var(--font-display)", fontWeight: 800, fontSize: size, lineHeight: 1, textTransform: "uppercase", whiteSpace: "nowrap" }}>{name}</span>;
  return (
    <span style={{ display: "inline-flex", alignItems: "center", gap: size * 0.37, ...(pill ? { padding: "6px 16px 6px 6px", border: "1px solid var(--border-hairline)", borderRadius: "var(--radius-pill)", background: "var(--surface-paper)" } : {}), ...style }}>
      {side === "left" ? <>{sw}{txt}</> : <>{txt}{sw}</>}
    </span>
  );
}
