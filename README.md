# Organizador de Arquivos

Este script de automação foi desenvolvido para organizar arquivos de uma pasta específica, movendo-os para subpastas categorizadas.

## O que ele faz?

O script varre uma pasta específica e os move para suas respectivas subpastas

* Arquivos terminados em ".pdf" vão para a pasta "Documentos_PDF"
* Arquivos terminados em ".png", ".jpeg" e "jpg" vão para a pasta "Imagens"
* Arquivos terminados em ".docx" vão para a pasta "Documentos"
* Arquivos terminados em ".xlsx" vão para a pasta "Planilhas"

## Como usá-lo?

1) Instale e configure o Python em seu computador.
2) Baixe o arquivo `ordenar.py`.
3) Agora, para organizar outra pasta, abra o arquivo `ordenar.py` e mude o texto da variável "pasta" para o caminho que você quer. Por exemplo, você quer organizar uma pasta "Artigos", então você reestrutura seu caminho, observe: `pasta = r"C:\Users\User\Artigos"`. Há também de reescrever o caminho com o seu nome de usuário, veja: `pasta = r"C:\Users\albuquerque.felipe\Artigos"`.
4) Execute o script no terminal.
