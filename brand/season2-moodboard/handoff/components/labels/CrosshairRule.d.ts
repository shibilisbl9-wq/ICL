import * as React from "react";
/** Footer crosshair strip. */
export interface CrosshairRuleProps {
  items: string[];
  color?: string;
  /** Font size px. Default 20 */
  size?: number;
  style?: React.CSSProperties;
}
export declare function CrosshairRule(props: CrosshairRuleProps): JSX.Element;
