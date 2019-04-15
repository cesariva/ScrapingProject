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
#Para configurar retardos de tiempo
import time

class Scrapper:
"""Clase base de Scraping que tiene la informacion básica para configurar, 
cargar el archivo, realizar el scraping, guardar la observacion, y esperar
un tiempo. 
Este script se debe invocar como Scraper.py AchivoConfiguracion
Ejemplo: Scraper.py TenableConfig.txt
"""

    def __init__(self):
        """ Incicializacion del scraper con el archivo de configuracion dado en el primer argumento"""
      print("Inicio Scraper")
      # Load the configuration filename in the first argument
      with open(sys.argv[1]) as f:
          configf = f.read()
      #Utiliza la clase configparser para interperetar el archivo de configuracion
      config = ConfigParser.RawConfigParser(allow_no_value=True)
      config.readfp(io.BytesIO(configf))
      # Inicializa el contenido de las variables de la clase con el archivo de configuracion
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
      self.listObs=[]

    def load_file(self):
        """ Funcion que carga el archivo donde se almacena el dataset"""
      exists=os.path.isfile(self.filename)
      if exists:
        with open(self.filename, mode='r') as csv_file:
          csv_reader = csv.DictReader(csv_file)
        csv_file.close()
          
    def scrap_obs(self):
        """ Funcion que descarga la informacion especifica de la pagina WEB y la almacena temporalmente en memoria"""
      print("Scraping obs: "+str(self.counter))
      #Pagina a consultar
      page=requests.get(self.base_url+str(self.counter))
      #Almacena el contenido de la pagina
      soup=BeautifulSoup(page.content)
      #Analizando el contenido de la pagina se identifico una estructura en json 
      #que se incluye al final de la pagina bajo el id "NEXT_DATA"
      tenab_json=soup.find(id="__NEXT_DATA__").text
      #print(tenab_json)
      #Convierte el contenido json en un diccionario se que pueda 
      newDictionary=json.loads(tenab_json)
      #print(newDictionary)
      self.listObs.append(newDictionary['props']['pageProps']['plugin'])
    	
    def store_obs(self):
        """ Funcion de almacena en disco en formato CVS los datos que se tienen en memoria"""
      print("storing Obs")
      fields=set()
      for i in self.listObs:
          fields=fields.union(set(i.keys()))
      with open('mycsvfile.csv','wb') as f:
          w = csv.DictWriter(f,fieldnames=fields)
          w.writeheader()
          w.writerows(self.listObs)
      
    def check_end(self):
        """ Funcion que verifica si ya se llego al final del scraping"""
      print("Cheking end")
      if self.final>self.counter:
        self.counter+=1
        return True
      return False

    def ex_delay(self):
        """ Función que ejecuta un retardo """
      print("Delay") 	
      time.sleep(float(self.tdelay))

""" Codigo principal del scraper """
#Inicializa la clase
s=Scrapper()
#Carga el archivo
s.load_file()
# Hace un bucle hasta que se cumpla la condición de fin de scraping
while s.check_end():
   # Hace la consutla especifica en la página WEB y guarda el resutlado en memoria 
   s.scrap_obs()
   # Graba el valor consultado en archivo CSV, en el disco. 
   s.store_obs()
   # Ejecuta un retardo antes de realizar una nueva consulta a la página WEB. 
   s.ex_delay()
   


