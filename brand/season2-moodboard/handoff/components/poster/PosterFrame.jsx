/** 1080-wide poster canvas with a brand ground + texture, scaled to fit a preview width. */
const GROUNDS = {
  floodlight: { bg: "var(--icl-floodlight)", fg: "var(--text-primary)" },
  white: { bg: "var(--icl-white)", fg: "var(--text-primary)" },
  night: { bg: "var(--surface-night)", fg: "var(--text-on-dark)" },
  quiet: { bg: "radial-gradient(ellipse at 50% 28%,rgba(25,197,113,.22),transparent 60%),var(--surface-quiet)", fg: "var(--text-on-dark)" },
  gradient: { bg: "var(--gradient-collage)", fg: "var(--text-on-dark)" }
};
export function PosterFrame({ ground = "white", texture = "none", format = "feed", displayWidth, children, style }) {
  const g = GROUNDS[ground] || GROUNDS.white;
  const H = format === "story" ? 1920 : format === "square" ? 1080 : 1350;
  const k = displayWidth ? displayWidth / 1080 : 1;
  const dark = ground === "night" || ground === "quiet" || ground === "gradient";
  let tex = null;
  if (texture === "grid") tex = <div style={{ position: "absolute", inset: 0, backgroundImage: dark ? "var(--texture-grid-dark)" : "var(--texture-grid)", backgroundSize: "var(--grid-unit) var(--grid-unit)", maskImage: dark ? "none" : "var(--fade-center)", WebkitMaskImage: dark ? "none" : "var(--fade-center)" }} />;
  if (texture === "halftone") tex = <div style={{ position: "absolute", inset: 0, backgroundImage: "var(--texture-halftone)", backgroundSize: "var(--texture-halftone-size)", maskImage: "radial-gradient(ellipse 60% 55% at 65% 40%,#000,transparent 75%)", WebkitMaskImage: "radial-gradient(ellipse 60% 55% at 65% 40%,#000,transparent 75%)" }} />;
  return (
    <div style={{ position: "relative", width: 1080 * k, height: H * k, overflow: "hidden", borderRadius: "var(--radius-poster)", ...style }}>
      <div style={{ position: "absolute", left: 0, top: 0, width: 1080, height: H, transform: "scale(" + k + ")", transformOrigin: "0 0", overflow: "hidden", background: g.bg, color: g.fg, fontFamily: "var(--font-sans)" }}>
        {tex}
        {children}
      </div>
    </div>
  );
}
