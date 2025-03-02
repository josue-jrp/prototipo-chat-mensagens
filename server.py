import socket
import threading
from estilos import Cores
import subprocess
import time
from class_server import Servidor, LogServer
import logs_server as log

def start():

    server = Servidor("192.168.15.11", 9090)
    server.ativar_server()
    print("servidor esperando conexões...")

    subprocess.Popen(["start", "cmd.exe", "/c", "cmd.exe", "/K", "python.exe", "logs_server.py"], shell=True)

    time.sleep(2)
    cliente = LogServer()
    cliente.conectar_com("192.168.15.11", 9000)

    parar_thread = threading.Event()

    def conectar():
        while True:
            conn, addr = server.accept()
            cliente.enviar_log(f" {Cores.VERDE}[ CONECTOU ]{Cores.RESET} {addr[0]}")

    def mostrar_conexoes():
        cliente.enviar_log("mostrar conexões ativas")
        #print("conexões ativas no momento:\n")
        dispositivos = server.mostrar_dispositivos_conectados()
        cliente.enviar_log(dispositivos)

    def enviar_msg(conn, addr):
    
        if len(server.dispositivos_conectados) != 0:

            try:
                msg = input()
                conn.send(msg.encode("utf-8"))
                mostrar_conexoes()

                # resposta recebe um retorno contendo informações do usuário que foi desconectado para que sejam passadas as informações para o servidor de logs
                resposta = server.desconectar_dispositivo(conn)
                cliente.enviar_log(resposta)

            except OSError:
                cliente.enviar_log(f"ocorreu um erro na comunicação. ")

        else:
            cliente.enviar_log("nenhum dispositivo está conectado ao servidor.")

    '''faz com que a função conectar - que fica escutando conexões - fique alerta sempre'''
    threading.Thread(target=conectar).start()
    return server, cliente







