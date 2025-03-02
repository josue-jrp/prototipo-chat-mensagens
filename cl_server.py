import socket
import os
import time
import threading
import subprocess
import server
from estilos import Cores
import logs_server as ls
import defs_uteis

ajustes_home = [{"online":False, "comand_line":True, "conversando":False, "servidor_log_ativado": False}]

opcoes = {"   ":f"{Cores.ROXO}CONSOLE DE OPÇÕES{Cores.RESET}","0": ["ficar online", "ficar offline"], "1": ["iniciar conversa (precisa estar online)","encerrar conversa"], "2": "tabela contatos salvos", "3":["usar linha de comando (usa essa...)", "alternar para interface amigável (só para bebês)"], "4": "listar conexões ativas"}
    
def apresentar_opcoes(opcoes):

    for key, value in opcoes.items():
        if key == "0":
            if ajustes_home[0]["online"]:
                print(f"{key} - {opcoes[key][-1]}")
            else:
                print(f"{key} - {opcoes[key][0]}")

        elif key == "1":
            if ajustes_home[0]["conversando"]:
                print(f"{key} - {opcoes[key][-1]}")
            else:
                if ajustes_home[0]["online"]:
                    print(f"{key} - {opcoes[key][0]}")
                else:
                    print(f"{Cores.CINZA}{key} - {opcoes[key][0]}", Cores.RESET)

        elif key == "2":
            print(f"{key} - {value}")

        elif key == "3":
            if ajustes_home[0]["comand_line"]:
                print(f"{key} - {opcoes[key][-1]}")
            else:
                print(f"{key} - {opcoes[key][0]}")

        elif key == "4":
            print(f"{key} - {value}")

        else:
            print(f"{key} {value}")

def executando_opcao_escolhida(op):

    if op == "0":
        if ajustes_home[0]["online"]:
            servidor.desativar_server()

        servidor, cliente = server.start()
        defs_uteis.msg_amigavel(f" {Cores.VERDE} SISTEMA ONLINE {Cores.RESET}")
        ajustes_home[0]["online"] = True
        ajustes_home[0]["servidor_log_ativado"] = True

        return servidor, cliente
    
    elif op == "1":
        return
    
    elif op == "2":
        return
    
    elif op == "3":
        return
    
    elif op == "4":
        return
    
    else:
        defs_uteis.msg_erro("essa opcao não está disponivel.")

def verificando_opcao_escolhida(opcao):
    '''verificando se a opção escolhida existe'''
    for chave, valor in opcoes.items():

        if chave == opcao:
            defs_uteis.msg_amigavel(f"usuário escolheu: {opcao}")
            servidor, cliente = executando_opcao_escolhida(opcao)
            return [servidor, cliente]

    else:
        defs_uteis.msg_erro("entrada inválida.")



while True:
    defs_uteis.limpar_console()
    apresentar_opcoes(opcoes)

    opcao_escolhida = input("\n> ")
    defs_uteis.limpar_console()
    log = verificando_opcao_escolhida(opcao_escolhida)

