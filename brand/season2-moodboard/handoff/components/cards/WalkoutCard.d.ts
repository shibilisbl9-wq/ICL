import * as React from "react";
/**
 * Walkout-song player card for UI collages.
 * @startingPoint section="Poster devices" subtitle="Walkout-song UI card" viewport="700x260"
 */
export interface WalkoutCardProps {
  title?: string;
  artist?: string;
  cover?: string;
  /** 0–1 */
  progress?: number;
  elapsed?: string;
  remaining?: string;
  /** 1 = 540px wide on the 1080 canvas */
  scale?: number;
  style?: React.CSSProperties;
}
export declare function WalkoutCard(props: WalkoutCardProps): JSX.Element;
