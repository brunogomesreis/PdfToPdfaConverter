import convertapi
from os import path
from glob import glob  

def find_ext(dr, ext):
    return glob(path.join(dr,"*.{}".format(ext)))


def conversor (arquivos, destino):
    convertapi.api_secret = '4ZxTMFABZpapijXD'
    for arquivo in arquivos:
        convertapi.convert('pdfa', {
        'File': arquivo
        }, from_format = 'pdf').save_files(destino)
        print(arquivo + ":  Converted")


print("Origin:")
origem = input()
print("Destiny:")
destino = input()

arquivos = find_ext(origem,'pdf')
conversor(arquivos,destino)

print("All files have been converted")