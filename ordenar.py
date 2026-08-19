import os
import shutil

pasta = r"C:\Users\albuquerque.felipe\Downloads"

arquivos = os.listdir(pasta)

for arquivo in arquivos:
    if arquivo.endswith(".pdf"):
        pasta_destino = os.path.join(pasta, "Documentos_PDF")
    elif arquivo.endswith(".png") or arquivo.endswith(".jpeg") or arquivo.endswith(".jpg"):
        pasta_destino = os.path.join(pasta, "Imagens")
    elif arquivo.endswith(".docx"):
        pasta_destino = os.path.join(pasta, "Documentos")
    elif arquivo.endswith(".xlsx"):
        pasta_destino = os.path.join(pasta, "Planilhas")
    else:
        continue
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)

    origem = os.path.join(pasta, arquivo)
    destino = pasta_destino

    shutil.move(origem, destino)
    print("movido", arquivo)

print("Pronto! Tudo separado.")

exit()
