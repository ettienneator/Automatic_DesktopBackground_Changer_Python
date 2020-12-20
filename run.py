import random
import os
import pathlib
import schedule
import time
import ctypes
import requests

#from PIL import Image
#from io import BytesIO


WALLPAPER_FOLDER = 'wallpapers'

def get_filenmes_from_directory(folder_location):
    files = os.listdir(folder_location)
    return files

def set_wallpaper():
    print("Setting the wallpaper")

    #response = requests.get('https://api.nasa.gov/planetary/apod?api_key=089zGvRSwZZzT4rLmMT9hUozq6BedVrv5wGPjjas')
    #print(response.status_code)

    #image_bytes = io.BytesIO(response.content)

    #img = PIL.Image.open(image_bytes)
    #img.show()

    wallpapers = get_filenmes_from_directory(WALLPAPER_FOLDER)
    random_wallpaper = random.choice(wallpapers)
    full_wallpaper_path = os.path.join(
        pathlib.Path().absolute(),
        WALLPAPER_FOLDER,
        random_wallpaper
    )

    ctypes.windll.user32.SystemParametersInfoW(20, 0, full_wallpaper_path , 0)

def run():
    # Setup a scheduler that changes wallpaper
    schedule.every(5).seconds.do(set_wallpaper)

    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == '__main__':
    run()
