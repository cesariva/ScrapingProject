# CONTENIDO DEL DATASET
Se descargaron todos los datos publicados en la pagina web por cada uno de los plugins.
Una observacion que surgió de analizar las paginas web de diferentes plugins, es que los detalles de cada plugin pueden ser diferentes, por lo tanto el algoritmo de scraping, crea una columna nueva cada vez que encuentra un nuevo detalle del plugin.

Se identificaron 82 campos diferentes en la información descargada, de los cuales en 77 se identificó información valiosa para el análisis de las vulnerabilidades. Debido a la gran cantidad de campos identificados, se propone la siguiente clasificación de los campos para ordenarlos y entenderlos más facilmente.

1. Basica: Información básica de la vulnerabilidad.
1. Severidad: Información relacionada con la severidad de la vulnerabilidad, es decir que tan grave puede ser la vulnerabilidad en terminos de facilidad de explotación y posibles impactos.
1. Tipo vulnerabilidad: Distintos tipo de clasificación de la vulnerabilidad.
1. Componente afectado: Indican cuales son los componentes o tipos de componentes afectados
1. Explotabilidad: estan relacionados con la explotabilidad de la vulnerabilidad, es decir si existen fuentes publicas de como explotar la vulnerabilidad, para aprovecharse de ella.
1. Fechas: Campos relacionados con fechas de la vulnerabilidad o del plugin. 
1. Advisories, bulletins: Campos relacionados con boletines o alertas de seguridad generados por fabricantes, CERTs, o institutos de investigación.
1. Inf. Especifica plugin: Detalles específicos del funcionamiento del plugin.


Los siguientes son los campos identificados.


