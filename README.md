# Organizador de Arquivos

Projeto em Python para organizar arquivos automaticamente por extensão.

## Funcionalidades

- Move arquivos PDF para a pasta `PDFs`
- Move arquivos PPK para a pasta `PPKs`
- Move imagens JPEG para a pasta `JPEGs`
- Move imagens PNG para a pasta `Imagens`
- Cria as pastas automaticamente caso não existam

## Tecnologias utilizadas

- Python
- os
- shutil

## Como executar

Clone o repositório:

```bash
git clone SEU_LINK_AQUI
```

Execute o script:

```bash
python organizador.py
```

## Exemplo

Antes:

``` id="2jj9zr"
Downloads/
    arquivo.pdf
    imagem.png
    chave.ppk
```

Depois:

``` id="kn91r8"
Downloads/
    PDFs/
    Imagens/
    PPKs/
```

## Objetivo do projeto

Praticar:
- manipulação de arquivos
- automação com Python
- lógica de programação
- uso de Git e GitHub
