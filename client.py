#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Programa cliente UDP que abre un socket a un servidor
"""

import socket
import sys

# Constantes. Dirección IP del servidor y contenido a enviar

try:
    SERVER = sys.argv[1]
    PORT = sys.argv[2]
    METODO = sys.argv[3]
    US = sys.argv[4]
    CADUCA = sys.argv[5]
except:
    sys.exit("Usage: client.py ip puerto register sip_address expires_value")

LINE = ("REGISTER sip: " + US + "SIP/2.0\r\n Exipires: " + CADUCA + "\r\n\r\n")

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as my_socket:
    my_socket.connect((SERVER, int(PORT)))
    print("Enviando:", LINE)
    my_socket.send(bytes(LINE, 'utf-8') + b'\r\n')
    data = my_socket.recv(1024)
    print('Recibido -- ', data.decode('utf-8'))

print("Socket terminado.")
