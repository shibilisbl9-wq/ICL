import * as React from "react";
/**
 * 1080-wide social poster canvas. Children are absolutely positioned in 1080 px space.
 * @startingPoint section="Posters" subtitle="Blank poster canvas" viewport="700x460"
 */
export interface PosterFrameProps {
  /** white/floodlight = day, night = countdowns/finals, quiet = tributes, gradient = collages */
  ground?: "white" | "floodlight" | "night" | "quiet" | "gradient";
  texture?: "none" | "grid" | "halftone";
  /** feed 1080×1350 (default), story 1080×1920, square 1080×1080 */
  format?: "feed" | "story" | "square";
  /** Rendered width in px; the 1080 canvas is scaled to fit */
  displayWidth?: number;
  children?: React.ReactNode;
  style?: React.CSSProperties;
}
export declare function PosterFrame(props: PosterFrameProps): JSX.Element;
