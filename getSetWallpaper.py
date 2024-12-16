import os
import requests
from dotenv import load_dotenv
import socket
import time
import subprocess

def is_connected():
    try:
        # Connect to the internet
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False

load_dotenv(dotenv_path='/home/risriddle/Workstation/Projects/Python/setWallpaper/.env')

# Check for internet connection up to 15 minutes (900 seconds)
for _ in range(90):
    if is_connected():
        api_key = os.getenv('API_KEY')
        res = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}")

        if res.status_code == 200:
            data = res.json()
            image_url = data.get('url')
            folder_path = "/home/risriddle/Pictures/NASA_APOD"
            if image_url:
                print(f"Image URL: {image_url}")

                 # Delete previous images in the folder
                # for file in os.listdir(folder_path):
                #     file_path = os.path.join(folder_path, file)
                #     try:
                #         if os.path.isfile(file_path):
                #             os.remove(file_path)
                #             print(f"Deleted previous file: {file_path}")
                #     except Exception as e:
                #         print(f"Error deleting file {file_path}: {e}")


                image_response = requests.get(image_url)
                if image_response.status_code == 200:
                    

                    os.makedirs(folder_path, exist_ok=True)

                    image_extension = image_url.split('.')[-1]
                    file_path = os.path.join(folder_path, f"apod.{image_extension}")

                    with open(file_path, "wb") as file:
                        file.write(image_response.content)

                    print(f"Image saved successfully to {file_path}")

                    # Set wallpaper for dark mode using GNOME command
                   
                    # os.system(f"gsettings set org.gnome.desktop.background picture-uri-dark file://{file_path}")
                    result = os.system(f"gsettings set org.gnome.desktop.background picture-uri-dark file:///{file_path}")
                    print(f"gsettings command result: {result}")

                    print("Wallpaper set successfully in dark mode style.")
                else:
                    print("Failed to fetch the image content.")
            else:
                print("No image found in the response.")
        else:
            print(f"Error: Unable to fetch data, status code {res.status_code}")
        
        break
    else:
        print("No internet connection. Retrying in 10 seconds...")
        time.sleep(10)
else:
    print("No internet connection after 15 minutes. Exiting script.")




