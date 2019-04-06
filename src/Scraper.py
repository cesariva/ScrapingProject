#!/usr/bin/env python

import sys
import ConfigParser
import io
import csv
import os
#Para realizar las consultas HTTP
import requests
#Para realizar el parsing del HTML
from bs4 import BeautifulSoup
#Para interpretar el json
import json

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
      #Pagina a consultar
      page=requests.get("https://www.tenable.com/plugins/nessus/421")
      #verifica el codigo de respuesta.
      page.status_code	
      #Almacena el contenido de la pagina
      soup=BeautifulSoup(page.content)
      print(soup.h1)
      #Analizando el contendio de la pagina se identifico una estructura en json 
      #que se incluye al fina de la pagina bajo el id "NEXT_DATA"
      tenab_json=soup.find(id="__NEXT_DATA__").text
      print(tenab_json)
      #Convierte el contenido json en un diccionario se que pueda 
      newDictionary=json.loads(tenab_json)
      newDictionary
    	
    def store_obs(self):
      print("scraping Obs")
    
    
    	
    def check_end(self):
      print("Cheking end")
    	
      


s=Scrapper()
s.load_file()

    def check_end(self):
      print("Cheking end")
    	
      


s=Scrapper()
s.load_file()
