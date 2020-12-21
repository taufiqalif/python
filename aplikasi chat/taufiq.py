#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 20:23:24 2020

@author: taufiq
"""

import socket

handlersocket = socket.socket()
serverIP = "127.0.0.1"
serverport = 2222

handlersocket.connect((serverIP,serverport))
print("terkoneksi ke server")

while True:
    message = handlersocket.recv(1024)
    print("pesan dari server: ")
    message = eval(input("pesan anda: "))
    handlersocket.send(message)
    pass