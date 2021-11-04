from PIL import Image, ImageFile
import PIL
import os
import glob
from alive_progress import alive_bar
ImageFile.LOAD_TRUNCATED_IMAGES = True

def compress_images(startdirectory='./images/', quality=65, maxsize=1080):
    currentdir = os.path.dirname(__file__)
    outputdirectory = './test/'

    for root, dirs, filenames in os.walk(startdirectory):
        print('working')
        print(root.lstrip('./'))
        create = os.path.join(outputdirectory,root.lstrip('./'))
        try:
            os.makedirs(create)
            print('address created')
        except:
            print('address exist')
    for root, dirs, filenames in os.walk(startdirectory):
        images = [file for file in filenames if file.endswith(('jpg', 'png', 'PNG'))]
        with alive_bar(len(images)) as bar:
            for image in images:
                os.chdir(root)
                try:
                    img = Image.open(image)
                except:
                    print('bad image, skipping')
                (x,y) = (img.size)
                if x > maxsize or y> maxsize:
                    img.thumbnail((maxsize,maxsize))
                img.save(currentdir + '/test' + root.lstrip('.') + '/'+ image, optimize=True, quality=quality)
                os.chdir(currentdir)
                bar()
    for root, dirs, filenames in os.walk(startdirectory):
        images = [file for file in filenames if file.endswith(('tif'))]
        with alive_bar(len(images)) as bar:
            for image in images:
                os.chdir(root)
                try:
                    img = Image.open(image)
                except:
                    print('bad image, skipping')
                (x,y) = (img.size)
                if x > maxsize or y> maxsize:
                    img.thumbnail((maxsize,maxsize))
                img.convert('RGB').save(currentdir + '/test' + root.lstrip('.') + '/'+ image.replace('tif', 'jpg'), "JPEG", quality=quality)
                os.chdir(currentdir)
                bar()
    for root, dirs, filenames in os.walk(startdirectory):
        images = [file for file in filenames if file.endswith(('jpeg'))]
        with alive_bar(len(images)) as bar:
            for image in images:
                os.chdir(root)
                try:
                    img = Image.open(image)
                except:
                    print('bad image, skipping')
                (x,y) = (img.size)
                if x > maxsize or y> maxsize:
                    img.thumbnail((maxsize,maxsize))
                img.convert('RGB').save(currentdir + '/test' + root.lstrip('.') + '/'+ image.replace('jpeg', 'jpg'), "JPEG", quality=quality)
                os.chdir(currentdir)
                bar()

compress_images()
