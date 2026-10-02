/** Motion ribbon trailing the athlete — arc (bat swing / bowling) or streak (running). */
export function Ribbon({ variant = "arc", colors, size = 1400, width = 180, fadeFrom = 0.38, style }) {
  const c = colors && colors.length ? colors : ["var(--team-blue-titans)", "#FFFFFF", "var(--icl-violet)", "var(--icl-orchid)", "var(--team-blue-titans)", "var(--icl-green)", "var(--team-sky)"];
  const w = [0.29, 0.04, 0.13, 0.06, 0.27, 0.08, 0.13];
  if (variant === "streak") {
    let acc = 0; const stops = [];
    c.forEach((col, i) => { const a = acc * 100, b = (acc + w[i % w.length]) * 100; stops.push(col + " " + a + "% " + b + "%"); acc += w[i % w.length]; });
    return <div style={{ width: size, height: width, background: "linear-gradient(180deg," + stops.join(",") + ")", maskImage: "linear-gradient(90deg,transparent,#000 70%,transparent)", WebkitMaskImage: "linear-gradient(90deg,transparent,#000 70%,transparent)", ...style }} />;
  }
  const inner = size / 2 - width; let r = inner; const stops = ["transparent 0 " + inner + "px"];
  c.forEach((col, i) => { const nr = r + width * w[i % w.length]; stops.push(col + " " + r + "px " + nr + "px"); r = nr; });
  stops.push("transparent " + r + "px");
  const m = "linear-gradient(90deg,transparent " + fadeFrom * 100 + "%,#000 " + (fadeFrom * 100 + 14) + "%)";
  return <div style={{ width: size, height: size, background: "radial-gradient(circle at 50% 50%," + stops.join(",") + ")", maskImage: m, WebkitMaskImage: m, pointerEvents: "none", ...style }} />;
}
