import socket
from datetime import datetime
from estilos import Cores
from class_server import Servidor
import time
import subprocess

if __name__ == "__main__":
    try:

        server_log = Servidor("0.0.0.0", 9000)
        server_log.socket.listen(1)
        print("servidor de logs esperando conexão...")
        conn, addr = server_log.socket.accept()

        print("== logs do servidor ==".upper())

        while True:
        
            msg = conn.recv(1024).decode("utf-8")
            if not msg:
                continue

            agora = datetime.now()
            hora = agora.hour
            minuto = agora.minute
            segundo = agora.second

            print(f"{Cores.CINZA}[ {hora}:{minuto}:{segundo} ]{Cores.RESET} {msg}")

    except TypeError as error:
        print(f"[ erro ] do tipo: [ {error} ]")





