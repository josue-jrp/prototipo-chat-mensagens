import subprocess
from estilos import Cores

def limpar_console():
    subprocess.run(["cls"], shell=True)

def msg_amigavel(msg):
    print(f"{Cores.VERDE}[*]{Cores.RESET} {msg}")

def msg_erro(msg):
    print(f"{Cores.VERMELHO}[*]{Cores.RESET} {msg}")