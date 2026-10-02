/** Hand-drawn Flare circle around a date, word or calendar cell. */
export function HandCircle({ children, color = "var(--accent-highlight)", stroke = 5, rotate = -8, pad = 14, style }) {
  return (
    <span style={{ position: "relative", display: "inline-block", ...style }}>
      {children}
      <span style={{ position: "absolute", left: -pad, top: -pad, right: -pad, bottom: -pad, border: stroke + "px solid " + color, borderRadius: "var(--radius-hand-circle)", transform: "rotate(" + rotate + "deg)", pointerEvents: "none" }} />
    </span>
  );
}
