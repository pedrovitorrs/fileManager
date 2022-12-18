from fastapi import FastAPI, Response
from Enum import *
import glob
import os
from dicttoxml import dicttoxml

app = FastAPI()

'''
    Retorna um [JSON, XML] com o nome de todos os arquivos.
'''
@app.get("/{diretorio:path}/{fileType}")
async def getFilesJSON(diretorio, fileType: FileType):
    listFiles = glob.glob("/" + diretorio + "/" + "*")
    
    if fileType is FileType.XML:
        return Response(content=dicttoxml(listFiles, custom_root="files", attr_type=False), media_type="application/xml")
    
    return {'files': listFiles}