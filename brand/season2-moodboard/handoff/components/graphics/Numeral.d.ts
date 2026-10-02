import * as React from "react";
/**
 * Oversized number (days to go, jersey, season) — place behind PlayerCutout.
 * @startingPoint section="Poster devices" subtitle="Giant numeral" viewport="700x320"
 */
export interface NumeralProps {
  children: React.ReactNode;
  /** px on the 1080 canvas; ≈65% of poster height. Default 860 */
  size?: number;
  /** Default var(--accent-hit) */
  color?: string;
  style?: React.CSSProperties;
}
export declare function Numeral(props: NumeralProps): JSX.Element;
