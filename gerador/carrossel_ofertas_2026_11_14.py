"""Carrossel "3 ofertas tech de hoje" (14/11/2026) no estilo CARTAZ (amarelo/preto/vermelho).
Referência do estilo novo. Uso: python3 gerador/carrossel_ofertas_2026_11_14.py <pasta_de_saida>"""
import base64, subprocess, pathlib, sys
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
body{width:1080px;height:1350px;overflow:hidden;position:relative;background:#FFD60A;font-family:AR;color:#111}
.band{position:absolute;left:0;right:0;top:0;height:120px;background:#111;color:#FFD60A;display:flex;justify-content:space-between;align-items:center;padding:0 64px;font-family:AN;font-size:46px;letter-spacing:.04em}
.foot{position:absolute;left:64px;right:64px;bottom:60px;display:flex;justify-content:space-between;align-items:flex-end;font-weight:800;font-size:30px;line-height:1.25;text-transform:uppercase}
.foot b{font-family:AN;font-weight:400;font-size:44px;background:#111;color:#FFD60A;padding:10px 22px;white-space:nowrap}
.big{white-space:nowrap;position:absolute;left:64px;font-family:AN;line-height:.95;text-transform:uppercase}
.red{position:absolute;left:64px;right:64px;background:#E10600;color:#fff;font-family:AN;text-transform:uppercase;transform:rotate(-2deg);padding-left:36px;white-space:nowrap}
.cat{position:absolute;left:64px;top:180px;background:#111;color:#FFD60A;font-family:AN;font-size:40px;letter-spacing:.05em;padding:8px 20px}
.spec{position:absolute;left:64px;right:64px;font-weight:800;font-size:40px;line-height:1.3;text-transform:uppercase}
.por{position:absolute;left:64px;font-family:AN;font-size:56px}
"""
def band(r): return f'<div class="band"><span>404 PREÇO ALTO</span><span>{r}</span></div>'
def foot(l, b): return f'<div class="foot"><span>{l}</span><b>{b}</b></div>'

OFERTAS = [  # (categoria, nome, specs, preço, loja) — preços vistos no Promobit em 14/11/2026
    ("PLACA DE VÍDEO", "RTX 5060<br>8GB", "Inno3D GeForce RTX 5060<br>Twin X2 · GDDR7", "R$ 2.678", "Mercado Livre"),
    ("NOTEBOOK", "ASUS<br>Vivobook Go 15", "Ryzen 5 7520U · 8GB RAM<br>SSD 256GB · Tela 15,6\" Full HD", "R$ 2.449", "Mercado Livre"),
    ("NOTEBOOK", "Vaio<br>FE16", "Ryzen 7 5825U · 16GB RAM<br>SSD 512GB · Tela 16\" IPS", "R$ 3.514", "Mercado Livre"),
]
slides = [f"""{band('14/11')}
<div class="big" style="top:200px;font-size:235px">3 ofertas</div>
<div class="big" style="top:450px;font-size:178px">tech de hoje</div>
<div class="red" style="top:760px;height:240px;font-size:140px;line-height:240px">Preço conferido</div>
{foot('Placa de vídeo e notebooks<br>arrasta pro lado', 'ARRASTA')}"""]
for i, (cat, nome, spec, preco, loja) in enumerate(OFERTAS, 1):
    slides.append(f"""{band(f'OFERTA 0{i} / 03')}
<div class="cat">{cat}</div>
<div class="big" style="top:275px;font-size:158px">{nome}</div>
<div class="spec" style="top:640px">{spec}</div>
<div class="por" style="top:790px">POR</div>
<div class="red" style="top:870px;height:260px;font-size:210px;line-height:260px">{preco}</div>
{foot(f'Visto em 14/11 no {loja}<br>O preço pode mudar', 'LINK NO GRUPO')}""")
slides.append(f"""{band('TODO DIA')}
<div class="big" style="top:190px;font-size:200px">Quer o link<br>dessas<br>ofertas?</div>
<div class="red" style="top:830px;height:240px;font-size:110px;line-height:240px">Grupo no Telegram</div>
{foot('Ofertas de tecnologia todo dia<br>entra antes da Black Friday 27/11', 'LINK NA BIO')}""")

out = pathlib.Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
for n, b in enumerate(slides, 1):
    h = f'/tmp/of{n}.html'
    pathlib.Path(h).write_text(f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body>{b}</body></html>')
    subprocess.run(['google-chrome', '--headless=new', '--no-sandbox', '--hide-scrollbars', '--force-device-scale-factor=1', '--window-size=1080,1350', '--virtual-time-budget=2000', f'--screenshot=/tmp/of{n}.png', h], capture_output=True)
    Image.open(f'/tmp/of{n}.png').convert('RGB').save(out / f'404precoalto-ofertas-{n}.jpg', quality=93)
print('ok')
