#!/usr/bin/env python

import sys
import ConfigParser
import io

class Scrapper:
    def __init__(self):	
      print "Inicio Scraper"
      # Load the configuration file in the first argument
      with open(sys.argv[1]) as f:
          configf = f.read()
      config = ConfigParser.RawConfigParser(allow_no_value=True)
      config.readfp(io.BytesIO(configf))
      # Print config contents
      print("Base URL to scraping:")
      print(config.get('target', 'base_url'))
      print("Time to wait between queries")
      print(config.get('general', 'query_delay')+" seconds")
      print("Storage file")
      print(config.get('target', 'scrap_file'))



s=Scrapper()
