# fileManager

## Objetivo

1. Implemente uma API RESTful que exponha as seguintes operações para manipulação de arquivos texto em
um determinado diretório pré-definido:

* GET /arquivos/json: retorna um JSON com o nome de todos os arquivos.
* GET /arquivos/xml: retorna um XML com o nome de todos os arquivos.
* GET /arquivos/nome_arquivo: retorna o conteúdo textual do arquivo texto de nome nome_arquivo.
* DELETE /arquivos: remove todos os arquivos.
* DELETE /arquivos/nome_arquivo: remove o arquivo de nome nome_arquivo.
* PUT /arquivos/nome_arquivo: atualiza o conteúdo do arquivo de nome nome_arquivo caso o
mesmo já exista, ou cria um arquivo com o conteúdo fornecido caso contrário.

## Instalação

```shell
uvicorn main:app --reload
```
