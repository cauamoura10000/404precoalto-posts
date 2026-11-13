# Identidade visual — 404 Preço Alto

Referência viva: `gerador/carrossel_quem_somos.py` (gera o carrossel "Quem somos"). Copie a base de CSS dele.

- **Estilo:** liquid glass. Painéis de vidro fosco (`backdrop-filter: blur(26px) saturate(170%)`, borda branca 24% de opacidade, brilho interno no topo, sombra funda) por cima de formas SÓLIDAS (números "404" gigantes e círculos) que aparecem desfocadas através do vidro.
- **Sem cara de IA:** fundo preto chapado com granulado (feTurbulence, opacidade ~0.13, overlay). Nada de degradê roxo/azul, nada de emoji nas artes, nada de texto em cima de forma colorida fora do vidro.
- **Cores:** verde `#3DF58A` (marca), laranja `#FF8A3D` (detalhe), fundo `#07090C`, texto `#EEF2F5`.
- **Fontes** (via `npm pack @fontsource/space-grotesk @fontsource/inter @fontsource/jetbrains-mono`, embutidas em base64): Space Grotesk 700 nos títulos, Inter nos textos, JetBrains Mono nos rótulos, contadores e @.
- **Moldura de toda arte:** topo `404 PREÇO ALTO` (esq.) e contador `01 / 05` (dir.) em mono; rodapé `@404precoalto` (esq.) e chamada curta (dir.).
- **Formatos:** feed/carrossel 1080×1350 (JPEG); stories 1080×1920 (JPEG); Reels 1080×1920 MP4, 6–15 s.
- **Render:** `google-chrome --headless=new --no-sandbox --hide-scrollbars --window-size=W,H --virtual-time-budget=2000 --screenshot=...`, depois converter para JPEG com Pillow (quality 92+). Sempre conferir a imagem antes de usar: texto legível, nada encostando nas formas coloridas.
- **Pastas:** `posts/AAAA-MM-DD-slug/` com as imagens; links públicos em `https://raw.githubusercontent.com/cauamoura10000/404precoalto-posts/main/<caminho>`.
