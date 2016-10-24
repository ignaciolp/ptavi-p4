#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import socketserver
import sys


class SIPRegisterHandler(socketserver.DatagramRequestHandler):
    """
    Echo server class
    """

    def handle(self):
        informacion = {}
        self.wfile.write(b"Hemos recibido tu peticion")
        for line in self.rfile:
            print("Direccion IP y Puerto del cliente: ", self.client_address)
            print("El cliente nos manda ", line.decode('utf-8'))
            if line.decode('utf-8')[:8] == 'REGISTER': 
                informacion[line.decode('utf-8')[14:-9]]= self.client_address[0]
                print("El cliente nos manda ", line.decode('utf-8'))
                print('SIP/2.0 200 OK\r\n\r\n')
                print("diccionario", informacion)
  
if __name__ == "__main__":
    serv = socketserver.UDPServer(('', int(sys.argv[1])), SIPRegisterHandler)
    print("Lanzando servidor UDP de SIP")
    
    try:
        serv.serve_forever()
    except KeyboardInterrupt:
        print("Finalizado servidor")
