import requests
import imageio
import time
from datetime import datetime
from io import BytesIO
from PIL import Image
from requests_toolbelt.multipart.encoder import MultipartEncoder

# Configuration
gif_url = "https://radar.weather.gov/ridge/standard/KMPX_loop.gif"
upload_url = "http://192.168.50.153/doUpload"
set_gif_url = "http://192.168.50.153/set"
delete_gif_url = "http://192.168.50.153/delete"
clear_gif_queue_url = "http://192.168.50.153/set?clear=gif"
gif_dir = "/image/80x80.gif"
interval = 60

def clear_gif_queue():
    retries = 3
    for i in range(retries):
        try:
            response = requests.get(clear_gif_queue_url)
            if response.status_code == 200:
                print("GIF queue cleared successfully.")
                return True
            else:
                print(f"Clear GIF queue failed: {response.status_code} {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Clear GIF queue failed: {e}, retrying ({i + 1}/{retries})...")
            time.sleep(2 ** i)
    print("Failed to clear GIF queue after multiple attempts")
    return False

def download_and_resize_gif(url, size=(80, 80)):
    retries = 3
    for i in range(retries):
        try:
            response = requests.get(url)
            response.raise_for_status()
            gif = imageio.mimread(BytesIO(response.content), memtest=False)
            resized_gif = [Image.fromarray(frame).resize(size, Image.LANCZOS) for frame in gif]
            output = BytesIO()
            imageio.mimsave(output, resized_gif, format='GIF')
            output.seek(0)
            return output
        except requests.exceptions.RequestException as e:
            print(f"Download retrying.")
            time.sleep(2 ** i)
    raise Exception("Failed to download and resize GIF after multiple attempts")

def upload_gif(gif_data, filename):
    retries = 3
    for i in range(retries):
        try:
            gif_data.seek(0)
            m = MultipartEncoder(fields={'dir': gif_dir, 'image': (filename, gif_data, 'image/gif')})
            response = requests.post(upload_url, data=m, headers={'Content-Type': m.content_type})
            if response.status_code == 200:
                print(f"Upload successful: {filename}")
                return True
            else:
                print(f"Upload retrying")
        except requests.exceptions.RequestException as e:
            print(f"Upload retrying")
            time.sleep(2 ** i)
    print("Failed to upload GIF after multiple attempts")
    return False

def set_gif(filename):
    retries = 3
    for i in range(retries):
        try:
            url = f"{set_gif_url}?gif=/image/80x80.gif/{filename}"
            print(f"Setting GIF with URL: {url}")
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Set GIF successful: {filename}")
                return True
            else:
                print(f"Set GIF failed: {response.status_code} {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Set GIF failed: {e}, retrying ({i + 1}/{retries})...")
            time.sleep(2 ** i)
    print("Failed to set GIF after multiple attempts")
    return False

def delete_old_gif(filename):
    retries = 3
    for i in range(retries):
        try:
            url = f"{delete_gif_url}?file=/image/80x80.gif/{filename}"
            print(f"Deleting old GIF with URL: {url}")
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Deleted old GIF successful: {filename}")
                return True
            else:
                print(f"Delete old GIF failed: {response.status_code} {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Delete old GIF failed: {e}, retrying ({i + 1}/{retries})...")
            time.sleep(2 ** i)
    print("Failed to delete old GIF after multiple attempts")
    return False

def main():
    if not clear_gif_queue():
        print("Failed to clear GIF queue at startup.")
        return

    last_filename = None
    while True:
        try:
            # Step 1: Download and resize the GIF
            gif_file = download_and_resize_gif(gif_url)
            filename = datetime.now().strftime("weather%H%M.gif")
            
            # Step 2: Upload the resized GIF
            if not upload_gif(gif_file, filename):
                continue
            
            # Step 3: Set the uploaded GIF
            if not set_gif(filename):
                continue

            # Step 4: Delete the old GIF
            if last_filename and not delete_old_gif(last_filename):
                continue
            
            last_filename = filename

            time.sleep(interval)
        except Exception as e:
            print("An error occurred:", e)
            time.sleep(interval)

if __name__ == "__main__":
    main()
