import argparse
import os
from PIL import Image
from PIL.ExifTags import TAGS




def main(directorio):
    for filename in os.listdir(directorio):
        if filename.endswith(".jpg")or filename.endswith(".png")or filename.endswith(".jpeg"):
            path = os.path.join(directorio, filename)
            my_img = Image.open(path)
            exif_data = my_img.getexif()
            for tagId in exif_data:
                tag = TAGS.get(tagId, tagId)
                data = exif_data.get(tagId)
                print(f"{tag:16}:{data}")
        else:
            continue




if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=' ',formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument("-md", metavar='METADATA', dest="md", required=True)

    directorio = parser.parse_args().md
    main(directorio)