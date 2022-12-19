from fastapi import FastAPI, Response, HTTPException
from Enum import *
import glob
import os
from dicttoxml import dicttoxml
from Model import *

app = FastAPI()

'''
    Retorna [JSON, XML] com o nome de todos os arquivos do diretório especificado.
'''
@app.get("/file/{diretorio:path}/{fileType}")
async def getFiles(diretorio: str, fileType: FileType):
    listFiles = glob.glob("/" + diretorio + "/" + "*")

    if fileType is FileType.XML:
        return Response(content=dicttoxml(listFiles, custom_root="files", attr_type=False), media_type="application/xml")

    return {'status': 'ok', 'files': listFiles}

'''
    Retorna o conteúdo textual do arquivo texto de nome nome_arquivo.
'''
@app.get("/content/{diretorio:path}")
async def getFileContent(diretorio: str):
    try:
        file = open("/" + diretorio, 'r')
        content = file.read()
        return {'status': 'ok', 'fileContent': content}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail="Item not found")

'''
    Remove todos os arquivos do diretorio especificado.
'''
@app.delete("/{diretorio:path}/files")
async def deleteFiles(diretorio: str):
    try:
        for file in os.listdir("/" + diretorio):
            os.remove(os.path.join("/" + diretorio, file))
        return {'status': 'ok'}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail="Item not found")
    
'''
    Remove o arquivo do diretorio especificado.
'''
@app.delete("/{diretorio:path}/file")
async def deleteFile(diretorio: str):
    try:
        os.remove("/" + diretorio)
        return {'status': 'ok'}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail="Item not found")

'''
    Atualiza o conteúdo do arquivo de nome especificado caso o mesmo já exista, ou cria um arquivo com o conteúdo fornecido caso contrário.
'''
@app.put("/{diretorio:path}/file")
async def updateFile(diretorio: str, item: Item):
    try:
        with open("/" + diretorio, "w") as file:
            file.write(item.content)
        return {'status': 'ok'}
    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, detail="Failed to write file.")
