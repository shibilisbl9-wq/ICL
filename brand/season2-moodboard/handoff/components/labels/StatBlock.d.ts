import * as React from "react";
/** Display stat + mono detail. */
export interface StatBlockProps {
  value: React.ReactNode;
  detail?: string;
  size?: number;
  align?: "left" | "center" | "right";
  color?: string;
  /** Colour for the value only */
  accent?: string;
  style?: React.CSSProperties;
}
export declare function StatBlock(props: StatBlockProps): JSX.Element;
