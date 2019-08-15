#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import socket
import time

target_host = "free.idcfengye.com"
target_port = 11127

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

while 1:
    message = str(time.time())

    client.send(message.encode("utf-8"))

    response = client.recv(4096).decode("utf-8")

    print(response)

    time.sleep(2)
