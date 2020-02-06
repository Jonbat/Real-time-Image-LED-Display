![](mouse_demo.gif)

# Real-time-32x32-Pi-Image-Displayer
Take images from a phone and display it in real-time on a 32x32 LED matrix!
An IR remote can be configured to scoll through 10 example display files.
Also, an ambient light mode can be used to control the display using surrounding light.
Check out my [youtube video](https://youtu.be/txqw9IOIMH0) some step-by-step installation instructions and demos. 👌
 
## Materials
A Raspberry Pi newer than version 1 recommended to adequately drive the display.

* [Raspberry Pi](https://www.adafruit.com/product/3055)
* [32x32 LED Display](https://www.adafruit.com/product/1484)
* [5 V Power Supply](https://www.adafruit.com/product/658)
* [IR Receiver](https://www.amazon.com/Gikfun-Infrared-Emission-Receiver-Arduino/dp/B06XYNDRGF/ref=sr_1_1?crid=2EO861DR6QX1A&keywords=vs1838b&qid=1579450541&sprefix=VS1838B%2Caps%2C155&sr=8-1)
* [Ambient Light Sensor](https://www.ebay.com/i/123260676774?)
* An Android or iOS mobile device that can take pictures

## Installation Help
The 'image_capture_mobile_app' folder runs on the mobile device and everything else runs on the Raspberry Pi. 
* [Pi Hat Installation](https://learn.adafruit.com/adafruit-rgb-matrix-plus-real-time-clock-hat-for-raspberry-pi)
* [Hardware and software integration](https://youtu.be/txqw9IOIMH0)
* [Mobile Image Capture App Installation](https://flutter.dev/docs/get-started/install)

## Built With
* [Flutter](https://flutter.dev/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Python](https://www.python.org/)

## Included Libraries
* [RPI RGB LED Matrix Library](https://github.com/hzeller/rpi-rgb-led-matrix)
* [IR Remote Module](https://github.com/owainm713/IR-Remote-Receiver-Python-Module)
* [Mobile Image Capture](https://www.coderzheaven.com/2019/04/30/upload-image-in-flutter-using-php)

