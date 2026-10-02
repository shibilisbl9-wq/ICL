/** Condensed caps headline with a script phrase slicing across it — the ICL signature. */
export function ScriptCaps({ caps, script, capsSize = 180, scriptSize, scriptColor = "var(--accent-script-light)", capsColor = "var(--text-primary)", align = "left", offsetX = 0.3, offsetY = 0.35, angle = -8, style }) {
  const s = scriptSize || Math.round(capsSize * 0.95);
  const lines = String(caps).split("\n");
  return (
    <div style={{ position: "relative", display: "inline-block", textAlign: align, ...style }}>
      <div style={{ fontFamily: "var(--font-display)", fontWeight: 900, fontSize: capsSize, lineHeight: "var(--leading-display)", color: capsColor, whiteSpace: "nowrap" }}>
        {lines.map((l, i) => <div key={i}>{l}</div>)}
      </div>
      {script ? (
        <div style={{ position: "absolute", left: (offsetX * 100) + "%", top: (offsetY * 100) + "%", transform: "translate(-15%,-30%) rotate(" + angle + "deg)", fontFamily: "var(--font-script)", fontSize: s, lineHeight: 1, color: scriptColor, whiteSpace: "nowrap", pointerEvents: "none" }}>{script}</div>
      ) : null}
    </div>
  );
}
