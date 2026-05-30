import os
import requests

Auth_token="LPeq-p-Mjmu1HeKR2jsQEE39y_60inVcW9Tf0_ebW5Q"

def download_wallpaper(folder_name="Wallpapers"):
    if not os.path.exist(folder_name):
        os.makedirs(folder_name)
        print(f"Created Folder:{folder_name}")
    url=f"https://api.unsplash.com/photos/random/?client_id={Auth_token}"
    try:
        response=requests.get(url,timeout=15)
        if response.status_code == 200:
            

