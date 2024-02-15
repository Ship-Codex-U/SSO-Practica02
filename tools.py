import os
import shutil
import random
import string

def normPath(ruta):
    return os.path.normpath(ruta)  # Normalizar la ruta

def processLine(line):
    newLine = ""
    
    for character in line:
        if(character.isdigit()):
            newLine += random.choice(string.ascii_uppercase)
            
        elif(character.isalpha()):
            newLine += random.choice(string.digits)
    
    return newLine


def processFile(inputFile, outputFile):
    # Abrir archivos de entrada y salida
    with open(inputFile, "r") as IF, open(outputFile, "w") as OF:

        for line in IF:
            newLine = processLine(line)# --------------------------------------------------------------------------------------> Mandamos el renglon a procesar
            OF.write(newLine)
            

def processDir(source, destination):
    try:
        # Verificar si la ruta proporcionada es una carpeta
        if not os.path.isdir(source):
            print(f"Error: {source} no es una carpeta válida.")
            return

        # Crear el directorio de la copia si no existe
        if not os.path.exists(destination):
            os.makedirs(destination)

        # Copiar todo el contenido de la carpeta origen al destino
        for name in os.listdir(source):
            absoluteSourcePath = os.path.join(source, name)
            absoluteDestinationPath = os.path.join(destination, name)

            # Si es una carpeta, llamar recursivamente a esta función
            if os.path.isdir(absoluteSourcePath):
                processDir(absoluteSourcePath, absoluteDestinationPath) # ------------------------------------------------------> Mandamos la carpeta a procesar
                
            else:
                shutil.copy2(absoluteSourcePath, absoluteDestinationPath)  # Utilizamos shutil.copy2 para conservar metadatos
                
                newNameFile = "new_" + name #Nuevo nombre del archivo
                newAbsoluteDestinationPath = os.path.join(destination, newNameFile) #Nueva ruta de destino con el nuevo nombre
                
                processFile(absoluteDestinationPath, newAbsoluteDestinationPath) # ----------------------------------------------> Mandamos el archivo a procesar
                
                os.remove(absoluteDestinationPath) #Removemos el archivo original de la carpeta copia
                os.rename(newAbsoluteDestinationPath, absoluteDestinationPath) #Renombramos el archivo para dejarlo con el nombre del archivo original

    except Exception as e:
        print(f"Error al copiar contenido de {source} a {destination}: {e}")