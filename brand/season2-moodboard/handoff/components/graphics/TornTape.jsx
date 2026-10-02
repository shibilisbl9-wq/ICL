/** Violet torn-paper strip carrying a headline or repeating label. */
export function TornTape({ children, color = "var(--accent-tape)", textColor = "#FFFFFF", rotate = -3, height = 230, fontSize, mono = false, style }) {
  const fs = fontSize || (mono ? Math.round(height * 0.22) : Math.round(height * 0.85));
  return (
    <div style={{ height, background: color, clipPath: "var(--torn-edge)", transform: "rotate(" + rotate + "deg)", display: "flex", alignItems: "center", justifyContent: "center", color: textColor, whiteSpace: "nowrap", overflow: "hidden",
      fontFamily: mono ? "var(--font-mono)" : "var(--font-display)", fontWeight: mono ? 700 : 900, fontSize: fs, letterSpacing: mono ? ".2em" : ".01em", lineHeight: 1, ...style }}>
      {children}
    </div>
  );
}
