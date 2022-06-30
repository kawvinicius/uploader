
# ⚡️Uploader

O uploader foi desenvolvido para ser usado internamente na empresa Innova Empreendimentos. Basicamente o script utiliza a biblioteca PyDrive para enviar arquivos (boletos, comprovantes, notas fiscais) para seu respectivo lugar no google drive.


## Instalando as dependências 

O primeiro passo é instalar o pydrive através do pip. (Para isso, o python já deve estar instalado)

```bash
  pip install pydrive
```
    
Em seguida, é necessário buscar o json de validação do projeto e habilitar a API do Google Drive para ser acessada externamente pelo script (Tutorial disponível abaixo)

## Running Tests

Após tudo estar instalado e configurado, é necessário adicionar os arquivos na pasta ``` ./files``` e rodar o seguinte comando:  

```bash
  python uploader.py 
```


Para levar o arquivo para a página correta o programa leva em consideração a formatação da data (formato permitido: ```dd.mm.aa```) e a tag da operação. 

````OP07```` - Leva para a Operação 07

````OPAB01```` - Leva para a pasta do Areia Branca

````PG````  - Leva para Pouso das Garças

````AQBET```` - Pasta de construção do Lote 240

````AQTH```` - Aquisição de Tiago e Suzy

````CLOD```` - Área de Clodomiro (Nordeste)

```OP05``` - Operação 05

Obs: o caractere entre as datas pode ser alterado(por exemplo, pode ser trocado por uma ```/```), mas é importando manter as tags sempre da forma que estão listadas




## Referências

 - [Documentação do Pydrive](https://pythonhosted.org/PyDrive/)
 - [Resolver problemas com o pip](https://dicasdepython.com.br/resolvido-pip-nao-e-reconhecido-como-um-comando-interno/)
 - [Com pegar o json de validação e criar o projeto no Google Console](https://filipemot.medium.com/integra%C3%A7%C3%A3o-google-drive-com-python-e-enviar-o-link-pelo-gmail-5d048907976)

