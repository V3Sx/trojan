import socket
from time import sleep

IP = "10.168.61.198"
PORT = 443

def connect(IP, PORT):
    try:
        c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c.connect((IP, PORT))
        return c
    except Exception as e:
        print(f"Error: {e}")


def listen(c):
    try:
        while True:
            data = c.recv(1024).decode().strip()
            if data == "/exit":
                return
            else:
                print(data)
                
    except Exception as e:
        print(f"listen function error: {e}")

if __name__ == "__main__":
    try:
        while True:
            client = connect(IP, PORT)
            if client:
                        listen(client)
            else:
                        sleep(.5)

    except KeyboardInterrupt:
                print("Program stopped by user.")

    except Exception as error:
        print(f"Main connection error: {error}")