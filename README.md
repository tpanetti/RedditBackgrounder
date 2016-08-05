# Reddit Backgrounder
![alt text](https://img.shields.io/badge/python-3.5-blue.svg "Tested on Python version 3.5.2")
Grabs the top valid image from a specified subreddit and sets it to be the Windows desktop background.

This is tested to work on 64 bit Windows 10 build 1607 (anniversary update).
`minx` and `miny` can be set to only look for images that are above a certain resolution.
The default subreddit to look for is /r/spaceporn.

### Usage:
Dependent on [Pillow](https://pypi.python.org/pypi/Pillow/) and [praw](https://pypi.python.org/pypi/praw). Install these dependencies with pip using `pip install Pillow` and `pip install praw`. After that, simply execute main.py and enjoy your new background!

Support for 32 bit can be added by changing

```python
ctypes.windll.user32.SystemParametersInfoW(...)
```

to

```python
ctypes.windll.user32.SystemParametersInfoA(...)
```

This should work on older versions of Windows, but will not work on WindowsXP as the file is not converted to BMP format.

### To do:
* Automatic detection of 32bit vs 64bit
* Search after the default limit if no valid images are found
* Add option to search for specific resolution. Closest resolution image will be selected
* Save recently used images to ensure new ones are used when possible
* Add documentation explaining how to make this an automatically run Windows task
