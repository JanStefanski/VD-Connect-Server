# VD伴侣应用服务器

<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

[中文](README_zh.md) | [English](README.md) | [Polski](README_pl.md)

这就是VD连接服务器。它是一个websocket服务器，它被设计为在Raspberry Pi上运行，并且提供VD连接应用程序与设备信息。

## 安装

要安装这个应用程序，请进入要下载的文件夹，并运行以下命令：
```shell
git clone https://github.com/JanStefanski/VD-Connect-Server.git
cd VD-Connect-Server
```

然后运行以下命令，以安装python依赖项：
```shell
pip install -r requirements.txt
```

## 启动

要启动服务器，请运行以下命令：
```shell
python3 main.py
```

## 项目结构

这个项目依赖于requirements.txt文件中描述的包。 它使用`websocket`和`asyncio`包来运行服务器。 `gpiozero`和`psutil`是用来收集工作站和提供它们的数据的。 `gpiozero`可以用来控制Raspberry Pi上的GPIO引脚。