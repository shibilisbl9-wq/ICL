import * as React from "react";
/** Jersey-number tile for collages. */
export interface JerseyTileProps {
  number?: string;
  size?: number;
  color?: string;
  textColor?: string;
  style?: React.CSSProperties;
}
export declare function JerseyTile(props: JerseyTileProps): JSX.Element;
