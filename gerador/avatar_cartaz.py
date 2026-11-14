"""Foto de perfil (Telegram/Instagram) no estilo cartaz. Uso: python3 gerador/avatar_cartaz.py"""
import base64, subprocess, pathlib
from PIL import Image
F='/home/claude/fonts/'
an=base64.b64encode(open(F+'fontsource-anton/files/anton-latin-400-normal.woff2','rb').read()).decode()
html=f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:AN;src:url(data:font/woff2;base64,{an})}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1080px;background:#FFD60A;overflow:hidden;position:relative;font-family:AN;text-transform:uppercase}}
.n{{position:absolute;left:0;right:0;top:170px;text-align:center;font-size:500px;line-height:1;color:#111;letter-spacing:-.01em}}
.r{{position:absolute;left:150px;right:150px;top:660px;height:190px;background:#E10600;color:#fff;font-size:140px;line-height:190px;text-align:center;transform:rotate(-3deg)}}
</style></head><body><div class="n">404</div><div class="r">Preço alto</div></body></html>"""
out=pathlib.Path(__file__).resolve().parent.parent/'marca'
(out/'avatar.html').write_text(html)
subprocess.run(['google-chrome','--headless=new','--no-sandbox','--hide-scrollbars','--force-device-scale-factor=1','--window-size=1080,1080','--virtual-time-budget=2000',f'--screenshot={out}/avatar.png',str(out/'avatar.html')],capture_output=True)
im=Image.open(out/'avatar.png').convert('RGB'); im.save(out/'404precoalto-avatar.jpg',quality=95)
# prévia do recorte redondo
from PIL import ImageDraw
m=Image.new('L',im.size,0); ImageDraw.Draw(m).ellipse((0,0)+im.size,fill=255)
c=Image.new('RGB',im.size,(255,255,255)); c.paste(im,(0,0),m); c.resize((300,300)).save('/tmp/avatar-redondo.png')
(out/'avatar.html').unlink(); (out/'avatar.png').unlink()
print('ok')
