import threading
import socket
import time

class Client:
    client_count = 0
    def __init__(self, args):
        if len(args) != 2: 
            raise Exception
        self.conn = args[0]
        self.addr = args[1]
        self.connected = True
        print(f"[INFO] Client connected. {self.addr}")
        Client.client_count += 1

    def __len__(self):
        return Client.client_count
    
    def handle(self):
        while self.connected:
            msg_len = self.conn.recv(HEADER).decode(FORMAT)
            if msg_len:
                msg = self.conn.recv(msg_len := int(msg_len)).decode(FORMAT)
                self.connected = False if msg == DISCONNECT else True
                print(f"[{self.addr}]: {msg}")
        
        Client.client_count -= 1
        print(f"[INFO] {Client.client_count} ACTIVE CLIENTS")


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    clients = []
    
    while True:
        clients.append([Client(server.accept())])
        print(f"[INFO] {Client.client_count} ACTIVE CLIENTS")
        thread = threading.Thread(target=clients[-1][0].handle)
        clients[-1].append(thread)
        thread.start()



def not_main():
    if __name__ == "__main__":
        from globalv import *
    else:
        from Battleship.res.global_variables import *
    print("[INFO] Starting server...")
    main()


not_main()