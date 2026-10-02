Social poster canvas (1080 px space) with brand grounds and textures. Lay children out with absolute positioning using the poster tokens (72 side margin, 64 top, 54 grid).

```jsx
<PosterFrame ground="night" texture="halftone" displayWidth={540}>
  <PosterHeader logoSrc="assets/icl-logo-white.png" meta={["SEASON 02","UAE · 2026"]} />
  <Numeral style={{position:"absolute",right:30,top:250}} size={1050}>3</Numeral>
</PosterFrame>
```

- Grounds: white/floodlight (default, most posts), night (countdown, finals), quiet (results, tributes), gradient (UI collages only).
