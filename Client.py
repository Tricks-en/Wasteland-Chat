import asyncio
import websockets
import os

history = []

async def receive_task(websocket):
    try:
        async for message in websocket:
          if f">>> {message.lstrip("<<<")}" not in history:
            print(f"<<< {message}")
            history.append(f"<<< {message}")
    except websockets.exceptions.ConnectionClosed:
        print("\nConnection closed by server")

async def send_task(websocket):
    while True:
        os.system("cls")
        for line in history:
            print(line)
        message = await asyncio.to_thread(input, "")  # run blocking input in thread
        if message.lower() in ["quit", "exit", "q"]:
            break
        await websocket.send(message)
        if message != ">>> ":
          print(f">>> {message}")
          history.append(f">>> {message}")

async def chat():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        # Clear + show initial history
        os.system("cls")
        for line in history:
            print(line)

        # Run receive and send concurrently
        receive = asyncio.create_task(receive_task(websocket))
        send = asyncio.create_task(send_task(websocket))

        # Wait for either to finish (e.g. user types quit)
        done, pending = await asyncio.wait(
            [receive, send], return_when=asyncio.FIRST_COMPLETED
        )

        # Cancel the other task
        for task in pending:
            task.cancel()

if __name__ == "__main__":
    try:
        asyncio.run(chat())
    except KeyboardInterrupt:
        print("\nExited")