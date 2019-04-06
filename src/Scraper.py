#!/usr/bin/env python

import sys
import ConfigParser
import io
import csv
import os

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
      self.filename=config.get('target', 'scrap_file')
      self.delay=config.get('general', 'query_delay')
      self.base_url=config.get('target', 'base_url')

    def load_file(self):
      exists=os.path.isfile(self.filename)
      if exists:
      	with open(self.filename, mode='r') as csv_file:
          csv_reader = csv.DictReader(csv_file)
          
    def scrap_obs(self):
      print("Scraping obs")	
    	
    def store_obs(self):
      print("scraping Obs")
    
    
    	
    def check_end(self):
      print("Cheking end")
    	
      


s=Scrapper()
s.load_file()
