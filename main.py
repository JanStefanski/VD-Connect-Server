import asyncio
from asyncio import sleep
import websockets
import logging
import psutil
from gpiozero import CPUTemperature
import json


class VDServer:
    def __init__(self):
        self.websocket = None
        self.is_streaming = False

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
                            await sleep(1)
                elif message == "refresh_info":
                    await self.send_device_info()
                else:
                    await websocket.send("unknown_command")
            except websockets.ConnectionClosed:
                self.is_streaming = False
                break

    async def send_device_info(self):
        device_info = {
            "cpu_temperature": round(CPUTemperature().temperature, 1),
            "cpu_usage": psutil.cpu_percent(1),
            "memory_usage": psutil.virtual_memory()[2],
            "disk_usage": psutil.disk_usage("/").percent,
            "network_usage": psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv,
        }
        print(device_info['memory_usage'])
        await self.websocket.send('[device_info]' + json.dumps(device_info))

    async def send_client_info(self):
        client_info = {
            "remote_ip": self.websocket.remote_address[0],
            "remote_port": self.websocket.remote_address[1],
            "local_ip": self.websocket.local_address[0],
            "local_port": self.websocket.local_address[1],
        }
        await self.websocket.send('[client_info]' + json.dumps(client_info))


async def main():
    logging.basicConfig(level=logging.DEBUG)
    server = VDServer()
    async with websockets.serve(server.start, "0.0.0.0", 25931):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
