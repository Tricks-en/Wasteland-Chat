from websockets.sync.client import connect
import os

history = []

def chat():
  uri = "ws://localhost:8765"
  with connect(uri) as websocket:
    while True:
      os.system("cls")
      for chat in history:
        print(f"{chat}")
        
      message = input("")

      websocket.send(message)
      print(f">>> {message}")
      history.append(f">>> {message}")

      os.system("cls")
      for chat in history:
        print(f"{chat}")

      response = websocket.recv()
      print(f"<<< {response}")
      history.append(f"<<< {response}")


if __name__ == "__main__":
  chat()