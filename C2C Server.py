import asyncio
from websockets.asyncio.server import serve, broadcast
import os

connected = set()
history = []

async def Incoming(websocket):
  connected.add(websocket)
  while True:
    os.system("cls")
    for chat in history:
      print(f"{chat}")
    message = await websocket.recv()
  
    broadcast(connected, message)
    history.append(message)



async def main():
  async with serve(Incoming, "localhost", 8765) as server:
    await server.serve_forever()


if __name__ == "__main__":
  asyncio.run(main())