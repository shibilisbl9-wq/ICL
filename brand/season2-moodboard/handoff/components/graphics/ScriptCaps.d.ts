import * as React from "react";
/**
 * Caps headline + crossing script phrase.
 * @startingPoint section="Poster devices" subtitle="Script over caps headline" viewport="700x260"
 */
export interface ScriptCapsProps {
  /** Caps headline; use \n for line breaks */
  caps: string;
  /** Script phrase crossing the caps (one per poster) */
  script?: string;
  capsSize?: number;
  /** Default ≈ 0.95 × capsSize */
  scriptSize?: number;
  /** var(--accent-script-light) on light grounds, var(--accent-script-dark) or var(--accent-hit) on dark */
  scriptColor?: string;
  capsColor?: string;
  align?: "left" | "center" | "right";
  /** Script anchor as fraction of the caps box. Defaults 0.3 / 0.35 */
  offsetX?: number;
  offsetY?: number;
  /** Degrees. Default -8 */
  angle?: number;
  style?: React.CSSProperties;
}
export declare function ScriptCaps(props: ScriptCapsProps): JSX.Element;
