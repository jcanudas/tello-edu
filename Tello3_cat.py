#
# Demostació del Control del dron Tello amb Python3 
#
# http://www.ryzerobotics.com/
#
# 1/1/2018 (traducció 22/05/24)

import threading 
import socket
import sys
import time


host = ''
port = 9000
locaddr = (host,port) 


# Create a UDP socket
# Les rutines de socket UDP permeten una comunicació IP senzilla mitjançant el protocol de datagrama d'usuari (UDP)
# El protocol de datagrama d'usuari (UDP) s'executa a la part superior del protocol d'Internet (IP)
# i es va desenvolupar per a aplicacions que no requereixen funcions de fiabilitat,
# reconeixement o control de flux a la capa de transport.

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

# Aquest funció ens permet rebre informació del dronper saber si ha rebut la instrucció correctament
def recv():
    count = 0
    while True: 
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break

# Mostra en pantalla algunes de les instruccions que es poden utilitzar

print ('\r\n\r\nTello Python3 Demo.\r\n')

print ('Tello: command takeoff land flip forward back left right \r\n       up down cw ccw speed speed?\r\n')

print ('end -- quit demo.\r\n')


# Executa la recepció de dades del dron en paral·lel 
#recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()

# Bucle per enviar les dades del dron introduides des del teclat

while True: 

    try:
        msg = input("");

        if not msg:
            break  

        if 'end' in msg:
            print ('...')
            sock.close()  
            break

        # envia la dada o comanda
        msg = msg.encode(encoding="utf-8") 
        sent = sock.sendto(msg, tello_address)
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()  
        break



