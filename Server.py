import asyncio
from websockets.asyncio.server import serve
import os

history = []

async def chat(websocket):
  while True:
    os.system("cls")
    for chat in history:
      print(f"{chat}")
    message = await websocket.recv()
    print(f"<<< {message}")
    history.append(f"<<< {message}")

    greeting = input("")

    await websocket.send(greeting)
    print(f">>> {greeting}")
    history.append(f">>> {greeting}")

async def main():
  async with serve(chat, "localhost", 8765) as server:
    await server.serve_forever()


if __name__ == "__main__":
  asyncio.run(main())