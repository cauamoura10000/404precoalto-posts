"""Posts de 17/11/2026 no estilo CARTAZ: Carrossel "5 ofertas tech da semana" (6 imagens 1080x1350)
e Reels "Como saber se a promoção da Black Friday é real" (4 quadros + MP4).
Uso: python3 gerador/posts_2026_11_17.py  (rodar da raiz do repositório)"""
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
.n{{position:absolute;right:64px;font-family:AN;font-size:300px;line-height:1;color:#111;opacity:.12}}
"""
def band(r): return f'<div class="band"><span>404 PREÇO ALTO</span><span>{r}</span></div>'
def foot(l, b): return f'<div class="foot"><span>{l}</span><b>{b}</b></div>'

# Ofertas listadas no Promobit (categoria informática) na manhã de 17/11/2026, todas no Mercado Livre.
# Só o preço atual vai na arte (preço "de" não conferido).
OFERTAS = [  # (categoria, linha1, linha2, specs, preço)
    ("PLACA DE VÍDEO", "ASRock", "RX 9060 XT", "Radeon · 16GB GDDR6", "R$ 3.744"),
    ("PLACA DE VÍDEO", "Inno3D", "RTX 5060", "Twin X2 · 8GB GDDR7 · 128-bit", "R$ 2.647"),
    ("NOTEBOOK GAMER", "ASUS TUF", "Gaming F16", "RTX 5060 · Core i7<br>16GB RAM · SSD 512GB", "R$ 5.519"),
    ("NOTEBOOK", "ASUS Vivobook", "Go 15", "Ryzen 5 7520U · 8GB RAM<br>SSD 256GB · Tela 15,6\" Full HD", "R$ 2.549"),
    ("MONITOR", "Samsung", "Odyssey G5", "27\" QHD · 180 Hz<br>G-Sync e FreeSync", "R$ 2.929"),
]
CARROSSEL = [f"""{band('17/11')}
<div class="big" style="top:190px;font-size:250px">5 ofertas</div>
<div class="big" style="top:450px;font-size:150px">tech da semana</div>
<div class="red" style="top:740px;height:220px;font-size:96px;line-height:220px">Esquenta Black Friday</div>
<div class="spec" style="top:1060px;font-size:34px">Placa de vídeo, notebook e monitor<br>Link de todas no grupo do Telegram</div>
{foot('Arrasta<br>pro lado', 'LINK NA BIO')}"""]
for i, (cat, l1, l2, spec, preco) in enumerate(OFERTAS, 1):
    CARROSSEL.append(f"""{band(f'OFERTA 0{i} / 05')}
<div class="cat" style="top:190px">{cat}</div>
<div class="big" style="top:300px;font-size:150px">{l1}</div>
<div class="big" style="top:450px;font-size:150px">{l2}</div>
<div class="spec" style="top:620px">{spec}</div>
<div class="por" style="top:800px">POR</div>
<div class="red" style="top:870px;height:240px;font-size:190px;line-height:240px">{preco}</div>
{foot('Visto em 17/11 no Mercado Livre<br>O preço pode mudar', 'LINK NO GRUPO')}""")

REELS = [
f"""{band('BLACK FRIDAY')}
<div class="big" style="top:290px;font-size:190px">Essa</div>
<div class="big" style="top:520px;font-size:190px">promoção</div>
<div class="big" style="top:750px;font-size:190px">é real?</div>
<div class="red" style="top:1150px;height:240px;font-size:120px;line-height:240px">Descobre em 10 s</div>
{foot('Antes de pagar<br>na Black Friday', '404')}""",
f"""{band('DICA 01 / 02')}
<div class="cat" style="top:300px">ANTES DE COMPRAR</div>
<div class="big" style="top:430px;font-size:180px">Olha o</div>
<div class="big" style="top:650px;font-size:180px">histórico</div>
<div class="big" style="top:870px;font-size:180px">de preço</div>
<div class="spec" style="top:1130px">Comparador de preço mostra<br>o gráfico dos últimos meses</div>
<div class="red" style="top:1330px;height:200px;font-size:110px;line-height:200px">Pelo menos 3 meses</div>
{foot('Não só o preço<br>de hoje', '01 / 02')}""",
f"""{band('DICA 02 / 02')}
<div class="cat" style="top:300px">SINAL DE ALERTA</div>
<div class="big" style="top:430px;font-size:170px">Subiu antes</div>
<div class="big" style="top:640px;font-size:170px">pra cair</div>
<div class="big" style="top:850px;font-size:170px">depois?</div>
<div class="spec" style="top:1100px">Se o preço \"de\" só apareceu<br>em novembro, o desconto é falso</div>
<div class="red" style="top:1310px;height:220px;font-size:130px;line-height:220px">Metade do dobro</div>
{foot('O famoso<br>black fraude', '02 / 02')}""",
f"""{band('LINK NO GRUPO')}
<div class="big" style="top:290px;font-size:180px">A gente</div>
<div class="big" style="top:500px;font-size:180px">confere</div>
<div class="big" style="top:710px;font-size:180px">pra você</div>
<div class="red" style="top:980px;height:250px;font-size:104px;line-height:250px">Grupo no Telegram</div>
<div class="spec" style="top:1330px">Ofertas tech todo dia<br>Black Friday é 27/11</div>
{foot('Entra antes<br>da Black Friday', 'LINK NA BIO')}""",
]

def render(html, png, h, fb):
    f = png.with_suffix('.html')
    f.write_text(f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{css(h, fb)}</style></head><body>{html}</body></html>')
    subprocess.run(['google-chrome', '--headless=new', '--no-sandbox', '--hide-scrollbars', '--force-device-scale-factor=1',
                    f'--window-size=1080,{h}', '--virtual-time-budget=2000', f'--screenshot={png}', str(f)], capture_output=True)
    f.unlink()
    img = Image.open(png).convert('RGB'); png.unlink(); return img

C = pathlib.Path('posts/2026-11-17-carrossel-ofertas-da-semana'); C.mkdir(parents=True, exist_ok=True)
for i, b in enumerate(CARROSSEL, 1):
    render(b, C / f'c{i}.png', 1350, 60).save(C / f'404precoalto-ofertas-semana-{i}.jpg', quality=93)
R = pathlib.Path('posts/2026-11-17-reels-promocao-real'); R.mkdir(parents=True, exist_ok=True)
for i, b in enumerate(REELS, 1):
    render(b, R / f'q{i}.png', 1920, 120).save(R / f'reels-quadro-{i}.jpg', quality=93)

# Reels: 4 quadros de 3 s com fade de 0,4 s = 10,8 s
q = [str(R / f'reels-quadro-{i}.jpg') for i in range(1, 5)]
inp = sum([['-loop', '1', '-t', '3', '-i', x] for x in q], [])
fc = '[0][1]xfade=transition=fade:duration=0.4:offset=2.6[a];[a][2]xfade=transition=fade:duration=0.4:offset=5.2[b];' \
     '[b][3]xfade=transition=fade:duration=0.4:offset=7.8,format=yuv420p[v]'
subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', *inp, '-f', 'lavfi', '-t', '10.8', '-i', 'anullsrc=r=44100:cl=stereo',
                '-filter_complex', fc, '-map', '[v]', '-map', '4:a', '-r', '30', '-c:v', 'libx264', '-profile:v', 'high',
                '-crf', '20', '-c:a', 'aac', '-shortest', '-movflags', '+faststart', str(R / '404precoalto-reels-promocao-real.mp4')], check=True)
print('ok')
