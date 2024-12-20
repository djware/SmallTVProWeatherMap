# SmallTVProWeatherMap
Adds a Weather Map gif for the SmallTV Pro Weather app. 

![water](https://github.com/djware/SmallTVProWeatherMap/assets/85318457/9aaee89d-13b7-4db9-98dd-d8dd17fbf255)

![SmallTv Pro](https://github.com/GeekMagicClock/smalltv-pro)

Disclaimer - Per [GeekMagicClock](https://github.com/GeekMagicClock/smalltv-pro/issues/72#issuecomment-2521860672) the data is written directly to the internal NOR flash, the erasing and writing life may be limited. It is not recommended to update pictures frequently as it may damage the device, on your own risk.

This repository contains a Python script designed for managing GIF images on the [SmallTv Pro](https://github.com/GeekMagicClock/smalltv-pro). The script automates the downloading, resizing, uploading, setting, and deleting of GIFs to keep your SmallTv Pro display updated with the latest weather radar animations.

## Features

- **Automated GIF Management**: Download, resize, and upload GIFs automatically at set intervals.

## Prerequisites

- Python 3.x
- Required Python libraries:
  - `requests`
  - `imageio`
  - `Pillow`
  - `requests_toolbelt`

You can install the required libraries using:
```bash
pip install requests imageio Pillow requests_toolbelt
```

## Configure the script:
Weather gif can be found here. https://www.radarmonster.com/ find your location and grab the image url. Copy it into the gif_url section below. 


```bash
# Configuration
gif_url = "https://radar.weather.gov/ridge/standard/KMPX_loop.gif"
upload_url = "http://192.168.50.153/doUpload"
set_gif_url = "http://192.168.50.153/set"
delete_gif_url = "http://192.168.50.153/delete"
clear_gif_queue_url = "http://192.168.50.153/set?clear=gif"
gif_dir = "/image/80x80.gif"
interval = 60
```
## How It Works
Download and Resize GIF:

The script downloads a GIF from the specified URL and resizes it to 80x80 pixels.


The resized GIF is uploaded to the SmallTv Pro device.


The uploaded GIF is set as the current display on the SmallTv Pro.


The previously displayed GIF is deleted to keep the storage clean.


The GIF queue is cleared at startup and can be cleared within the functions as needed.


## Acknowledgements
SmallTv Pro by GeekMagicClock
The Python libraries used in this project
