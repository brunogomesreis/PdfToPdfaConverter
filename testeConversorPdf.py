import convertapi
from os import path
from glob import glob  
from setuptools import setup

setup(name='PdfConverterToPdfa',
      version='0.1',
      description='Bruno Reis Corporation',
      url='http://github.com/storborg/funniest',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      packages=['funniest'],
      install_requires=[
          'markdown',
      ],
      zip_safe=False)



def find_ext(dr, ext):
    return glob(path.join(dr,"*.{}".format(ext)))


def conversor (arquivos, destino):
    convertapi.api_secret = '4ZxTMFABZpapijXD'
    for arquivo in arquivos:
        convertapi.convert('pdfa', {
        'File': arquivo
        }, from_format = 'pdf').save_files(destino)
        print(arquivo + ":  Convertido")


print("Diretório de origem:")
origem = input()
print("Diretório de destino:")
destino = input()

arquivos = find_ext(origem,'pdf')
print ("Foram encontrados " + arquivos.__len__ + " arquivos")
conversor(arquivos,destino)

print("todos documentos foram convertidos")