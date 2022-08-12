# README

Este projeto foi realizado com o intuito de produzir um artigo científico para a cadeira de Banco de Dados II. 
É possível visualizar os passos do fluxo através do arquivo pca_analysis.ipynb sem a necessidade de clonar nem executar o repositório, basta clicar no arquivo pelo próprio github.

## Requerimentos para a execução de todo fluxo:
* Sistema operacional unix
* Docker (com o seu usuário pertencendo ao grupo docker)
* python 3 instalado
* pipenv instalado
* ferramenta de visualização e execução de jupyter notebook (visual studio code com a extensão 'jupyter notebook' ou a própria ferramenta jupyter notebook)

## Execução:
1 - Dentro da pasta raiz, execute:

    .../BD-PCA-project/$ pipenv shell

2 - Em seguida, iniciaremos o ambiente postgresql docker executando o seguinte comando:

    .../BD-PCA-project/$ python3 postgres_prepare.py

3 - Agora será necessário abrir a ferramenta para acessar o jupyter notebook: pca_analysis.ipynb
