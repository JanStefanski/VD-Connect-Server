import asyncio
import websockets
import logging
import sys
import os
import psutil
import random
import json
from gpiozero import CPUTemperature, RGBLED

led = RGBLED(red=17, green=27, blue=22)

led.color = (0, 0, 0)


def read_config():
    with open("config.json") as config_file:
        return json.load(config_file)


class VDServer:
    def __init__(self):
        self.websocket = None
        self.is_streaming = False
        self.debug_wo_raspberry = False

    async def start(self, websocket, path):
        self.websocket = websocket
        while True:
            try:
                message = await websocket.recv()
                if message == "my_info":
                    await self.send_client_info()
                elif message == "stream_device_info":
                    if not self.is_streaming:
                        self.is_streaming = True
                        while True:
                            await self.send_device_info()
                            await asyncio.sleep(1)
                elif message == "refresh_info":
                    await self.send_device_info()
                elif message == "board_info":
                    pass  # TODO: Send RPi board info
                else:
                    await websocket.send("unknown_command")
            except websockets.ConnectionClosed:
                self.is_streaming = False
                break

    async def send_device_info(self):
        device_info = {
            "cpu_temperature": round(CPUTemperature().temperature,
                                     1) if self.debug_wo_raspberry is False else random.randint(0, 100),
            "cpu_usage": psutil.cpu_percent(1),
            "memory_usage": psutil.virtual_memory()[2],
            "disk_usage": psutil.disk_usage("/").percent,
            "network_usage": psutil.net_io_counters().bytes_sent
                             + psutil.net_io_counters().bytes_recv,
        }
        print(device_info["memory_usage"])
        await self.websocket.send("[device_info]" + json.dumps(device_info))

    async def send_client_info(self):
        client_info = {
            "remote_ip": self.websocket.remote_address[0],
            "remote_port": self.websocket.remote_address[1],
            "local_ip": self.websocket.local_address[0],
            "local_port": self.websocket.local_address[1],
        }
        await self.websocket.send("[client_info]" + json.dumps(client_info))


async def main():
    config = read_config()
    server_config = config["server_config"]
    if not os.path.exists(server_config["log_file"]):
        os.makedirs(os.path.dirname(server_config["log_file"]))

    logging.basicConfig(
        level=(logging.DEBUG if server_config["debug"] == "True" else logging.INFO),
        format="%(asctime)s %(levelname)s: %(message)s",
        handlers=[
            logging.FileHandler(server_config["log_file"]),
            logging.StreamHandler(sys.stdout),
        ],
    )
    server = VDServer()
    async with websockets.serve(
            server.start,
            server_config["host"],
            server_config["port"],
            close_timeout=server_config["close_timeout"],
            ping_timeout=server_config["ping_timeout"],
    ):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
