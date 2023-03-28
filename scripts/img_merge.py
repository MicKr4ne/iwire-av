from PIL import Image
from os import listdir
from os.path import isfile, join, exists

img1_path = r'D:\DEV\Thesis\Datasets\Denoiser\Restormer\mixed_syn_rain2\val\rain'
img2_path = r'D:\DEV\Thesis\Datasets\Denoiser\Restormer\mixed_syn_rain2\val\norain'
img_destpath = r'D:\DEV\Thesis\Datasets\Denoiser\RESCAN\mixed_syn_rain2\val'

ext = '.png'
images = [f.replace(ext, '') for f in listdir(img1_path) if f.endswith(ext) and isfile(join(img1_path, f))]

for img in images:

    #Read the two images
    image1 = Image.open(f'{img1_path}/{img}{ext}')
    # image1.show()
    image2 = Image.open(f'{img2_path}/{img}{ext}')
    #image2.show()
    #resize, first image
    #image1 = image1.resize((426, 240))
    image1_size = image1.size
    image2_size = image2.size
    new_image = Image.new('RGB',(2*image1_size[0], image1_size[1]), (250,250,250))
    new_image.paste(image1,(0,0))
    new_image.paste(image2,(image1_size[0],0))
    new_image.save(f'{img_destpath}/{img}{ext}',"png")
    #new_image.show()