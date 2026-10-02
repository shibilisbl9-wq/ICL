/** Outlined circle with a player role code (BAT / BWL / AR / WK). */
export function RoleBadge({ role = "BAT", size = 50, active = false, dark = false, style }) {
  const c = active ? "var(--icl-violet)" : dark ? "var(--text-on-dark)" : "var(--text-primary)";
  return (
    <span style={{ width: size, height: size, borderRadius: "50%", border: "2px solid " + c, color: c, background: dark ? "transparent" : "var(--surface-paper)", display: "inline-flex", alignItems: "center", justifyContent: "center", fontFamily: "var(--font-mono)", fontWeight: 700, fontSize: Math.round(size * 0.24), flex: "none", ...style }}>{role}</span>
  );
}
