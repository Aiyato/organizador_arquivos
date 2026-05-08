import os   
import shutil   
pasta = "C:/Users/brenn/Downloads"
arquivos = os.listdir(pasta)

tipos ={
    ".pdf": "PDFs",
    ".jpeg": "JPEGs",
    ".png": "Imagens",
    ".ppk": "PPKs",
}

for arquivo in arquivos:
    
    for extensao, nome_pasta in tipos.items():
        if arquivo.endswith(extensao):
            destino = pasta + "/" + nome_pasta
            os.makedirs(destino, exist_ok=True)
            origem = pasta + "/" + arquivo
            novo_destino = destino + "/" + arquivo
            shutil.move(origem, novo_destino)
            print(f"Arquivo {arquivo} movido!")
           