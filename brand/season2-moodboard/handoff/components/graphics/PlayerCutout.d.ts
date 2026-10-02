import * as React from "react";
/** Player cutout with contact shadow; placeholder when no src. */
export interface PlayerCutoutProps {
  src?: string;
  alt?: string;
  width?: number;
  height?: number;
  /** Use on dark grounds */
  night?: boolean;
  label?: string;
  style?: React.CSSProperties;
}
export declare function PlayerCutout(props: PlayerCutoutProps): JSX.Element;
