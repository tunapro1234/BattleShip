import threading
import socket
import time
import json # burada dbex kullanmalıyım

class Client:
    client_count = 0
    def __init__(self, args):
        if len(args) != 2: 
            raise Exception
        self.conn = args[0]
        self.addr = args[1]
        self.mode = sender
        self.connected = True
        
                
        self.old_t_msg = None
        self.t_msg = None
        self.r_msg = None
        
        print(f"[INFO] Client initialized. {self.addr}")
        Client.client_count += 1

    def __len__(self):
        return Client.client_count
    
    def recv(self, timeout=None):
        msg_len = self.conn.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg = self.conn.recv(msg_len := int(msg_len)).decode(FORMAT)
            return msg
        print("cidden neler olduğunu bilmiyorum")
        recv()

    def send(self, msg):
        msg_len = len(msg := msg.encode(FORMAT))
        send_len = str(msg_len).encode(FORMAT)
        send_len += b" " * (HEADER - len(send_len))
        self.conn.send(send_len)
        self.conn.send(msg)
                
    def receiver(self):
        while self.connected:
            # her an disconnect mesajı gelebilir
            msg = recv_msg()
            if msg == DISCONNECT:
                self.connected = False
            
            if self.mode == receiver:
                if msg.startswith(";;"):
                    if msg == RECV_:
                        self.mode = sender
                    elif msg == START:
                        self.r_msg = msg
                
                elif msg.startswith("(") and msg.endswith(")"):
                    try:
                        msg = json.loads(msg)
                    except:
                        raise Exception("HACKLENDIK")
                    
                    self.r_msg = msg
                        
            
            print(f"[{self.addr}]: {msg}")
        
        Client.client_count -= 1
        print(f"[INFO] {Client.client_count} ACTIVE CLIENTS")
    
    def transmitter(self):
        while self.connected:
            # yeni mesaj eklendiğinde ve gönderen tarafsak
            if self.t_msg != self.old_t_msg and self.mode == sender:
                self.send(self.t_msg)
                self.old_t_msg = self.t_msg

    def handler():
        self.receive_thread = threading.Thread(target=self.receiver)
        self.send_thread = threading.Thread(target=self.transmitter)
        self.transmitter_thread.start()
        self.receive_thread.start()
        while True:
            
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    # clients = []
    
    while True:
        clients.append(Client(server.accept()))
        print(f"[INFO] {Client.client_count} SELECTABLE CLIENTS")
        # thread = threading.Thread(target=clients[-1][0].handle)
        # clients[-1].append(thread)
        thread.start()

def not_main():
    if __name__ == "__main__":
        from globalv import *
    else:
        from Battleship.res.global_variables import *
    print("[INFO] Starting server...")
    main()


not_main()