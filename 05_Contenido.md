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
## Basica
* description:Descripción de la vulnerabilidad.
* script_id:Identificador Principal del Plugin. Se pude considerar el indice principal de este dataset..
* script_name:Nombre del Plugin.
* solution:Solucion recomendad por Tenable para solucionar la vulnerabilidad..
* synopsis:Resumen de la vulnerabilidad.

## Severidad
* cvss_base_score:Score de la severidad de la vulnerabilidad de 0 a 10, Este es el score Base, que incluye la facilidad de explotación y el impacto a la informacion. https://www.first.org/cvss/.
* cvss_score_rationale:Justificación de la calificacion realizada a taves de los citerios del estandar CVSS..
* cvss_score_source:Fuente dde donde se tomo el score CVSS..
* cvss_temporal_score:Score de la severidad de la vulnerabilidad de 0 a 10, Este es el score Temporal, que incluye la relavancia actual de la vulnerabilidad https://www.first.org/cvss/.
* cvss_temporal_vector:Vector reducido de los criterios utilizados para calcular el score temporal.
* cvss_vector:Vector reducido de los criterios utilizados para calcular el score base.
* cvss3_base_score:Score de la severidad de la vulnerabilidad de 0 a 10, Este es el score Base, que incluye la facilidad de explotación y el impacto a la informacion, este score utiliza los criterios de la version 3 del estandar. https://www.first.org/cvss/.
* cvss3_temporal_score:Score de la severidad de la vulnerabilidad de 0 a 10, Este es el score Temporal en la versión 3, que incluye la relavancia actual de la vulnerabilidad https://www.first.org/cvss/.
* cvss3_temporal_vector:Vector reducido de los criterios utilizados para calcular el score temporal en la version 3..
* cvss3_vector:Vector reducido de los criterios utilizados para calcular el score  base en la version 3..
"* risk_factor:Clasificación del factor de riesgo de la vulnerabilidad, puede ser:
Critical, High, Medium, Low o Info."
* risk_factor_score:Clasificación del factor de riesgo de la vulnerabilidad de 1 a 5.
* stig_severity:Categorias utilizadas por el DoD US, para clasificar la severidad de las vulenrabilidades. DISA Severity Level I II o II, donde la catagoria I son las más severas. Cada categoria tiene asociado un nivel de cumplimiento..

## Tipo vulnerabilidad
* cwe:Clasificación de la vulnerabilidad de acuerdo al CWE (https://cwe.mitre.org/).
* default_account:Detalla si la vulnerabilidad esta relacionada con una cuenta por defecto del componente..
* unsupported_by_vendor:Detalla si la vulnerabilidad esta relacionada con la falta de soporte por el fabricante..
* compliance:Si el plugin verifica algun tipo de compliance, Es decir cumplimiento de algun estandar o normativa..

## Componente afectado
* agent:Si la vulnerabilidad se identifica a traves de un agente corriendo en Linux, Mac OS o Windows..
* cpe:Identificadores del Common Platform Enumeration, los cuales identifican los componentes tecnológicos afectados por las vulenrabilidades. https://cpe.mitre.org/.
* script_family:Clasificación del plugin definida por el fabricante, dependiendo del tipo de prueba y el componente a probar..

## Explotabilidad
* canvas_package:Si existe un paquete de Canvas un software de explotacion de vulnerabilidaes para verificar la vulnerabilidad. http://www.immunityinc.com/products/canvas/.
* d2_elliot_name:Nombre del modulo de d2 elliot para explotar la vulnerabilidaad..
* edb-id:Identificador de Exploit DB, si existe un E-DB para explotar la vulnerablidad..
* exploit_available:Exploit publico disponible.
* exploit_framework_canvas:Si existe un modulo de canvas para explotar la vulnerabilidad..
* exploit_framework_core:Si existe un modulo de CORE impact para explotar la vulnerabilidad..
* exploit_framework_d2_elliot:Si existe un modulo de d2 elliot para explotar la vulnerabilidad..
* exploit_framework_metasploit:Si existe un modulo de metasploit para explotar la vulnerabilidad..
* exploitability_ease:Facilidad de explotacion de la vulnerabilidad.
* exploited_by_malware:Si la vulnerabilidad es explotable por malware.
* exploited_by_nessus:Si la vulnerabilidad es explotable por Nessis`+.
* metasploit_name:Nombre del modulo de metasploit que puede ser utilizado para explotar la vulnerabilidad..

## Fechas
* patch_publication_date:Fecha de publicación del parche que soluciona la vulnerabilidad.
* plugin_modification_date:Fecha de modificación del plugin de Nessus que identifica la vulnerabilidad..
* plugin_publication_date:Fecha de publicación del plugin de Nessus que identifica la vulnerabilidad..
* vuln_publication_date:Fecha de publcación de la vulnerabilidad..

## Advisories, bulletins
* alas:Amazon Linux AMI Security Advisories, referencia de boletin de seguridad de Amazon, de la pagina https://alas.aws.amazon.com/.
* apple-sa:Apple security advisor, identificador del boletin de se guridad de Apple.
* bids:Identificador de la vulnerabilidades en https://www.securityfocus.com/bid.
* cert:Boletin de seguridad del US-Cert perteneciente a homelan security. https://twitter.com/USCERT_gov.
* cisco-bug-id:Identificador de bug de cisco.
* cisco-sa:Identificador de Security Advisor de Cisco.
* cves:Identificadores del CVE common vulnerability exposure, la principal base de datos de vulenrabilidades a nivel mundial. https://cve.mitre.org/.
* dsa:Identificador de Debian Security Advisories.
* fedora:Identificador de actualización de Fedora, (Fedora Update Notification).
* freebsd:FreeBSD security Advisor. https://www.freebsd.org/security/advisories/.
* glsa:Identificador de Gentoo Linux Security Advisories https://security.gentoo.org/glsa.
* hp:Identificador de boletin de seguridad de HP. https://support.hpe.com/portal/site/hpsc/public/kb/secBullArchive.
* iava:identificador information assurance vulnerability alert (IAVA) del DoDCert.
* iavb:identificador information assurance vulnerability bulletin (IAVB) del DoDCert.
* icsa:ICS-cert Advisories. https://ics-cert.us-cert.gov/advisories.
* in_the_news:Indica si la vulnerabilidad ha aparecido en las noticias..
* jsa:Juniper Network Security Advisories. https://kb.juniper.net/InfoCenter/index?page=content&channel=SECURITY_ADVISORIES.
* mcafee-sb:McAfee Securty bulletin. https://support.mcafee.com/.
* mfsa:Mozilla foundation security advisories.https://www.mozilla.org/en-US/security/advisories/.
* msft:Boletin técnico de Microsoft.
* mskb:Base de conocimiento de Microsoft.
* rhsa:Red hat Security Advisories. https://access.redhat.com/security/security-updates/#/security-advisories.
* see_also:Otras referencias web que pueden complementar la información de la vulenrabilidad..
* ssa:Slackware security advisories. http://www.slackware.com/security/.
* tra:Tenable Research Advisories. https://tenable.com/security/research.
* usn:Ubuntu security notices. https://usn.ubuntu.com/.
* vmsa:Vmware security advisories. https://www.vmware.com/il/security/advisories.html.
* xrefs:Otras referencias externas sobre la vulnerabilidad..
* zdi:Zero day initiative, security advisories. https://www.zerodayinitiative.com/advisories/published/.

## Inf. Especifica plugin
* dependencies:Otros plugins necesarios para poder ejecutar este plugin.
* filename:Nombre de archivo del plugin.
* plugin_type:Tipo de plugin utilizado para identificar la vulnerabilidad. 
** Local es un plugin que debio correr de manera local en el componente evaluado. 
** Remote es un plugin que pudo identificar la vulnerabilida desde la red. 
** Combined que necesita ambas pruebas tanto locales como de red.
** Summary da información de la prueba no necesariamente una vulnerabilidad..
* potential_vulnerability:La vulnerabilidad identificada es potencial, es decir no se tiene una certeza absoluta de que la vulnerabilidad este presente, puede tratarse de un falso positivo..
* script_copyright:Derechos de autor de cada plugin.
* script_required_ports:Puertos de red necesarios por el plugin para realizar su prueba.
* script_required_udp_ports:Puertos de red udp necesarios por el plugin para realizar su prueba.
* script_version:Version del plugin.
