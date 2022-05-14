import os
import argparse
import requests
from lxml import html



def main(url):
    print("\nObteniendo imagenes de la url:"+ url)

    try:
        response = requests.get(url)  
        parsed_body = html.fromstring(response.text)

        # expresion regular para obtener imagenes
        images = parsed_body.xpath('//img/@src')

        print ('Imagenes %s encontradas' % len(images))

        #create directory for save images
        os.system("mkdir images")

        for image in images:
            if image.startswith("http") == False:
                download = url + image
            else:
                download = image
            # download images in images directory
            r = requests.get(download)
            f = open('images/%s' % download.split('/')[-1], 'wb')
            f.write(r.content)
            f.close()

    except Exception as e:
        print(e)
        print ("Error conexion con " + url)
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=' ',formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("-ws", metavar='WEBSCRAPE', dest="ws", required=True)

    url = parser.parse_args().ws
    main(url)