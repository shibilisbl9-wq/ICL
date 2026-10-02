// Resolves window.ICL with the design-system components.
// Uses the compiled bundle namespace if present, otherwise transpiles component sources.
(function(){
  var base = document.currentScript.src.replace(/lib\/ds-loader\.js.*$/, '');
  var files = ['graphics/Numeral','graphics/ScriptCaps','graphics/TornTape','graphics/Ribbon','graphics/PlayerCutout','labels/CrosshairRule','labels/RoleBadge','labels/HandCircle','labels/TeamTag','labels/StatBlock','cards/WalkoutCard','cards/JerseyTile','poster/PosterFrame','poster/PosterHeader'];
  function findNs(){ for (var k of Object.keys(window)) { try { var v = window[k]; if (v && typeof v === 'object' && v.PosterFrame && v.Numeral) return v; } catch(e){} } return null; }
  window.ICL_READY = new Promise(function(resolve){
    function go(){
      var ns = findNs(); if (ns) { window.ICL = ns; return resolve(ns); }
      var out = {};
      Promise.all(files.map(function(f){ return fetch(base + 'components/' + f + '.jsx').then(function(r){ return r.text(); }); })).then(function(srcs){
        srcs.forEach(function(src){
          var code = Babel.transform(src.replace(/^export\s+/gm, ''), { presets: ['react'] }).code;
          var names = (src.match(/^export\s+function\s+(\w+)/gm) || []).map(function(m){ return m.split(/\s+/)[2]; });
          var fn = new Function('React', code + '\nreturn {' + names.join(',') + '};');
          Object.assign(out, fn(React));
        });
        window.ICL = out; resolve(out);
      });
    }
    if (window.Babel) go(); else window.addEventListener('DOMContentLoaded', go);
  });
})();
