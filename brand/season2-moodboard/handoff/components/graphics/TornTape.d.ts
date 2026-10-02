import * as React from "react";
/** Torn violet tape — Season 1 device carried into Season 2. */
export interface TornTapeProps {
  children: React.ReactNode;
  /** Default var(--accent-tape) */
  color?: string;
  textColor?: string;
  /** Degrees, −3 to −6. Default -3 */
  rotate?: number;
  height?: number;
  fontSize?: number;
  /** Mono label style (repeating strip) instead of display headline */
  mono?: boolean;
  style?: React.CSSProperties;
}
export declare function TornTape(props: TornTapeProps): JSX.Element;
