from pathlib import Path
import json
import time

caminho = Path("teste.json")
conteudo = ["configuração 1", "configuração 2", "configuração 3", "configuração 4"]
dados = []

for item in conteudo:
    dados.append(item)

dados = " ".join(dados)
dados = dados.replace(",", "\n")

arquivo_json = json.dumps(dados)

caminho.write_text(arquivo_json)

time.sleep(2)

path = Path("teste.json")
formatado = path.read_text()
arquivo = json.loads(formatado)

print(arquivo)

