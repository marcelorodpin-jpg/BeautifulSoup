# Autor: Marcelo Rodrigues
# Projeto: Raspagem de dados com Python

# Importando a biblioteca BeautifulSoup
from bs4 import BeautifulSoup

# Abrir o arquivo HTML e ler seu conteúdo
with open("index.html", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

# Leitura do html
site = BeautifulSoup(conteudo, "html.parser")

#Buscar todos os cards da pagina
produtos = site.find_all("div", class_="card")
# Loop para exibir os produtos encontrados
for produto in produtos:
    nome = produto.find("div", class_="nome").text.strip()
    preco = produto.find("div", class_="preco").text.strip()
    # Verifica se a palavra "Notebook" está no nome do produto
    if "Notebook" in nome:
        print('----------------------------------')
        print(f"O nome do produto é {nome} - Preço: {preco}")
        break  # Encerra o loop após encontrar o primeiro notebook
    