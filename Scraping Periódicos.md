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
