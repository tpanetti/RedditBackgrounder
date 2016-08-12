#!python3
import praw
import ctypes
import requests
import os
from PIL import Image
from io import BytesIO

user_agent = 'reddit_background'
subreddit = 'spaceporn'
minx = 2560
miny = 1440

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

