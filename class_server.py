import socket
import threading
from estilos import Cores

class Servidor:
    def __init__(self, ip, porta, nome = "server"):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.bind((ip, int(porta)))
            self.live = False
            self.dispositivos_conectados = []

        except TypeError as error:
            print(f"não foi possível criar um socket de servidor. [ {error} ]")

    def ativar_server(self):
        self.socket.listen()
        self.live = True

    def desativar_server(self): 
        if self.live:
            self.socket.close()
            self.live = False
           
        else:
            print("o server ainda não está ativo. Não é possivel desativar.")

    def accept(self):
        if self.live:
            conexao, addr = self.socket.accept()
            self.dispositivos_conectados.append((conexao, addr))    
            return conexao, addr
        
        else:
            return "O servidor ainda não está ativo."

    def desconectar_dispositivo(self, conn):
        self.mostrar_dispositivos_conectados()

        if len(self.dispositivos_conectados) != 0:
            try:
                desconectar = int(input("digite o indice do dispositivo que deseja desconectar do servidor: "))
                
            except ValueError:
                print("digite um valor numérico, por favor! [ erro de valor ]")
                return

            if desconectar > len(self.dispositivos_conectados) -1 or desconectar < 0:
                return "indice que você forneceu não existe na lista de dispositivos conectados! [ erro ] "

            else:
                conexao = self.dispositivos_conectados.pop(desconectar)
                conn.send(b"close conection")
                conexao[0].close()
                return f"{Cores.VERMELHO}[ DESCONECTADO ]{Cores.RESET} {conexao[1][0]} {conexao[0]}"

        else:
            print("não há nenhum dispositivo para ser desconectado!")
                

    def mostrar_dispositivos_conectados(self):
        dispositivos = []
        if len(self.dispositivos_conectados) != 0:
            for indice, dispositivo in enumerate(self.dispositivos_conectados): 
                dispositivos.append(f"indice: {indice}, socket: {dispositivo[0]}, ip: {dispositivo[1][0]}, porta: {dispositivo[1][1]}\n")
                dispositivos = " ".join(dispositivos)
                return dispositivos

        else:
            return "ainda não há nenhum dispositivo conectado a este servidor."

class Cliente():
    def __init__(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.conected = False
            
        except TypeError as error:
            print(f"não foi possível criar um socket de cliente: [ {error} ]")

    def conectar_com(self, ip, porta):
        try:
            self.socket.connect((ip, int(porta)))
            print("cliente conectado. ")
            self.conected = True

        except TypeError as error:
            print(f"não foi possível conectar. [ {error} ]")

    def desconectar_do_server(self):
        if self.conected:
            self.socket.close()
            self.conected = False

        else:
            print("o cliente já está desconectado do servidor")

    def esta_conectado(self):
    
        if self.conected:
            erro = self.socket.getsockopt(socket.SOL_SOCKET, socket.SO_ERROR)
            print(erro)

            if erro == 0:
                # erro retornando 0 significa que a conexão não possui erros.
                return "OK"
            
            else:
                self.conected = False
                return "close connection"
            
        else:
            return "OK"
        

class LogServer(Cliente):
    def __init__(self):
        super().__init__()

    def enviar_log(self, msg):
        try:
            self.socket.send(msg.encode("utf-8"))

        except TypeError as error:
            print(f"[ erro ] tipo de erro: [ {error} ]")

    ''' depois podemos implementar um método que escreve os logs em um arquivo txt (por exemplo)'''


