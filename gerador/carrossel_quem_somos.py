import base64, subprocess, pathlib
F='/home/claude/fonts/'
def b64(p): return base64.b64encode(open(p,'rb').read()).decode()
fonts=f"""
@font-face{{font-family:SG;font-weight:500;src:url(data:font/woff2;base64,{b64(F+'fontsource-space-grotesk-5.3.0/files/space-grotesk-latin-500-normal.woff2')})}}
@font-face{{font-family:SG;font-weight:700;src:url(data:font/woff2;base64,{b64(F+'fontsource-space-grotesk-5.3.0/files/space-grotesk-latin-700-normal.woff2')})}}
@font-face{{font-family:IN;font-weight:400;src:url(data:font/woff2;base64,{b64(F+'fontsource-inter-5.3.0/files/inter-latin-400-normal.woff2')})}}
@font-face{{font-family:IN;font-weight:500;src:url(data:font/woff2;base64,{b64(F+'fontsource-inter-5.3.0/files/inter-latin-500-normal.woff2')})}}
@font-face{{font-family:JB;font-weight:500;src:url(data:font/woff2;base64,{b64(F+'fontsource-jetbrains-mono-5.3.0/files/jetbrains-mono-latin-500-normal.woff2')})}}
"""
CSS = fonts + """
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1350px;background:#07090C;overflow:hidden;position:relative;font-family:IN;color:#EEF2F5}
.bg404{position:absolute;font-family:SG;font-weight:700;color:#3DF58A;line-height:.8;letter-spacing:-0.06em;white-space:nowrap}
.dot{position:absolute;border-radius:999px}
.grain{position:absolute;inset:0;opacity:.13;mix-blend-mode:overlay;pointer-events:none}
.glass{position:absolute;border-radius:56px;
 background:linear-gradient(140deg,rgba(255,255,255,.16) 0%,rgba(255,255,255,.05) 45%,rgba(255,255,255,.08) 100%);
 backdrop-filter:blur(26px) saturate(170%);-webkit-backdrop-filter:blur(26px) saturate(170%);
 border:1.5px solid rgba(255,255,255,.24);
 box-shadow:inset 0 2px 0 rgba(255,255,255,.5),inset 0 -2px 6px rgba(255,255,255,.06),inset 18px 0 40px -30px rgba(255,255,255,.35),0 40px 80px rgba(0,0,0,.5)}
.top{position:absolute;top:64px;left:72px;right:72px;display:flex;justify-content:space-between;font-family:JB;font-size:24px;letter-spacing:.08em;color:rgba(238,242,245,.75)}
.bot{position:absolute;bottom:60px;left:72px;right:72px;display:flex;justify-content:space-between;align-items:center;font-family:JB;font-size:24px;color:rgba(238,242,245,.75)}
h1{font-family:SG;font-weight:700;letter-spacing:-0.035em;line-height:.95}
.lab{font-family:JB;font-size:24px;letter-spacing:.12em;color:#3DF58A;text-transform:uppercase}
p{font-size:38px;line-height:1.35;color:rgba(238,242,245,.86)}
.pill{display:flex;align-items:center;gap:22px;padding:26px 34px;border-radius:999px;font-family:SG;font-weight:500;font-size:40px;
 background:linear-gradient(140deg,rgba(255,255,255,.14),rgba(255,255,255,.04));backdrop-filter:blur(20px) saturate(170%);
 border:1.5px solid rgba(255,255,255,.22);box-shadow:inset 0 2px 0 rgba(255,255,255,.45),0 20px 40px rgba(0,0,0,.35)}
.pill i{width:14px;height:14px;border-radius:99px;background:#3DF58A;flex:none}
.g{color:#3DF58A}
"""
GRAIN='<svg class="grain" width="1080" height="1350" aria-hidden="true"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="3" stitchTiles="stitch"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>'
def frame(n, body, bot_right='arrasta &rarr;'):
    return f"""<div class="top"><span>404 PREÇO ALTO</span><span>0{n} / 05</span></div>{body}
<div class="bot"><span>@404precoalto</span><span>{bot_right}</span></div>"""

slides={}
slides[1]=f"""
<div class="bg404" style="font-size:760px;left:-60px;top:250px">404</div>
<div class="dot" style="width:150px;height:150px;background:#FF8A3D;right:120px;top:190px"></div>
<div class="glass" style="left:72px;right:72px;top:560px;height:640px;padding:72px">
 <div class="lab" style="color:#EEF2F5">prazer,</div>
 <h1 style="font-size:132px;margin-top:28px">Preço alto?<br>Aqui <span class="g">não.</span></h1>
 <p style="margin-top:44px;max-width:780px">Somos o 404 Preço Alto. A gente caça ofertas de tecnologia pra você.</p>
</div>
{frame(1,'')}"""
slides[2]=f"""
<div class="bg404" style="font-size:520px;right:-120px;top:120px">4</div>
<div class="dot" style="width:380px;height:380px;background:#3DF58A;left:-250px;bottom:420px"></div>
<div class="dot" style="width:90px;height:90px;background:#FF8A3D;right:40px;bottom:120px"></div>
<div class="glass" style="left:72px;right:72px;top:250px;bottom:190px;padding:76px;display:flex;flex-direction:column;justify-content:space-between">
 <div><div class="lab">quem somos</div>
 <h1 style="font-size:96px;margin-top:30px">Um canal de ofertas tech feito por quem também monta setup.</h1></div>
 <p>Todo dia a gente garimpa preço em hardware, periféricos e acessórios. Se tá caro, não entra.</p>
</div>
{frame(2,'')}"""
items=["SSD e memória RAM","Placa de vídeo e processador","Mouse, teclado e headset","Monitores e notebooks","Cupons e erros de preço"]
pills="".join(f'<div class="pill"><i></i>{t}</div>' for t in items)
slides[3]=f"""
<div class="bg404" style="font-size:900px;left:560px;top:430px">0</div>
<div class="dot" style="width:120px;height:120px;background:#FF8A3D;right:90px;top:200px"></div>
<div style="position:absolute;left:72px;top:190px"><div class="lab">o que você encontra</div>
<h1 style="font-size:100px;margin-top:26px">Tudo que<br>faz o setup.</h1></div>
<div style="position:absolute;left:72px;right:72px;top:560px;display:flex;flex-direction:column;gap:26px;align-items:flex-start">{pills}</div>
{frame(3,'')}"""
steps=[("01","A gente confere o histórico de preço do produto."),("02","Só posta se o desconto for de verdade."),("03","Você recebe no grupo, várias vezes por dia.")]
rows="".join(f'<div style="display:flex;gap:40px;align-items:baseline;padding:40px 0;border-top:1.5px solid rgba(255,255,255,.16)"><span style="font-family:JB;font-size:34px;color:#3DF58A">{a}</span><p style="font-size:42px;color:#EEF2F5">{b}</p></div>' for a,b in steps)
slides[4]=f"""
<div class="dot" style="width:460px;height:460px;background:#3DF58A;right:-250px;top:150px"></div>
<div class="dot" style="width:170px;height:170px;background:#FF8A3D;left:10px;bottom:150px"></div>
<div class="glass" style="left:72px;right:72px;top:210px;bottom:190px;padding:76px">
 <div class="lab">como funciona</div>
 <h1 style="font-size:96px;margin:30px 0 40px">Sem enrolação.</h1>
 {rows}
</div>
{frame(4,'')}"""
slides[5]=f"""
<div class="bg404" style="font-size:600px;left:50%;transform:translateX(-50%);top:160px">404</div>
<div class="dot" style="width:170px;height:170px;background:#FF8A3D;right:110px;top:500px"></div>
<div class="glass" style="left:72px;right:72px;top:600px;height:560px;padding:72px">
 <div class="lab">black friday · 27/11</div>
 <h1 style="font-size:104px;margin-top:28px">Entra no grupo antes que o preço suba.</h1>
 <div style="margin-top:48px;display:inline-flex;align-items:center;gap:18px;padding:24px 40px;border-radius:999px;background:#3DF58A;color:#07090C;font-family:SG;font-weight:700;font-size:40px">Link na bio</div>
</div>
{frame(5,'','salva e compartilha')}"""
for n,b in slides.items():
    html=f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{b}{GRAIN}</body></html>'
    pathlib.Path(f'slide{n}.html').write_text(html)
    subprocess.run(['google-chrome','--headless=new','--no-sandbox','--hide-scrollbars','--force-device-scale-factor=1','--window-size=1080,1350','--virtual-time-budget=2000',f'--screenshot=s{n}.png',f'slide{n}.html'],capture_output=True)
    from PIL import Image
    Image.open(f's{n}.png').convert('RGB').save(f'404precoalto-quem-somos-{n}.jpg',quality=93)
print('ok')
