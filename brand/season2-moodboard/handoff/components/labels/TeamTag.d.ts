import * as React from "react";
/** Team name + kit swatch. */
export interface TeamTagProps {
  name: string;
  /** Kit colour, e.g. var(--team-blue-titans) */
  color: string;
  size?: number;
  /** Swatch side. Default left */
  side?: "left" | "right";
  /** Pill chip with round swatch */
  pill?: boolean;
  style?: React.CSSProperties;
}
export declare function TeamTag(props: TeamTagProps): JSX.Element;
