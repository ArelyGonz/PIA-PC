''


def Main():
    info = 'PIA 063 PC E2022'
    parser = argparse.ArgumentParser(info)

    parser.add_argument('-opt', '--option', required = True, help = 'Opcion para elegir script a utilizar.', dest = 'opt')

    
    
    #ENCRIPTAR
    parser.add_argument('-enc', '--enc', help = 'Ruta del directorio a encriptar.')
    #DESENCRIPTAR
    parser.add_argument('-dec', '--dec', help = 'Ruta del directorio a desencriptar.')
    #WEBSCRAPE
    parser.add_argument('-ws', '--ws', help= 'Url de la pagina a escanear.')
    #METADATA
    parser.add_argument('-md', '--md', help= 'Ruta del imagen para extraer informacion. ')
    #ESCANEO DE PUERTOS 
    parser.add_argument('-ip', '--ip', help= 'IP a escanear')
    #ESCANEO DE PUERTOS POWERSHELL
    parser.add_argument('-ep', '--ep', help= 'IP a escanear CON PS')
    #APi 
    parser.add_argument('-api', '--api', help= 'API y busqueda de correos')
    
    
   

    args = parser.parse_args()
    
    
        
    if args.opt.upper()== 'ENCRIPTAR':
         path_to_encrypt = args.enc
         encrypt.main(path_to_encrypt)

    if args.opt.upper()== 'DESENCRIPTAR':
         path_to_encrypt = args.dec
         decrypt.main(path_to_encrypt)
     
    if args.opt.upper()== 'ESCANEO_DE_PUERTOS':
        target = args.ip
        puertos.main(target)

    if args.opt.upper()== 'WEBSCRAPE':
         url = args.ws
         webscrape.main(url)

    if args.opt.upper()== 'METADATA':
         directorio = args.md
         metadata.main(directorio)
      
    if args.opt.upper()== 'API':
         email = args.api
         api.main(email)
       

    if args.opt.upper()== 'ESCANEOPUERTOSPOWERSHELL':
         command = "powershell -ExecutionPolicy ByPass -File EscaneoPuertosPowershell.ps1"
         print(command)
         powerShellResult = subprocess.run(command)
    
if __name__ == '__main__':
    import argparse
    import encrypt
    import decrypt
    import puertos
    import metadata
    import api
    import webscrape
    import subprocess    
    Main()
    
    
    
