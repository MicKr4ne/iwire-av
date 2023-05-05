import shutil
import os
from os import listdir
from os.path import isfile, join, exists

img_path = r'D:\DEV\pytorch-CycleGAN-and-pix2pix\results\mixed_syn_rain\test_latest\images'
dest_path = r'D:\DEV\Thesis\Datasets\Denoiser\Restormer\mixed_syn_rain2'

ext = '.png'
norain_tag = '_real_A'
rain_tag = '_fake_B'
images = [f.replace(ext, '') for f in listdir(img_path) if f.endswith(ext) and isfile(join(img_path, f))]

for img in images:
    if img.endswith('_real_A'):
        p = img.replace(norain_tag, '')
        print(f'{img_path}\\{img}{ext}')
        print(f'{dest_path}\\norain')
        shutil.copy(f'{img_path}\\{img}{ext}', f'{dest_path}\\norain\\{p}{ext}')
    elif img.endswith('_fake_B'):
        p = img.replace(rain_tag, '')
        print(f'{img_path}\\{img}{ext}')
        print(f'{dest_path}\\rain')
        shutil.copy(f'{img_path}\\{img}{ext}', f'{dest_path}\\rain\\{p}{ext}')
exit()

for label in labels100k:
    weather = label['attributes']['weather']
    if weather in weather_cond:

        src = img_path + label['name']
        dst = img_path + weather + '/' + label['name']
        if os.path.isfile(src):
            shutil.move(src, dst)
    # if weather == 'rainy':
    #    rainy +=1
    # elif weather == 'clear':
    #    clear += 1
    # elif weather == 'snowy':
    #    snowy += 1

# print(f'rainy: {rainy}, snowy: {snowy}, clear: {clear}') 

'''
from PIL import Image
import os
from os import listdir
from os.path import isfile, join, exists

basewidth = 512


img_path= 'D:/DEV/Thesis/img_human_test'
target_path = f'{img_path}/512'

ext = ('.jpg')

files = [f.replace(ext, '') for f in listdir(img_path) if f.endswith(ext) and isfile(join(img_path, f))]
if(not exists(target_path)):
    os.makedirs(target_path)

for file in files:
    print (file)
    img = Image.open(join(img_path,f'{file}{ext}'))
    # wpercent = (basewidth/float(img.size[0]))
    # hsize = int((float(img.size[1])*float(wpercent)))
    # img = img.resize((basewidth,hsize), Image.LANCZOS)
    img = img.resize((basewidth,basewidth), Image.LANCZOS)
    img.save(join(target_path, f'{file}_512{ext}'))
'''