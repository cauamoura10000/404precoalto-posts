"""Posts de 15/11/2026 no estilo CARTAZ: Reels "Achado do fim de semana" (4 quadros + MP4) e Stories "PC ou console?".
Uso: python3 gerador/posts_2026_11_15.py  (rodar da raiz do repositório)"""
import base64, subprocess, pathlib
from PIL import Image

F = '/home/claude/fonts/'  # npm pack @fontsource/anton @fontsource/archivo
def ff(name, w, path):
    d = base64.b64encode(open(F + path, 'rb').read()).decode()
    return f"@font-face{{font-family:{name};font-weight:{w};src:url(data:font/woff2;base64,{d})}}"
FONTS = ff('AN', 400, 'fontsource-anton/files/anton-latin-400-normal.woff2') + \
        ff('AR', 500, 'fontsource-archivo/files/archivo-latin-500-normal.woff2') + \
        ff('AR', 800, 'fontsource-archivo/files/archivo-latin-800-normal.woff2')
CSS = FONTS + """
*{box-sizing:border-box;margin:0;padding:0}
body{width:1080px;height:1920px;overflow:hidden;position:relative;background:#FFD60A;font-family:AR;color:#111}
.band{position:absolute;left:0;right:0;top:0;height:120px;background:#111;color:#FFD60A;display:flex;justify-content:space-between;align-items:center;padding:0 64px;font-family:AN;font-size:46px;letter-spacing:.04em}
.foot{position:absolute;left:64px;right:64px;bottom:120px;display:flex;justify-content:space-between;align-items:flex-end;font-weight:800;font-size:32px;line-height:1.25;text-transform:uppercase}
.foot b{font-family:AN;font-weight:400;font-size:46px;background:#111;color:#FFD60A;padding:10px 22px;white-space:nowrap}
.big{white-space:nowrap;position:absolute;left:64px;font-family:AN;line-height:.95;text-transform:uppercase}
.red{position:absolute;left:64px;right:64px;background:#E10600;color:#fff;font-family:AN;text-transform:uppercase;transform:rotate(-2deg);padding-left:36px;white-space:nowrap}
.cat{position:absolute;left:64px;background:#111;color:#FFD60A;font-family:AN;font-size:44px;letter-spacing:.05em;padding:8px 22px}
.spec{position:absolute;left:64px;right:64px;font-weight:800;font-size:40px;line-height:1.3;text-transform:uppercase}
.box{position:absolute;left:64px;right:64px;border:6px dashed #111;display:flex;align-items:center;justify-content:center;font-family:AN;font-size:44px;color:#111;opacity:.55;letter-spacing:.04em}
.opt{position:absolute;left:64px;right:64px;height:220px;display:flex;align-items:center;font-family:AN;text-transform:uppercase}
"""
def band(r): return f'<div class="band"><span>404 PREÇO ALTO</span><span>{r}</span></div>'
def foot(l, b): return f'<div class="foot"><span>{l}</span><b>{b}</b></div>'

# Oferta vista no Promobit (Top Ofertas) em 15/11/2026, AliExpress. Sem preço "de": não conferido.
REELS = [
f"""{band('ACHADO DO FIM DE SEMANA')}
<div class="big" style="top:330px;font-size:210px">Achado</div>
<div class="big" style="top:550px;font-size:210px">do fim</div>
<div class="big" style="top:770px;font-size:210px">de semana</div>
<div class="red" style="top:1200px;height:250px;font-size:150px;line-height:250px">Preço baixo</div>
{foot('15/11 · oferta tech<br>conferida hoje', '404')}""",
f"""{band('PERIFÉRICO GAMER')}
<div class="cat" style="top:300px;transform:rotate(-3deg)">TECLADO MAGNÉTICO</div>
<div class="big" style="top:420px;font-size:230px">Akko</div>
<div class="big" style="top:640px;font-size:230px">TAC75</div>
<div class="spec" style="top:930px">Layout 75% · Rapid Trigger<br>Polling rate 8K</div>
<div class="red" style="top:1250px;height:220px;font-size:120px;line-height:220px">Switch magnético</div>
{foot('Teclado de nível<br>competitivo', '01 / 03')}""",
f"""{band('QUANTO TÁ?')}
<div class="big" style="top:330px;font-size:120px">Visto hoje por</div>
<div class="red" style="top:560px;height:330px;font-size:260px;line-height:330px">R$ 217</div>
<div class="spec" style="top:1020px">Visto em 15/11 no AliExpress<br>O preço pode mudar</div>
{foot('Confere na loja<br>antes de pagar', '02 / 03')}""",
f"""{band('LINK NO GRUPO')}
<div class="big" style="top:300px;font-size:210px">Quer o</div>
<div class="big" style="top:510px;font-size:210px">link?</div>
<div class="red" style="top:870px;height:250px;font-size:104px;line-height:250px">Grupo no Telegram</div>
<div class="spec" style="top:1230px">Ofertas tech todo dia<br>Black Friday é 27/11</div>
{foot('Entra antes<br>da Black Friday', 'LINK NA BIO')}""",
]
STORIES = f"""{band('ENQUETE')}
<div class="big" style="top:250px;font-size:250px">PC ou</div>
<div class="big" style="top:500px;font-size:250px">console?</div>
<div class="spec" style="top:800px">Vota aí: a gente vai caçar<br>oferta do que ganhar</div>
<div class="box" style="top:1000px;height:360px">ENQUETE AQUI</div>
<div class="red" style="top:1440px;height:170px;font-size:84px;line-height:170px">Ofertas no grupo</div>
{foot('Grupo do Telegram<br>ofertas tech todo dia', 'LINK NA BIO')}"""

def render(html, png):
    h = png.with_suffix('.html')
    h.write_text(f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{html}</body></html>')
    subprocess.run(['google-chrome', '--headless=new', '--no-sandbox', '--hide-scrollbars', '--force-device-scale-factor=1',
                    '--window-size=1080,1920', '--virtual-time-budget=2000', f'--screenshot={png}', str(h)], capture_output=True)
    h.unlink()
    img = Image.open(png).convert('RGB'); png.unlink(); return img

R = pathlib.Path('posts/2026-11-15-reels-achado'); R.mkdir(parents=True, exist_ok=True)
for i, b in enumerate(REELS, 1):
    render(b, R / f'q{i}.png').save(R / f'reels-quadro-{i}.jpg', quality=93)
S = pathlib.Path('posts/2026-11-15-stories-enquete'); S.mkdir(parents=True, exist_ok=True)
render(STORIES, S / 's.png').save(S / '404precoalto-stories-enquete.jpg', quality=93)

# Reels: 4 quadros de 3 s com fade de 0,4 s = 10,8 s
q = [str(R / f'reels-quadro-{i}.jpg') for i in range(1, 5)]
inp = sum([['-loop', '1', '-t', '3', '-i', x] for x in q], [])
fc = '[0][1]xfade=transition=fade:duration=0.4:offset=2.6[a];[a][2]xfade=transition=fade:duration=0.4:offset=5.2[b];' \
     '[b][3]xfade=transition=fade:duration=0.4:offset=7.8,format=yuv420p[v]'
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', *inp, '-f', 'lavfi', '-t', '10.8', '-i', 'anullsrc=r=44100:cl=stereo',
                '-filter_complex', fc, '-map', '[v]', '-map', '4:a', '-r', '30', '-c:v', 'libx264', '-profile:v', 'high',
                '-crf', '20', '-c:a', 'aac', '-shortest', '-movflags', '+faststart', str(R / '404precoalto-reels-achado.mp4')], check=True)
print('ok')
