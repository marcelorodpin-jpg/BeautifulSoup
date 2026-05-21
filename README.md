# 🛒 Raspagem de Dados de Produtos com Python

Este é um projeto simples e eficiente de Web Scraping (raspagem de dados) desenvolvido em Python. O script lê um arquivo HTML local, identifica produtos estruturados em "cards" e filtra especificamente os itens que contêm a palavra "Notebook" no nome, exibindo o resultado no terminal.

## 🚀 Tecnologias Utilizadas

* **Python 3**
* **BeautifulSoup4** (Biblioteca para extração de dados de arquivos HTML e XML)

## 📋 Pré-requisitos

Antes de executar o script, você precisa ter o Python instalado em sua máquina e a biblioteca BeautifulSoup4. 

Você pode instalar a biblioteca necessária executando o seguinte comando no terminal:

```bash
pip install beautifulsoup4
```

## 📂 Estrutura do Projeto

O projeto precisa de um arquivo HTML na mesma pasta do script para funcionar. A estrutura esperada para cada produto dentro do `index.html` deve seguir este padrão:

```html
<div class="card">
    <div class="nome">Notebook Gamer</div>
    <div class="preco">R\$ 4.500,00</div>
</div>
```

## 🔧 Como Executar

1. Clone este repositório ou baixe os arquivos.
2. Certifique-se de que o arquivo `index.html` está na mesma pasta do script Python.
3. Abra o terminal na pasta do projeto e execute:

```bash
python seu_script.py
```

## 🧑‍💻 Autor

* **Marcelo Rodrigues** - *Desenvolvimento inicial* 
