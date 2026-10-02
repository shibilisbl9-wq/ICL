/** Giant display numeral that sits behind a player cutout. */
export function Numeral({ children, size = 860, color = "var(--accent-hit)", style }) {
  return (
    <div style={{ fontFamily: "var(--font-display)", fontWeight: 900, fontSize: size, lineHeight: "var(--leading-numeral)", letterSpacing: "var(--tracking-numeral)", color, userSelect: "none", ...style }}>
      {children}
    </div>
  );
}
