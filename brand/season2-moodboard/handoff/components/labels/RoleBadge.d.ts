import * as React from "react";
/** Player role circle. */
export interface RoleBadgeProps {
  role?: "BAT" | "BWL" | "AR" | "WK" | "C" | "VC";
  size?: number;
  /** Violet highlight for the featured role */
  active?: boolean;
  dark?: boolean;
  style?: React.CSSProperties;
}
export declare function RoleBadge(props: RoleBadgeProps): JSX.Element;
