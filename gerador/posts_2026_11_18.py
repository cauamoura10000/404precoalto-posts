"""Posts de 18/11/2026 no estilo CARTAZ: Reels "Setup gamer até R$ 1.400 só com ofertas" (4 quadros + MP4)
e Stories "Enquete: o que você vai comprar na Black Friday?" (1080x1920).
Uso: python3 gerador/posts_2026_11_18.py  (rodar da raiz do repositório)"""
import base64, subprocess, pathlib
from PIL import Image

F = '/home/claude/fonts/'  # npm pack @fontsource/anton @fontsource/archivo
def ff(name, w, path):
    d = base64.b64encode(open(F + path, 'rb').read()).decode()
    return f"@font-face{{font-family:{name};font-weight:{w};src:url(data:font/woff2;base64,{d})}}"
FONTS = ff('AN', 400, 'fontsource-anton/files/anton-latin-400-normal.woff2') + \
        ff('AR', 500, 'fontsource-archivo/files/archivo-latin-500-normal.woff2') + \
        ff('AR', 800, 'fontsource-archivo/files/archivo-latin-800-normal.woff2')
def css(h, fb):
    return FONTS + f"""
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1080px;height:{h}px;overflow:hidden;position:relative;background:#FFD60A;font-family:AR;color:#111}}
.band{{position:absolute;left:0;right:0;top:0;height:120px;background:#111;color:#FFD60A;display:flex;justify-content:space-between;align-items:center;padding:0 64px;font-family:AN;font-size:46px;letter-spacing:.04em}}
.foot{{position:absolute;left:64px;right:64px;bottom:{fb}px;display:flex;justify-content:space-between;align-items:flex-end;font-weight:800;font-size:30px;line-height:1.25;text-transform:uppercase}}
.foot b{{font-family:AN;font-weight:400;font-size:44px;background:#111;color:#FFD60A;padding:10px 22px;white-space:nowrap}}
.big{{white-space:nowrap;position:absolute;left:64px;font-family:AN;line-height:.95;text-transform:uppercase}}
.red{{position:absolute;left:64px;right:64px;background:#E10600;color:#fff;font-family:AN;text-transform:uppercase;transform:rotate(-2deg);padding-left:36px;white-space:nowrap}}
.cat{{position:absolute;left:64px;background:#111;color:#FFD60A;font-family:AN;font-size:42px;letter-spacing:.05em;padding:8px 22px;transform:rotate(-3deg)}}
.spec{{position:absolute;left:64px;right:64px;font-weight:800;font-size:38px;line-height:1.3;text-transform:uppercase}}
.por{{position:absolute;left:64px;font-family:AN;font-size:52px}}
.box{{position:absolute;left:64px;right:64px;border:6px dashed #111;display:flex;align-items:center;justify-content:center;font-family:AN;font-size:44px;color:#111;opacity:.55;letter-spacing:.04em}}
.item{{position:absolute;left:64px;right:64px;display:flex;justify-content:space-between;align-items:baseline;border-bottom:5px solid #111;padding-bottom:14px}}
.item span{{font-weight:800;font-size:40px;text-transform:uppercase;line-height:1.15}}
.item b{{font-family:AN;font-weight:400;font-size:84px;white-space:nowrap}}
.n{{position:absolute;right:64px;font-family:AN;font-size:300px;line-height:1;color:#111;opacity:.12}}
"""
def band(r): return f'<div class="band"><span>404 PREÇO ALTO</span><span>{r}</span></div>'
def foot(l, b): return f'<div class="foot"><span>{l}</span><b>{b}</b></div>'


# Ofertas vistas no Promobit na manhã de 18/11/2026 (preço atual; sem preço "de").
# Monitor Rise Mode 32" curvo 165Hz R$ 999,00 (Amazon) · Mouse Logitech G203 R$ 85,00 (Amazon)
# Teclado Redragon Karura 2 K502RGB R$ 119,99 (Amazon) · Headset Havit Fuxi-H5D R$ 118,00 (Shopee)
# Total: R$ 1.321,99
REELS = [
f"""{band('SETUP GAMER')}
<div class="big" style="top:290px;font-size:200px">Setup</div>
<div class="big" style="top:530px;font-size:200px">gamer</div>
<div class="big" style="top:770px;font-size:200px">completo</div>
<div class="red" style="top:1130px;height:260px;font-size:170px;line-height:260px">Até R$ 1.400</div>
{foot('Só com ofertas<br>de hoje', '404')}""",
f"""{band('PEÇA 01 / 02')}
<div class="cat" style="top:300px">MONITOR</div>
<div class="big" style="top:430px;font-size:170px">Rise Mode</div>
<div class="big" style="top:630px;font-size:170px">curvo 32"</div>
<div class="spec" style="top:860px">Full HD · 165 Hz · painel VA<br>DisplayPort e HDMI</div>
<div class="por" style="top:1090px">POR</div>
<div class="red" style="top:1170px;height:250px;font-size:190px;line-height:250px">R$ 999</div>
{foot('Visto em 18/11 na Amazon<br>O preço pode mudar', '01 / 02')}""",
f"""{band('PEÇA 02 / 02')}
<div class="cat" style="top:300px">PERIFÉRICOS</div>
<div class="item" style="top:430px"><span>Mouse<br>Logitech G203</span><b>R$ 85</b></div>
<div class="item" style="top:640px"><span>Teclado Redragon<br>Karura 2 RGB</span><b>R$ 119,99</b></div>
<div class="item" style="top:850px"><span>Headset<br>Havit Fuxi-H5D</span><b>R$ 118</b></div>
<div class="red" style="top:1150px;height:220px;font-size:120px;line-height:220px">Os 3 por R$ 322,99</div>
{foot('Mouse e teclado na Amazon<br>headset na Shopee · 18/11', '02 / 02')}""",
f"""{band('LINK NO GRUPO')}
<div class="big" style="top:290px;font-size:180px">Tudo junto</div>
<div class="red" style="top:560px;height:270px;font-size:200px;line-height:270px">R$ 1.321,99</div>
<div class="spec" style="top:930px">Monitor, mouse, teclado e headset<br>Os links estão no grupo do Telegram</div>
<div class="big" style="top:1120px;font-size:120px">Black Friday</div>
<div class="big" style="top:1250px;font-size:120px">é 27/11</div>
{foot('Entra antes<br>da Black Friday', 'LINK NA BIO')}""",
]

STORIES = f"""{band('ENQUETE')}
<div class="big" style="top:230px;font-size:170px">O que você</div>
<div class="big" style="top:420px;font-size:170px">vai comprar</div>
<div class="big" style="top:610px;font-size:170px">na Black</div>
<div class="big" style="top:800px;font-size:170px">Friday?</div>
<div class="spec" style="top:1020px">Vota aí: a gente caça oferta<br>do que ganhar</div>
<div class="box" style="top:1170px;height:300px">ENQUETE AQUI</div>
<div class="red" style="top:1530px;height:150px;font-size:80px;line-height:150px">Ofertas no grupo</div>
{foot('Grupo do Telegram<br>ofertas tech todo dia', 'LINK NA BIO')}"""

def render(html, png, h, fb):
    f = png.with_suffix('.html')
    f.write_text(f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{css(h, fb)}</style></head><body>{html}</body></html>')
    subprocess.run(['google-chrome', '--headless=new', '--no-sandbox', '--hide-scrollbars', '--force-device-scale-factor=1',
                    f'--window-size=1080,{h}', '--virtual-time-budget=2000', f'--screenshot={png}', str(f)], capture_output=True)
    f.unlink()
    img = Image.open(png).convert('RGB'); png.unlink(); return img


R = pathlib.Path('posts/2026-11-18-reels-setup-gamer'); R.mkdir(parents=True, exist_ok=True)
for i, b in enumerate(REELS, 1):
    render(b, R / f'q{i}.png', 1920, 120).save(R / f'reels-quadro-{i}.jpg', quality=93)
S = pathlib.Path('posts/2026-11-18-stories-enquete-black-friday'); S.mkdir(parents=True, exist_ok=True)
render(STORIES, S / 's.png', 1920, 120).save(S / '404precoalto-stories-enquete-bf.jpg', quality=93)

# Reels: 4 quadros de 3 s com fade de 0,4 s = 10,8 s
q = [str(R / f'reels-quadro-{i}.jpg') for i in range(1, 5)]
inp = sum([['-loop', '1', '-t', '3', '-i', x] for x in q], [])
fc = '[0][1]xfade=transition=fade:duration=0.4:offset=2.6[a];[a][2]xfade=transition=fade:duration=0.4:offset=5.2[b];' \
     '[b][3]xfade=transition=fade:duration=0.4:offset=7.8,format=yuv420p[v]'
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', *inp, '-f', 'lavfi', '-t', '10.8', '-i', 'anullsrc=r=44100:cl=stereo',
                '-filter_complex', fc, '-map', '[v]', '-map', '4:a', '-r', '30', '-c:v', 'libx264', '-profile:v', 'high',
                '-crf', '20', '-c:a', 'aac', '-shortest', '-movflags', '+faststart', str(R / '404precoalto-reels-setup-gamer.mp4')], check=True)
print('ok')
