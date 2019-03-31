Investigar si se puede descargar la información de esta página
https://www.tenable.com/plugins/nessus/23847 
en la cual cambiando el numero cambia informacion de una vulnerabilidad analizada por Tenable.


# Evaluacion Inicial
## Robots .txt
La página tenable.com efectivamente tiene un archivo robots.txt con la siguiente informacion relevante:
```User-agent: *
Sitemap: http://www.tenable.com/sitemap.xml
Disallow: /watch/
Disallow: /read/
Disallow: /includes/
Disallow: /misc/
Disallow: /modules/
Disallow: /profiles/
Disallow: /scripts/
Disallow: /themes/
Disallow: /private/
```

Se puede observar que no esta prohibido el directorio `plugins` del cual queremos descargar la información.
Igualmente se puede ver que la politica es para todo tipo de robot con cualquier User-Agent.

## Sitemap.xml
En este archivo se muestran 2 links a 2 paginas de urls del sitio, en total 5274 en estos no se encuentra el link https://www.tenable.com/plugins/nessus/


## Tamaño
La idea del scraping no es buscar en todo el contenido del sitio, solo se quiere descargar los plugins, por lo tanto al buscar en la pagina https://www.tenable.com/plugins/ se observa que el plugin mas reciente es el 123519

Realizando la búsqueda en google con ´site:www.tenable.com/plugins/nessus/´ indicó alrededor de 79300 resultados, lo que nos da una idea que podemos encontra información de alrededor de 100 mil plugins.

Cada pagina de plugin puede contener alrededor de 1kB de información con lo cual estariamos estimando una base de datos de alrededor 100MB, lo cual resulta viable y descargable en un tiempo moderado.

## Tecnologia
Utilizando la funcion builtwith de python se descubrió la siguiente tecnologia:

```{u'cdn': [u'CloudFlare'], u'javascript-frameworks': [u'jQuery'], u'tag-managers': [u'Google Tag Manager'], u'marketing-automation': [u'Marketo'], u'programming-languages': [u'PHP'], u'cms': [u'Drupal']}```

## Propietario
El propietario de la pagina identificadon con whois es:
```Registrant Name: Tenable Network Security
Registrant Organization: Tenable Network Security
Registrant Street: 7021 COLUMBIA GATEWAY DR STE 500
Registrant City: COLUMBIA
Registrant State/Province: MD
Registrant Postal Code: 21046-3369
Registrant Country: US
Registrant Phone: +1.4108720555
Registrant Phone Ext: 
Registrant Fax: 
Registrant Fax Ext: 
Registrant Email: hostmaster@tenablesecurity.com
```

## Aspectos Legales
La información que se quiere descargar se encuentra de manera pública, no requiere registro donde indiquen condiciones de uso explicitas de la información.

La información igualmente se encuentra indexada en Google.

La información es publicada por una compañía por lo tanto ella puede tener los derechos de la misma asi sea publica, por lo tanto la información descargada no puede ser utilizada para fines comerciales, solo académicos. Se utilizará una descarga conservadora que sea similar a una descarga de un usuario.












