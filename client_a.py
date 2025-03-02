import socket
from estilos import Cores
from class_server import Cliente
import threading

try:
    
    client = Cliente()
    client.conectar_com("192.168.15.11", 9090)

    def receber_msg():
        while True:
            msg = client.socket.recv(1024).decode("utf-8")
        
            if not msg:
                continue

            elif msg == "close conection":
                
                raise

            print("servidor: ", msg)

    threading.Thread(target=receber_msg).start()

except TypeError as error:
    print(f"conexão com o servidor foi fechada. [ {error} ]")