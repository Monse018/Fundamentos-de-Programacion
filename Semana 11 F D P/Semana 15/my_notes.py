#Abrir el documento
"""
file = open("my_notes.txt", "r")
 print(file)
lineas=file.readlines()
 print=(lineas)
file.close() # Cerrar el documento
"""

#Abrir y cerrar el documento automaticamente en modo lectura
with open("my_notes.txt","r") as archivo:
    lineas = archivo.readlines()
     #print(lineas)

# Documento con salto de lineas
for l in lineas:
   print(l.replace("\n"," "))

#Documento sin salto de lineas
with open("my_notes.txt","r") as archivo:
    contenido=archivo.read()
    lineas = contenido.split("\n")
    print(lineas)
