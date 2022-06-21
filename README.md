# VD Connect Server


<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
[English](README.md) | [Polski](README_pl.md) | [中文](README_zh.md)

This is the VD Connect server.
It is a websocket server that is supposed to run on a Raspberry Pi and to provide VD Connect companion app with device
info.

## Installation

To install this application go into the folder you want to download the application and run the following command to
clone the repository and go into the folder:

```shell
git clone https://github.com/JanStefanski/VD-Connect-Server.git
cd VD-Connect-Server
```

Then run the following command to install python requirements:

```shell
pip install -r requirements.txt
```

## Startup

To start the server run the following command:

```shell
python3 main.py
```

## Project structure

The project depends on packages described in the requirements.txt file.
It uses `websocket` and `asyncio` packages to run the server. 
`gpiozero` and `psutil` is used to collect data about the workstations' and provide it through created websockets.
The `gpiozero` package can also be used to control Raspberry Pi's GPIO pins.
