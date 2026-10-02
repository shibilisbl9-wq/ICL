import * as React from "react";
/**
 * Motion ribbon in team kit colours + one brand stripe.
 * @startingPoint section="Poster devices" subtitle="Motion ribbon" viewport="700x300"
 */
export interface RibbonProps {
  /** arc = bat swing / bowling arc, streak = straight run. Default arc */
  variant?: "arc" | "streak";
  /** Stripe colours outer→inner; team kit + one of var(--icl-green) / var(--icl-orchid) */
  colors?: string[];
  /** Arc diameter or streak length in px */
  size?: number;
  /** Band thickness in px */
  width?: number;
  /** Arc fade start (0–1 across). Default 0.38 */
  fadeFrom?: number;
  style?: React.CSSProperties;
}
export declare function Ribbon(props: RibbonProps): JSX.Element;
