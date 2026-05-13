import os
from os import path
pasta = input("Digite o caminho da pasta: ")
arquivos = os.listdir(pasta)
total= len(arquivos)
print(f"Total de arquivos: {total}")

for arquivo in arquivos:
    nome,extensao = path.splitext(arquivo)

    print(extensao)

contagem = {}

for arquivo in arquivos:
    nome,extensao = path.splitext(arquivo)

    if extensao in contagem:
        contagem[extensao] += 1
    else:
        contagem[extensao] = 1
print(contagem)