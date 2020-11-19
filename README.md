# raspi-hallmagnetic-sensor

<p>
    <a href="https://github.com/kikuty/raspi-hallmagnetic-sensor/commits/master">
    <img src="https://img.shields.io/github/last-commit/kikuty/raspi-hallmagnetic-sensor.svg?style=flat-square&logo=github&logoColor=white">
    <a href="https://github.com/kikuty/raspi-hallmagnetic-sensor/issues">
    <img src="https://img.shields.io/github/issues-raw/kikuty/raspi-hallmagnetic-sensor.svg?style=flat-square&logo=github&logoColor=white">
    <a href="https://github.com/kikuty/raspi-hallmagnetic-sensorpulls">
    <img src="https://img.shields.io/github/issues-pr-raw/kikuty/raspi-hallmagnetic-sensor.svg?style=flat-square&logo=github&logoColor=white">
    <a href="https://github.com/kikuty/raspi-hallmagnetic-sensorpulls">
    <img src="https://img.shields.io/github/license/kikuty/raspi-hallmagnetic-sensor.svg?style=flat-square&logo=github&logoColor=white">
</p>

<p>
  <a href="#about">About</a> | 
  <a href="#tested-sensor">Tested sensor</a> | 
  <a href="#pin-assingment">PIN assingment</a> | 
  <a href="#tested-environment">Tested environment</a> | 
  <a href="#usage">Usage</a> | 
  <a href="#license">License</a> | 
  <a href="#author">Author</a> 
</p>

***
## About
A magnet field monitor to work with Hall magnet sensor on the Raspberry Pi, featuring MQTT for distributing data.

## Tested sensor  
A3144 (Hall Magnetic Field sensor)  

## PIN assingment  
* Signal -> Pin18 (as specified in the "PIN" variable in the code)  
* +V -> 3.3V (e.g. Pin1)  
* GND -> GND  (e.g. Pin39)

Also see [Raspberry Pi GPIO Usage](https://www.raspberrypi.org/documentation/usage/gpio/),
or check the Pin status using the `gpio readall` command.

## Tested environment  
* Raspberry Pi 4 model B  
* Raspberry Pi OS (32-bit) with desktop and recommended software(verrion August 2020)  
* Python 3.7.3  

## Circuit diagram example
* coming soon

## Usage  
Clone and run this code, you'll need [paho-mqtt](https://pypi.org/project/paho-mqtt/) installed on your Raspberry Pi.

```
$  sudo pip3 install paho-mqtt
```

* coming soon

## License  
This project is published under [MIT license](https://en.wikipedia.org/wiki/MIT_License).  

## Author  
Yoshinao Kikuchi  
