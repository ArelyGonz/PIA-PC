import json
import requests
import argparse

def main (email):
  apikey = ("6e8e0eb1a4f4008f226176b77cc56f2f70cdb723")
  page = requests.get ("https://api.hunter.io/v2/email-verifier?email="+email+"&api_key="+apikey)
  print ("La respuesta HTTP:", page.status_code)
  hunter = json.loads(page.content)
  
  input("Se muestra el contenido del diccionario")
  for key in hunter["data"]:
      print (key, hunter["data"][key])
      if key == "sources":
          print ("Sources",len(hunter["data"]["sources"]))
          print ("\n\nEl correo "+email+", se encontró en las siguientes fuentes:")
          for sourc in range(len(hunter["data"]["sources"])):
              URL = "http://"+hunter["data"]["sources"][sourc]["domain"]
              pagestat = requests.get(URL)
              if pagestat.status_code == 200:
                  print (sourc,"\t",URL,"\tstatus:",pagestat.status_code)
              else:
                  print (sourc,"\t",URL,"\tstatus:",pagestat.status_code, "Falló")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=' ',formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("-api", metavar='API', dest="api", required=True)

    main(email)