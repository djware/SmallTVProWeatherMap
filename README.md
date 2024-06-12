# SmallTVProWeatherMap
Adds a Weather Map gif for the SmallTV Pro Weather app. 

![water](https://github.com/djware/SmallTVProWeatherMap/assets/85318457/9aaee89d-13b7-4db9-98dd-d8dd17fbf255)

![SmallTv Pro](https://github.com/GeekMagicClock/smalltv-pro/raw/main/assets/smalltv-pro-banner.png)

This repository contains a Python script designed for managing GIF images on the [SmallTv Pro](https://github.com/GeekMagicClock/smalltv-pro). The script automates the downloading, resizing, uploading, setting, and deleting of GIFs to keep your SmallTv Pro display updated with the latest weather radar animations.

## Features

- **Automated GIF Management**: Download, resize, and upload GIFs automatically at set intervals.
- **Queue Management**: Clear the GIF queue at startup and within functions to ensure smooth operation.
- **Retry Mechanism**: Robust error handling with retry logic for downloading, uploading, setting, and deleting GIFs.

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
