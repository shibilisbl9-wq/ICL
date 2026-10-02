import * as React from "react";
/** Hand-drawn highlight circle. One per poster. */
export interface HandCircleProps {
  children: React.ReactNode;
  /** Default var(--accent-highlight) */
  color?: string;
  stroke?: number;
  rotate?: number;
  pad?: number;
  style?: React.CSSProperties;
}
export declare function HandCircle(props: HandCircleProps): JSX.Element;
