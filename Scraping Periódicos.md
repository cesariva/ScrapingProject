## Introducción
Para comenzar con el web scraping de esta práctica, elegimos 4 periódicos:
1. "El financiero" (México)
2. "El economista" (México)
3. "La República" (Colombia)
4. "Portafolio" (Colombia)

Realizaremos un análisis de cada periódico para comprobar la viabilidad de realizar el web scraping, primero revisaremos el archivo robots.txt y el mapa de cada sitio web. Después continuaremos con el tamaño y la tecnología del sitio de cada periódico.

## Análisis
### El Financiero

1. Archivo Robots.txt
```
User-agent: *
Disallow: /author/*
Disallow: /page/latest/*
Disallow: /nacional/activan-doble-hoy-no-circula-para-este-miercoles.html
Disallow: /mas/enfoques/inconclusa-remodelacion-del-ste-cedida-a-empresa-publicitaria*
Disallow: /sociedad/empresa-publicitaria-saca-jugo-a-permisos-en-metrobus-y-tren-ligero*
Disallow: /opinion/pgr-revisaria-caso-altavista*
Disallow: /opinion/gobierno-va-por-beneficiados-de-enciclomedia*
Disallow: */whatsapp$
Disallow: */twitter$
Disallow: /index.php*
# Disallow: *.jpg$
# Disallow: *.jpeg$
# Disallow: *.gif$
# Disallow: *.png$

User-agent: Slurp
Crawl-delay: 2

Sitemap: http://www.elfinanciero.com.mx/sitemap.xml
Sitemap: http://www.elfinanciero.com.mx/sitemap-google-news.xml
```
2. Mapa de sitio
Están incluidos en el archivo robots.txt y son http://www.elfinanciero.com.mx/sitemap.xml, y http://www.elfinanciero.com.mx/sitemap-google-news.xml.

### El Economista

1. Archivo Robots.txt
```
User-agent: *
Allow: /
Disallow: /89775457
Sitemap: https://www.eleconomista.com.mx/sitemaps/googlenews.xml
Sitemap: https://www.eleconomista.com.mx/sitemaps/index.xml
Sitemap: https://www.eleconomista.com.mx/sitemaps/daily.xml
Disallow: /arteseideas/Willy-Sousa-artista-o-criminal--20120729-0016.html
Disallow: /politica/Detienen-a-Willy-Sousa-por-fraude-en-Mexico-en-tus-sentidos-20120725-0098.html 
Disallow: /arteseideas/Que-Mexico-en-tus-sentidos-quedo-a-deber-20110303-0106.html 
Disallow: /politica/Dictan-formal-prision-a-productor-de-Mexico-en-tus-sentidos-20120728-0021.html
```

2. Mapa de sitio
Están incluidos en el archivo robots.txt y son https://www.eleconomista.com.mx/sitemaps/googlenews.xml, https://www.eleconomista.com.mx/sitemaps/index.xml y https://www.eleconomista.com.mx/sitemaps/daily.xml

### La República

1. Archivo Robots.txt
```
robots.txt
User-agent: Googlebot
Allow: /
User-agent: Googlebot
Disallow: /vista-previa/
User-agent: Googlebot-News
Allow: /
User-agent: Googlebot-News
Disallow: /vista-previa/
User-agent: *
Allow: /
User-agent: *
Disallow: /vista-previa/

Sitemap: https://www.larepublica.co/sitemapindex
Sitemap: https://www.larepublica.co/sitemapnews
```
2. Mapa de sitio
Están incluidos en el archivo robots.txt y son https://www.larepublica.co/sitemapindex y https://www.larepublica.co/sitemapnews


### Portafolio

1. Archivo Robots.txt
```
Sitemap: http://www.portafolio.co/sitemap-index.xml
Sitemap: http://www.portafolio.co/sitemap-google-news.xml

User-agent: Googlebot
Allow: /
User-agent: Googlebot-News
Allow: /
User-agent: *
Allow: /
User-agent: sitecheck.internetseer.com
Disallow: /
User-agent: Zealbot
Disallow: /
User-agent: MSIECrawler
Disallow: /
User-agent: SiteSnagger
Disallow: /
User-agent: WebStripper
Disallow: /
User-agent: WebCopier
Disallow: /
User-agent: Fetch
Disallow: /
User-agent: Offline Explorer
Disallow: /
User-agent: Teleport
Disallow: /
User-agent: TeleportPro
Disallow: /
User-agent: WebZIP
Disallow: /
User-agent: linko
Disallow: /
User-agent: HTTrack
Disallow: /
User-agent: Microsoft.URL.Control
Disallow: /
User-agent: Xenu
Disallow: /
User-agent: larbin
Disallow: /
User-agent: libwww
Disallow: /
User-agent: ZyBORG
Disallow: /
User-agent: Download Ninja
Disallow: /
User-agent: UbiCrawler
Disallow: /
User-agent: DOC
Disallow: /
User-agent: Zao
Disallow: /
User-agent: Slurp
Disallow: /
User-agent: Maxthon
Disallow: /
User-agent: CNCDialer
Disallow: /
```
2. Mapa de sitio
Están incluidos en el archivo robots.txt y son http://www.portafolio.co/sitemap-index.xml y http://www.portafolio.co/sitemap-google-news.xml
