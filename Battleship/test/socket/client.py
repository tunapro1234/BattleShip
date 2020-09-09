import threading
import socket
import time


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)


def send(msg):
    # mesaj uzunluğunu alıyorsun
    msg_len = len(msg := msg.encode(FORMAT))
    # bu mesaj uzunluğunu göndermenin ne kadar tutacağını hesaplıyorsun
    send_len = str(msg_len).encode(FORMAT)
    # HEADER içinde padding yaparak bu mesajı gönderiyorsun
    send_len += b" " * (HEADER - len(send_len))
    # Daha sonra, önce mesaj uzunluğunu
    client.send(send_len)
    # sonra mesajı gönderiyorsun
    client.send(msg)


def not_main():
    if __name__ == "__main__":
        from globalv import *
    else:
        from Battleship.res.global_variables import *
    main()


not_main()