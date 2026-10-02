/** Poster top bar: logo left, mono meta lines right (or swapped). */
export function PosterHeader({ logoSrc = "assets/icl-logo-ink.png", logoWidth = 160, meta = [], swap = false, top = 64, style }) {
  const logo = <img src={logoSrc} alt="Imama Cricket League" style={{ width: logoWidth, display: "block" }} />;
  const m = <div style={{ fontFamily: "var(--font-mono)", fontSize: 20, lineHeight: 1.6, letterSpacing: "var(--tracking-mono)", textTransform: "uppercase", textAlign: swap ? "left" : "right" }}>{meta.map((l, i) => <div key={i}>{l}</div>)}</div>;
  return (
    <div style={{ position: "absolute", left: "var(--poster-margin)", right: "var(--poster-margin)", top, display: "flex", justifyContent: "space-between", alignItems: "flex-start", ...style }}>
      {swap ? <>{m}{logo}</> : <>{logo}{m}</>}
    </div>
  );
}
