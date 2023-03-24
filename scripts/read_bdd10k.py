import json
import shutil
import os

with open('./bdd100k_labels_images_train.json') as labels:
    labels100k = json.load(labels)

img_path = './bdd100k/images/100k/train/'
rainy = 0
snowy = 0
clear = 0
weather_cond = ['rainy', 'clear', 'snowy']
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
