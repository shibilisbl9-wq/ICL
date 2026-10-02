/** Player cutout (transparent PNG) standing on a contact shadow. Shows a dashed placeholder without src. */
export function PlayerCutout({ src, alt = "", width = 520, height = 880, night = false, label = "Player cutout · PNG", style }) {
  const ink = night ? "var(--text-on-dark)" : "var(--text-primary)";
  return (
    <div style={{ position: "relative", width, height, ...style }}>
      <div style={{ position: "absolute", left: "-8%", right: "-8%", bottom: -20, height: 50, background: night ? "var(--shadow-contact-night)" : "var(--shadow-contact)" }} />
      {src ? <img src={src} alt={alt} style={{ position: "absolute", inset: 0, width: "100%", height: "100%", objectFit: "contain", objectPosition: "bottom" }} />
        : <div style={{ position: "absolute", inset: 0, border: "3px dashed " + ink, borderRadius: (width / 2) + "px " + (width / 2) + "px 16px 16px", display: "flex", alignItems: "center", justifyContent: "center", color: ink, fontFamily: "var(--font-mono)", fontSize: 20, letterSpacing: ".14em", textTransform: "uppercase", opacity: .7 }}>{label}</div>}
    </div>
  );
}
