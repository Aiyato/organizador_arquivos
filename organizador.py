import os   
import shutil   
pasta = "C:/Users/brenn/Downloads"
arquivos = os.listdir(pasta)
for arquivo in arquivos:
    if arquivo.endswith(".pdf"):
        destino = pasta + "/PDFs"
        os.makedirs(destino, exist_ok=True)

        origem = pasta + "/" + arquivo
        novo_destino = destino + "/" + arquivo
        shutil.move(origem, novo_destino)

        print(f"Arquivo {arquivo} movido!")
    
    elif arquivo.endswith(".ppk"):
        destino = pasta + "/PPKs"
        os.makedirs(destino, exist_ok=True)

        origem = pasta + "/" + arquivo
        novo_destino = destino + "/" + arquivo
        shutil.move(origem, novo_destino)

        print(f"Arquivo {arquivo} movido!")

    elif arquivo.endswith(".jpeg"):
        destino = pasta + "/JPEGs"
        os.makedirs(destino, exist_ok=True)

        origem = pasta + "/" + arquivo
        novo_destino = destino + "/" + arquivo
        shutil.move(origem, novo_destino)

        print(f"Arquivo {arquivo} movido!")

    elif arquivo.endswith(".png"):
        destino = pasta + "/Imagens"
        os.makedirs(destino, exist_ok=True)

        origem = pasta + "/" + arquivo
        novo_destino = destino + "/" + arquivo
        shutil.move(origem, novo_destino)

        print(f"Arquivo {arquivo} movido!")
