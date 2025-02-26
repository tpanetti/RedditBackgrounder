#!python3
import praw
import ctypes
import requests
import os
import random
import sys
from PIL import Image
from io import BytesIO

#Grab arguments if resolution was specified in args
if len(sys.argv) == 2:
	minx = argv[0]
	miny = argv[1]
else:#Else grab screen resolution
	minx = ctypes.windll.user32.GetSystemMetrics(0)
	miny = ctypes.windll.user32.GetSystemMetrics(1)

user_agent = 'reddit_background'
subList = ['spaceporn', 'earthporn', 'CityPorn', 'wallpaper', 'EarthPorn', 'BeachPorn', 'SummerPorn', 'WinterPorn']
subreddit = random.choice(subList)


path = r""

r = praw.Reddit(user_agent=user_agent);
submissions = r.get_subreddit(subreddit).get_hot()
index = 0;
for x in submissions:
    r = requests.get(x.url)
    try:
        image = Image.open(BytesIO(r.content))
    except IOError:
        print("Not an image.")
        continue
    if(image.size[0] > minx and image.size[1] > miny):
        image.save('image', image.format)
        path = os.getcwd() + r'\image'
        print(path);
        break;
    index += 1


#Check architecture before assigning image to background
try:	#64-bit
	os.environ["PROGRAMFILES(X86)"]
	ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 3)
except:	#32-bit
	ctypes.windll.user32.SystemParametersInfoA(20, 0, path, 3)

