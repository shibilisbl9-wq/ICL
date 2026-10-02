window.ICL_READY.then(()=>{
const { Numeral, ScriptCaps, TornTape, Ribbon, PlayerCutout, CrosshairRule, HandCircle, TeamTag, StatBlock, WalkoutCard, JerseyTile, PosterFrame, PosterHeader } = window.ICL;
const A = "../../assets/";
const TEAMS = { bt:["Blue Titans","var(--team-blue-titans)"], er:["Enhance Royals","var(--team-enhance-royals)"], fl:["First Legends","var(--team-first-legends)"], dd:["Desert Devils","var(--team-desert-devils)"], bz:["Bizpoint Strikers","var(--team-bizpoint-strikers)"], nk:["Nahda Super Kings","var(--team-nahda-super-kings)"] };
const abs = (o) => ({ position:"absolute", ...o });

function Announcement({ w, d }) {
  return (<PosterFrame ground="white" texture="grid" displayWidth={w}>
    <PosterHeader logoSrc={A+"icl-logo-ink.png"} logoWidth={170} meta={["SEASON 02","UAE · 2026"]}/>
    <Numeral style={abs({left:0,right:0,top:250,textAlign:"center"})}>02</Numeral>
    <PlayerCutout style={abs({left:280,top:300})} width={520} height={880} src={d.cutout}/>
    <div style={abs({left:70,top:790,fontFamily:"var(--font-script)",fontSize:180,lineHeight:1,color:"var(--accent-script-light)",transform:"rotate(-8deg)",whiteSpace:"nowrap"})}>{d.script}</div>
    <div style={abs({left:0,right:0,top:1190,textAlign:"center",fontFamily:"var(--font-display)",fontWeight:900,fontSize:76,lineHeight:1})}>{d.headline}</div>
    <CrosshairRule style={abs({left:72,right:72,top:1282})} items={["DEC 2026","UAE IMAMA","DUBAI"]}/>
  </PosterFrame>);
}
function Countdown({ w, d }) {
  return (<PosterFrame ground="night" texture="halftone" displayWidth={w}>
    <Numeral size={1050} style={abs({right:30,top:250})}>{d.days}</Numeral>
    <PosterHeader logoSrc={A+"icl-logo-white.png"} logoWidth={150} meta={["FIRST BALL","SAT 08:00"]}/>
    <PlayerCutout night style={abs({left:160,top:290})} width={600} height={890} src={d.cutout}/>
    <ScriptCaps style={abs({left:72,top:1000})} caps={"DAYS\nTO GO"} script="Countdown" capsSize={170} scriptSize={150} capsColor="var(--text-on-dark)" scriptColor="var(--accent-script-dark)" offsetX={0.55} offsetY={0.4}/>
    <div style={abs({right:44,bottom:72,writingMode:"vertical-rl",transform:"rotate(180deg)",fontFamily:"var(--font-mono)",fontSize:18,letterSpacing:".2em"})}>SAT · DEC 12 · TOSS SPORTS ACADEMY</div>
  </PosterFrame>);
}
function MatchDay({ w, d }) {
  const a = TEAMS[d.a], b = TEAMS[d.b];
  return (<PosterFrame ground="floodlight" displayWidth={w}>
    <div style={abs({left:0,right:0,top:330,height:790,background:"linear-gradient(100deg,"+a[1]+" 0 50%,"+b[1]+" 50% 100%)",clipPath:"polygon(0 7%,100% 0,100% 93%,0 100%)"})}/>
    <PlayerCutout style={abs({left:30,top:310})} width={520} height={850} label="Captain · Team A"/>
    <PlayerCutout style={abs({left:530,top:310})} width={520} height={850} label="Captain · Team B"/>
    <div style={abs({left:480,top:680,width:120,height:120,borderRadius:"50%",background:"var(--icl-ink)",color:"var(--text-on-dark)",display:"flex",alignItems:"center",justifyContent:"center",fontFamily:"var(--font-display)",fontWeight:900,fontSize:58})}>VS</div>
    <TornTape style={abs({left:70,top:70,width:940})} height={230} fontSize={196}>MATCH DAY</TornTape>
    <div style={abs({left:250,top:130,fontFamily:"var(--font-script)",fontSize:170,lineHeight:1,color:"var(--icl-green)",transform:"rotate(-8deg)",whiteSpace:"nowrap"})}>Match Day</div>
    <div style={abs({left:72,right:72,top:1150,display:"grid",gridTemplateColumns:"minmax(0,1fr) 120px minmax(0,1fr)",alignItems:"center",fontFamily:"var(--font-display)",fontWeight:900,fontSize:80,lineHeight:.88})}>
      <div>{a[0].toUpperCase()}</div><img src={A+"icl-logo-ink.png"} alt="" style={{width:110,justifySelf:"center"}}/><div style={{textAlign:"right"}}>{b[0].toUpperCase()}</div>
    </div>
    <CrosshairRule size={18} style={abs({left:72,right:72,top:1300})} items={["SAT · DEC 12","09:00","GROUND 01"]}/>
  </PosterFrame>);
}
function PlayerOfMatch({ w, d }) {
  return (<PosterFrame ground="floodlight" displayWidth={w} style={{background:"#fff"}}>
    <Ribbon size={1400} width={180} style={abs({left:-220,top:650})}/>
    <PosterHeader logoSrc={A+"icl-logo-ink.png"} logoWidth={140} meta={["PLAYER OF THE MATCH","M07 · BT vs DD"]}/>
    <PlayerCutout style={abs({left:150,top:220})} width={620} height={920} src={d.cutout}/>
    <div style={abs({left:60,top:1040,fontFamily:"var(--font-script)",fontSize:130,lineHeight:1,color:"var(--icl-green)",transform:"rotate(-6deg)",whiteSpace:"nowrap"})}>{d.first}</div>
    <div style={abs({left:72,top:1140,fontFamily:"var(--font-display)",fontWeight:900,fontSize:150,lineHeight:.85})}>{d.last.toUpperCase()}</div>
    <StatBlock style={abs({right:110,top:1120})} align="right" value={d.stat} detail={d.statDetail}/>
  </PosterFrame>);
}
function Walkout({ w, d }) {
  return (<PosterFrame ground="gradient" texture="grid" displayWidth={w}>
    <PosterHeader logoSrc={A+"icl-logo-white.png"} logoWidth={150} meta={["SQUAD 2026","07 / 14"]}/>
    <JerseyTile style={abs({left:130,top:250})} number="07"/>
    <div style={abs({left:470,top:330,width:480,height:700,border:"3px dashed rgba(242,241,236,.6)",borderRadius:6,display:"flex",alignItems:"center",justifyContent:"center",fontFamily:"var(--font-mono)",fontSize:20,letterSpacing:".14em"})}>ACTION PHOTO</div>
    <PlayerCutout night style={abs({left:240,top:270})} width={600} height={880} src={d.cutout}/>
    <WalkoutCard style={abs({left:90,top:820})} title={d.song} artist={d.artist}/>
    <div style={abs({left:0,right:0,top:1160,textAlign:"center",fontFamily:"var(--font-display)",fontWeight:900,fontSize:104,lineHeight:1})}>{(d.first+" "+d.last).toUpperCase()}</div>
    <div style={abs({left:0,right:0,top:1278,textAlign:"center",fontFamily:"var(--font-mono)",fontSize:20,letterSpacing:".14em"})}>BLUE TITANS · ALL-ROUNDER · RHB</div>
  </PosterFrame>);
}
function Fixtures({ w }) {
  const fx=[["08:00","bz","nk","G1"],["08:00","fl","bt","G2"],["09:30","er","dd","G1"],["09:30","fl","nk","G2"],["11:00","bz","dd","G1"],["11:00","er","bt","G2"]];
  return (<PosterFrame ground="white" displayWidth={w}>
    <PosterHeader logoSrc={A+"icl-logo-ink.png"} logoWidth={140} swap meta={["MATCHDAY 01","SAT · DEC 12 2026"]}/>
    <ScriptCaps style={abs({left:64,top:170})} caps="FIXTURES" script="Group Stage" capsSize={250} scriptSize={150} scriptColor="var(--icl-green)" offsetX={0.5} offsetY={0.55}/>
    <div style={abs({left:72,right:72,top:480,borderBottom:"1px solid var(--icl-line-strong)"})}>
      {fx.map(([t,a,b,g],i)=>(<div key={i} style={{display:"grid",gridTemplateColumns:"100px minmax(0,1fr) 76px minmax(0,1fr) 56px",alignItems:"center",height:92,borderTop:"1px solid var(--icl-line-strong)"}}>
        <span style={{fontFamily:"var(--font-mono)",fontSize:22}}>{t}</span>
        <span style={{justifySelf:"end"}}><TeamTag name={TEAMS[a][0]} color={TEAMS[a][1]} side="right"/></span>
        <span style={{textAlign:"center",fontFamily:"var(--font-script)",fontSize:60,lineHeight:1,color:"var(--icl-violet)"}}>vs</span>
        <TeamTag name={TEAMS[b][0]} color={TEAMS[b][1]}/>
        <span style={{textAlign:"right",fontFamily:"var(--font-mono)",fontSize:18,color:"var(--text-muted)"}}>{g}</span></div>))}
    </div>
    <div style={abs({left:72,right:72,top:1080,display:"flex",justifyContent:"space-between",alignItems:"center"})}>
      <HandCircle stroke={6}><span style={{display:"block",padding:"0 30px",fontFamily:"var(--font-display)",fontWeight:900,fontSize:150,lineHeight:1}}>FINAL</span></HandCircle>
      <div style={{fontFamily:"var(--font-mono)",fontSize:22,lineHeight:1.6,letterSpacing:".12em",textAlign:"right"}}>16:30 · GROUND 01<br/>TOSS SPORTS ACADEMY<br/>AL GARHOUD</div>
    </div>
    <CrosshairRule size={18} style={abs({left:72,right:72,top:1286})} items={["UAE IMAMA","ICL","SEASON 02"]}/>
  </PosterFrame>);
}
function ThankYou({ w }) {
  return (<PosterFrame ground="quiet" displayWidth={w}>
    <div style={abs({left:0,right:0,top:420,textAlign:"center",fontFamily:"var(--font-mono)",fontSize:22,letterSpacing:".2em"})}>ICL · SEASON 02</div>
    <div style={abs({left:0,right:0,top:500,textAlign:"center",fontFamily:"var(--font-script)",fontSize:260,lineHeight:1,whiteSpace:"nowrap"})}>Thank You</div>
    <div style={abs({left:480,top:850,width:120,height:1,background:"var(--text-on-dark)"})}/>
    <div style={abs({left:0,right:0,top:890,textAlign:"center",fontFamily:"var(--font-mono)",fontSize:22,letterSpacing:".14em"})}>TO EVERY PLAYER & FAN</div>
    <img src={A+"icl-logo-white.png"} alt="" style={abs({left:450,top:1180,width:180})}/>
  </PosterFrame>);
}
window.POSTERS = { Announcement, Countdown, MatchDay, PlayerOfMatch, Walkout, Fixtures, ThankYou, TEAMS };
});
