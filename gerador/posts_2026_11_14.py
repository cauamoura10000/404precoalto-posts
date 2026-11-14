"""Gera os posts de 14/11/2026: post fixado (feed), quadros do Reels e stories.
Base de estilo: gerador/carrossel_quem_somos.py. Rodar de dentro da pasta de saída."""
import base64, subprocess, pathlib, sys
from PIL import Image

F = '/home/claude/fonts/'
def b64(p): return base64.b64encode(open(p, 'rb').read()).decode()
fonts = f"""
@font-face{{font-family:SG;font-weight:500;src:url(data:font/woff2;base64,{b64(F+'fontsource-space-grotesk-5.3.0/files/space-grotesk-latin-500-normal.woff2')})}}
@font-face{{font-family:SG;font-weight:700;src:url(data:font/woff2;base64,{b64(F+'fontsource-space-grotesk-5.3.0/files/space-grotesk-latin-700-normal.woff2')})}}
@font-face{{font-family:IN;font-weight:400;src:url(data:font/woff2;base64,{b64(F+'fontsource-inter-5.3.0/files/inter-latin-400-normal.woff2')})}}
@font-face{{font-family:IN;font-weight:500;src:url(data:font/woff2;base64,{b64(F+'fontsource-inter-5.3.0/files/inter-latin-500-normal.woff2')})}}
@font-face{{font-family:JB;font-weight:500;src:url(data:font/woff2;base64,{b64(F+'fontsource-jetbrains-mono-5.3.0/files/jetbrains-mono-latin-500-normal.woff2')})}}
"""
def css(w, h, top=64, bot=60):
    return fonts + f"""
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:{w}px;height:{h}px;background:#07090C;overflow:hidden;position:relative;font-family:IN;color:#EEF2F5}}
.top{{position:absolute;top:{top}px;left:72px;right:72px;display:flex;justify-content:space-between;font-family:JB;font-size:24px;letter-spacing:.08em;color:rgba(238,242,245,.75)}}
.bot{{position:absolute;bottom:{bot}px;left:72px;right:72px;display:flex;justify-content:space-between;align-items:center;font-family:JB;font-size:24px;color:rgba(238,242,245,.75)}}
""" + """
.bg404{position:absolute;font-family:SG;font-weight:700;color:#3DF58A;line-height:.8;letter-spacing:-0.06em;white-space:nowrap}
.dot{position:absolute;border-radius:999px}
.grain{position:absolute;inset:0;opacity:.13;mix-blend-mode:overlay;pointer-events:none}
.glass{position:absolute;border-radius:56px;
 background:linear-gradient(140deg,rgba(255,255,255,.16) 0%,rgba(255,255,255,.05) 45%,rgba(255,255,255,.08) 100%);
 backdrop-filter:blur(26px) saturate(170%);-webkit-backdrop-filter:blur(26px) saturate(170%);
 border:1.5px solid rgba(255,255,255,.24);
 box-shadow:inset 0 2px 0 rgba(255,255,255,.5),inset 0 -2px 6px rgba(255,255,255,.06),inset 18px 0 40px -30px rgba(255,255,255,.35),0 40px 80px rgba(0,0,0,.5)}
h1{font-family:SG;font-weight:700;letter-spacing:-0.035em;line-height:.95}
.lab{font-family:JB;font-size:24px;letter-spacing:.12em;color:#3DF58A;text-transform:uppercase}
p{font-size:38px;line-height:1.35;color:rgba(238,242,245,.86)}
.g{color:#3DF58A}
.cta{display:inline-flex;align-items:center;gap:18px;padding:24px 40px;border-radius:999px;background:#3DF58A;color:#07090C;font-family:SG;font-weight:700;font-size:40px}
.row{display:flex;gap:30px;align-items:baseline;padding:22px 0;border-top:1.5px solid rgba(255,255,255,.16)}
.row span{font-family:JB;font-size:30px;color:#3DF58A;flex:none}
.row p{font-size:32px;color:#EEF2F5}
"""
def grain(w, h):
    return f'<svg class="grain" width="{w}" height="{h}" aria-hidden="true"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="3" stitchTiles="stitch"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>'

def render(name, body, w, h, **kw):
    html = f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{css(w,h,**kw)}</style></head><body>{body}{grain(w,h)}</body></html>'
    pathlib.Path(f'/tmp/{name}.html').write_text(html)
    subprocess.run(['google-chrome', '--headless=new', '--no-sandbox', '--hide-scrollbars', '--force-device-scale-factor=1',
                    f'--window-size={w},{h}', '--virtual-time-budget=2000', f'--screenshot=/tmp/{name}.png', f'/tmp/{name}.html'], capture_output=True)
    Image.open(f'/tmp/{name}.png').convert('RGB').save(f'{name}.jpg', quality=93)

out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
import os; os.chdir(out)

# ---------- POST FIXADO 1080x1350 ----------
regras = [("01", "Só tecnologia: hardware e periféricos."),
          ("02", "Preço conferido no histórico."),
          ("03", "Sem spam e sem corrente: só oferta."),
          ("04", "Confira o preço na loja antes de pagar.")]
rows = "".join(f'<div class="row"><span>{a}</span><p>{b}</p></div>' for a, b in regras)
fix = f"""
<div class="bg404" style="font-size:480px;right:-70px;top:110px">404</div>
<div class="dot" style="width:130px;height:130px;background:#FF8A3D;left:80px;top:150px"></div>
<div class="dot" style="width:260px;height:260px;background:#3DF58A;left:-160px;bottom:220px"></div>
<div class="top"><span>404 PREÇO ALTO</span><span>FIXADO</span></div>
<div class="glass" style="left:72px;right:72px;top:330px;bottom:150px;padding:60px 64px">
 <div class="lab" style="color:#EEF2F5">ofertas tech todo dia</div>
 <h1 style="font-size:84px;margin-top:22px">Preço alto?<br>Aqui <span class="g">não.</span></h1>
 <p style="margin-top:24px;font-size:34px">Entra no grupo pelo link na bio e recebe as ofertas na hora.</p>
 <div class="lab" style="margin:40px 0 4px">regras do grupo</div>
 {rows}
</div>
<div class="bot"><span>@404precoalto</span><span>link na bio</span></div>"""
render('404precoalto-fixado', fix, 1080, 1350)

# ---------- REELS: 4 quadros 1080x1920 ----------
T, B = 150, 170   # margens de segurança da interface do Reels
def rf(n, body, right='@404precoalto'):
    return f'<div class="top"><span>404 PREÇO ALTO</span><span>0{n} / 04</span></div>{body}<div class="bot"><span>@404precoalto</span><span>{right}</span></div>'
q = {}
q[1] = rf(1, """
<div class="bg404" style="font-size:900px;left:-120px;top:290px">4</div>
<div class="dot" style="width:200px;height:200px;background:#FF8A3D;right:110px;top:330px"></div>
<div class="glass" style="left:72px;right:72px;top:760px;height:560px;padding:80px;display:flex;flex-direction:column;justify-content:center">
 <div class="lab" style="color:#EEF2F5">você procurou</div>
 <h1 style="font-size:170px;margin-top:30px">Preço<br>alto?</h1>
</div>""", '')
q[2] = rf(2, """
<div class="bg404" style="font-size:560px;left:50%;transform:translateX(-50%);top:330px">404</div>
<div class="dot" style="width:140px;height:140px;background:#FF8A3D;left:100px;bottom:420px"></div>
<div class="glass" style="left:72px;right:72px;top:640px;height:640px;padding:80px;display:flex;flex-direction:column;justify-content:center">
 <div class="lab">erro 404</div>
 <h1 style="font-size:150px;margin-top:30px">Não<br>encontrado<br><span class="g">aqui.</span></h1>
</div>""", '')
q[3] = rf(3, """
<div class="dot" style="width:520px;height:520px;background:#3DF58A;right:-260px;top:420px"></div>
<div class="dot" style="width:180px;height:180px;background:#FF8A3D;left:40px;bottom:380px"></div>
<div class="glass" style="left:72px;right:72px;top:560px;height:800px;padding:80px;display:flex;flex-direction:column;justify-content:center">
 <div class="lab">o que a gente faz</div>
 <h1 style="font-size:104px;margin-top:30px">Ofertas de tecnologia, todo dia.</h1>
 <p style="margin-top:44px;font-size:46px">A gente confere o histórico de preço antes de postar.</p>
</div>""", '')
q[4] = rf(4, """
<div class="bg404" style="font-size:600px;left:50%;transform:translateX(-50%);top:300px">404</div>
<div class="dot" style="width:170px;height:170px;background:#FF8A3D;right:110px;top:700px"></div>
<div class="glass" style="left:72px;right:72px;top:820px;height:620px;padding:80px;display:flex;flex-direction:column;justify-content:center">
 <div class="lab">black friday · 27/11</div>
 <h1 style="font-size:112px;margin-top:30px">Entra no grupo antes que o preço suba.</h1>
 <div style="margin-top:50px"><div class="cta" style="font-size:46px">Link na bio</div></div>
</div>""", 'segue o perfil')
for n, b in q.items():
    render(f'reels-quadro-{n}', b, 1080, 1920, top=T, bot=B)

# ---------- STORIES 1080x1920 ----------
st = """
<div class="top"><span>404 PREÇO ALTO</span><span>STORIES</span></div>
<div class="bg404" style="font-size:700px;left:-80px;top:220px">404</div>
<div class="dot" style="width:190px;height:190px;background:#FF8A3D;right:100px;top:300px"></div>
<div class="dot" style="width:380px;height:380px;background:#3DF58A;right:-200px;bottom:330px"></div>
<div class="glass" style="left:72px;right:72px;top:640px;height:820px;padding:80px;display:flex;flex-direction:column;justify-content:space-between">
 <div>
  <div class="lab" style="color:#EEF2F5">pergunta pra você</div>
  <h1 style="font-size:112px;margin-top:30px">Que produto você quer ver em <span class="g">promoção?</span></h1>
  <p style="margin-top:40px;font-size:44px">Responde aqui no direct. A gente caça a oferta.</p>
 </div>
 <div><div class="cta" style="font-size:44px">Grupo: link na bio</div></div>
</div>
<div class="bot"><span>@404precoalto</span><span>responde no direct</span></div>"""
render('404precoalto-stories-caixinha', st, 1080, 1920, top=T, bot=B)
print('ok')
