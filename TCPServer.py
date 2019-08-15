#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import datetime
import socket
import threading
import time

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(2)

print("[*] Listening on [%s:%d]" % (bind_ip, bind_port))


def handle(client_socket, addr):
    while 1:
        request = client_socket.recv(4096).decode("utf-8")
        print("[*] From [%s:%d] received: %s Now is %f" % (addr[0], addr[1], request, time.time()))
        client_socket.send("ACK!".encode("utf-8"))


while 1:
    client, addr = server.accept()
    print("[*] Accepted connection from: [%s:%d] in [%s]" % (addr[0], addr[1], datetime.datetime.now().time()))
    client_handler = threading.Thread(target=handle, args=(client, addr))
    client_handler.start()
