#!/usr/bin/env python

import sys
import ConfigParser
import io
import csv
import os
#Para realizar las consultas HTTP
#import requests
#Para realizar el parsing del HTML
#from bs4 import BeautifulSoup
#Para interpretar el json
import json
import time

class Scrapper:
    def __init__(self):	
      print "Inicio Scraper"
      # Load the configuration file in the first argument
      with open(sys.argv[1]) as f:
          configf = f.read()
      config = ConfigParser.RawConfigParser(allow_no_value=True)
      config.readfp(io.BytesIO(configf))
      # Print config contents
      self.filename=config.get('target', 'scrap_file')
      self.tdelay=config.get('general', 'query_delay')
      self.base_url=config.get('target', 'base_url')
      self.initial=int(config.get('target', 'initial_plugin'))
      self.final=int(config.get('target', 'final_plugin'))
      print("Base URL to scraping:"+self.base_url)
      print("Time to wait between queries:"+self.tdelay+" seconds")
      print("Storage file"+self.filename)
      print("Plugins del "+str(self.initial)+" hasta el "+str(self.final))
      self.counter=self.initial

    def load_file(self):
      exists=os.path.isfile(self.filename)
      if exists:
      	with open(self.filename, mode='r') as csv_file:
          csv_reader = csv.DictReader(csv_file)
        csv_file.close()
          
    def scrap_obs(self):
      print("Scraping obs"+str(self.counter))
      
    	
    def store_obs(self):
      print("storing Obs")
    
     	
    def check_end(self):
      print("Cheking end")
      if self.final>self.counter:
        self.counter+=1
        return True
      return False

    def ex_delay(self):
      print("Delay") 	
      time.sleep(float(self.tdelay))


s=Scrapper()
s.load_file()
while s.check_end():
   s.scrap_obs()
   s.store_obs()
   s.ex_delay()
   

