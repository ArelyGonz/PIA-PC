import nmap
import argparse

#toma el rango de los puertos que seran escaneados



def main(target): 
    scanner = nmap.PortScanner()
    for i in range(10 , 20+1):
        #Empieza el scaneo de puertos
        res = scanner.scan( target ,str(i))
        for host in scanner.all_hosts():
            print('Host : %s (%s)' % (host, scanner[host].hostname()))
            print('State : %s' % scanner[host].state())
            for proto in scanner[host].all_protocols():
                print('Protocol : %s' % proto)

                lport = scanner[host][proto].keys()
                for port in lport:
                    print ('port : %s\tstate : %s' % (port, scanner[host][proto][port]['state']))              
                        

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=' ',formatter_class=argparse.            
                        RawDescriptionHelpFormatter)

    parser.add_argument("-ip", metavar='ESCANEO_DE_PUERTOS', dest="ip", required=True)

    target = parser.parse_args().ip

    main(target) 
                    
                
                


    

             
             
            
        
