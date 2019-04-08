#!/usr/bin/python

import csv

somedict = dict(raymond='red', rachel='blue', matthew='green')
dictnessus= {u'buildId': u'p2AdntJYBx284YSUAvgCl', 
u'query': {u'type': u'nessus', u'id': u'45360'}, 
u'assetPrefix': u'/plugins', 
u'page': u'/plugin', 
u'props': 
	{u'cookies': {}, 
	u'pageProps': {
		u'dependencyIds': [10107], 
		u'errorStatus': False, 								    
		u'type': u'nessus',
		u'plugin': {
			u'cvss_temporal_vector': 
			u'CVSS2#E:H/RL:OF/RC:C', 
			u'cvss_base_score': 7.5, 
			u'exploitability_ease': 
			u'No exploit is required', 
			u'script_name': 
			u'SiteX photo.php albumid Parameter SQL Injection', 
			u'edb-id': 
			u'11881', 
			u'cvss_temporal_score': 6.5, 
			u'cves': [u'CVE-2010-1343'], 
			u'exploited_by_nessus': u'true', 
			u'preferences': [], 
			u'script_version': 
			u'1.13', 
			u'risk_factor': u'High', 
			u'filename': u'sitex_albumid_sqli.nasl', 
			u'vuln_publication_date': u'2010/03/25', 
			u'product': u'nessus', 
			u'xrefs': {
				u'EDB-ID': [u'11881']
				}, 
			u'description': u"The version of SiteX hosted on the remote web server fails to sanitize input to the 'albumid' parameter of the 'photo.php' script before using it in a database query.\n\nProvided PHP's 'magic_quotes_gpc' setting is disabled, an unauthenticated, remote attacker can leverage this issue to manipulate SQL queries and, for example, uncover sensitive information from the associated database, read arbitrary files, or execute arbitrary PHP code.", 
			u'plugin_modification_date': u'2018/07/27', 
			u'dependencies': [u'http_version.nasl'], 
			u'risk_factor_score': 4, 
			u'plugin_publication_date': 
			u'2010/03/26', 
			u'script_copyright': 
			u'This script is Copyright (C) 2010-2018 Tenable Network Security, Inc.', 
			u'cvss_vector': u'CVSS2#AV:N/AC:L/Au:N/C:P/I:P/A:P', 
			u'script_required_ports': [u'Services/www', u'80'], 
			u'script_family': u'CGI abuses', 
			u'bids': [u'38976'], 
			u'solution': u'Unknown at this time.', 
			u'synopsis': u'The remote web server contains a PHP script that is susceptible to a SQL injection attack.', 
			u'exploit_available': u'false', 
			u'script_id': 45360, 
			u'plugin_type': u'remote'}}}}
			
somedict2 = {'nombre':'Cesar','Apellido':'Rodriguez','Rol':'Papa'}
somedict3 = {'Apellido':'Rodriguez','nombre':'Laura','Rol':'Hija'}
somedict4 = {'nombre':'Carmen','Apellido':'Corrales'}

listaDics=[somedict2]
listaDics.append(somedict3)
listaDics.append(somedict4)

fields=set()
for i in listaDics:
	fields=fields.union(set(i.keys()))

with open('mycsvfile.csv','wb') as f:
    w = csv.DictWriter(f,fieldnames=fields)
    w.writeheader()
    w.writerows(listaDics)
    	

# with open('mycsvfile.csv','wb') as f:
#     w = csv.DictWriter(f,fieldnames=dictnessus['props']['pageProps']['plugin'].keys())
#     w.writeheader()
#     w.writerow(dictnessus['props']['pageProps']['plugin'])




