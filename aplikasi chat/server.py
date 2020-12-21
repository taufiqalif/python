#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 13:22:44 2020

@author: taufiq
"""
import socket

listenersocket = socket.socket()
serverIP = "0.0.0.0"
serverport = 2222
listenersocket.bind((serverIP,serverport))
listenersocket.listen(0)
print("server siap nemerima cliant")
while True:
    handlersocket, addr = listenersocket.accept()
    print("Alamat baru terkoneksi",addr)
    while True:
        message = eval(input("Pesan anda: "))
        a = str(message)
        handlersocket.send(a)
        message = handlersocket.recv(1024)
        print("Pesan masuk: ")
        pass
    pass