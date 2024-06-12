# SmallTVProWeatherMap
Adds a Weather Map gif for the SmallTV Pro Weather app. 

![water](https://github.com/djware/SmallTVProWeatherMap/assets/85318457/9aaee89d-13b7-4db9-98dd-d8dd17fbf255)

![SmallTv Pro](https://github.com/GeekMagicClock/smalltv-pro/raw/main/assets/smalltv-pro-banner.png)

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
How It Works
Download and Resize GIF:

The script downloads a GIF from the specified URL and resizes it to 80x80 pixels.
Upload GIF:

The resized GIF is uploaded to the SmallTv Pro device.
Set GIF:

The uploaded GIF is set as the current display on the SmallTv Pro.
Delete Old GIF:

The previously displayed GIF is deleted to keep the storage clean.
Clear GIF Queue:

The GIF queue is cleared at startup and can be cleared within the functions as needed.
Contributing
We welcome contributions to improve this script! If you have any suggestions or find any bugs, please open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgements
SmallTv Pro by GeekMagicClock
The Python libraries used in this project
