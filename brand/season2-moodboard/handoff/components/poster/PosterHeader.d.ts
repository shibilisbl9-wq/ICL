import * as React from "react";
/** Poster header: logo + mono meta. */
export interface PosterHeaderProps {
  /** assets/icl-logo-ink.png on light, assets/icl-logo-white.png on dark */
  logoSrc?: string;
  logoWidth?: number;
  /** Mono lines, e.g. ["SEASON 02","UAE · 2026"] */
  meta?: string[];
  /** Meta left, logo right */
  swap?: boolean;
  top?: number;
  style?: React.CSSProperties;
}
export declare function PosterHeader(props: PosterHeaderProps): JSX.Element;
