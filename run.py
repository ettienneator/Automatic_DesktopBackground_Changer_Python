import random
import os
import pathlib
import schedule
import time
import ctypes
import requests
import json
import urllib.request
import shutil
from datetime import timedelta, date
import datetime

#from PIL import Image
#from io import BytesIO


WALLPAPER_FOLDER = 'wallpapers'
FILENAME = '1.jpg'

def get_filenmes_from_directory(folder_location):
    files = os.listdir(folder_location)
    return files

def random_date():

    # Picks date from the start of 2015 to today.
    start_date = datetime.date(2015, 1, 1)
    end_date = date.today()

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)

    # DEBUG: # Prints random_date to see if its working.
    # DEBUG: print(random_date)

    return random_date

def set_wallpaper():
    print("Setting the wallpaper")

    response = requests.get('https://api.nasa.gov/planetary/apod?api_key=089zGvRSwZZzT4rLmMT9hUozq6BedVrv5wGPjjas')
    # DEBUG: print(response.status_code)

    # Gets the random_date and puts it into date. The formatted string replaces date with random_date.
    date = random_date()
    query = urllib.request.urlopen(f'https://api.nasa.gov/planetary/apod?api_key=089zGvRSwZZzT4rLmMT9hUozq6BedVrv5wGPjjas&date={date}')

    # Reads the json query.
    apodread = query.read()

    # Puts the query info into a specific format.
    decodeapod = json.loads(apodread.decode('utf-8'))

    # DEBUG: Prints the API Data.
    # DEBUG: print(decodeapod)

    # Takes the URL and downloads it into current directory. File becomes named "1.jpg".
    # The reason the picture may becaome just black, is because Nasa has included videos in their APOD Api.
    # Alternatively, you can use hdurl
    urllib.request.urlretrieve(decodeapod['url'], FILENAME)

    # Gets full file directory for wallpapers.
    wallpapers = get_filenmes_from_directory(WALLPAPER_FOLDER)

    # Replaces the new image with the old image in the folder.
    os.replace("1.jpg", f"wallpapers/{FILENAME}")

    # Chooses the only file in wallpapers folder. Gets the complete file path that Windows can read.
    full_wallpaper_path = os.path.join(
        pathlib.Path().absolute(),
        WALLPAPER_FOLDER,
        FILENAME
    )

    # Puts the full path of the file to the desktop.
    ctypes.windll.user32.SystemParametersInfoW(20, 0, full_wallpaper_path , 0)

def run():
    # Setup a scheduler that changes wallpaper
    schedule.every(5).seconds.do(set_wallpaper)

    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == '__main__':
    run()
