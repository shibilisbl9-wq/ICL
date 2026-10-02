/** Frosted music-player card for walkout-song collages. */
export function WalkoutCard({ title = "Walkout song", artist = "Artist name", cover, progress = 0.42, elapsed = "1:14", remaining = "−2:31", scale = 1, style }) {
  const s = (n) => n * scale;
  const tri = (dir) => <span style={{ width: 0, height: 0, borderTop: s(11) + "px solid transparent", borderBottom: s(11) + "px solid transparent", [dir === "l" ? "borderRight" : "borderLeft"]: s(16) + "px solid var(--icl-ink)" }} />;
  return (
    <div style={{ width: s(540), padding: s(24), borderRadius: s(24), background: "rgba(242,241,236,.86)", backdropFilter: "blur(var(--blur-card))", WebkitBackdropFilter: "blur(var(--blur-card))", color: "var(--icl-ink)", display: "grid", gridTemplateColumns: s(120) + "px minmax(0,1fr)", gap: s(22), alignItems: "center", fontFamily: "var(--font-sans)", ...style }}>
      <div style={{ width: s(120), height: s(120), borderRadius: s(12), background: "var(--icl-ink)", overflow: "hidden", display: "flex", alignItems: "center", justifyContent: "center", color: "var(--icl-green)", fontFamily: "var(--font-display)", fontWeight: 900, fontSize: s(48) }}>
        {cover ? <img src={cover} alt="" style={{ width: "100%", height: "100%", objectFit: "cover" }} /> : "S2"}
      </div>
      <div>
        <div style={{ fontWeight: 600, fontSize: s(32), lineHeight: 1.15 }}>{title}</div>
        <div style={{ fontSize: s(22), color: "var(--text-muted)" }}>{artist}</div>
        <div style={{ marginTop: s(16), height: s(6), borderRadius: s(3), background: "rgba(14,16,13,.15)" }}><div style={{ width: progress * 100 + "%", height: "100%", borderRadius: s(3), background: "var(--icl-ink)" }} /></div>
        <div style={{ display: "flex", justifyContent: "space-between", marginTop: s(8), fontFamily: "var(--font-mono)", fontSize: s(16), color: "var(--text-muted)" }}><span>{elapsed}</span><span>{remaining}</span></div>
        <div style={{ display: "flex", justifyContent: "center", alignItems: "center", gap: s(40), marginTop: s(6) }}>
          <div style={{ display: "flex" }}>{tri("l")}{tri("l")}</div>
          <div style={{ display: "flex", gap: s(8) }}><span style={{ width: s(8), height: s(26), background: "var(--icl-ink)" }} /><span style={{ width: s(8), height: s(26), background: "var(--icl-ink)" }} /></div>
          <div style={{ display: "flex" }}>{tri("r")}{tri("r")}</div>
        </div>
      </div>
    </div>
  );
}
