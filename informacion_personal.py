# Crear un Diccionario
informacion_personal = {
"Nombre": "Juan Pablo Rodríguez",
"Edad": 38,
"Ciudad": "Quito",
"Profesion": "Doctor"
}

# Modificar la ciudad
informacion_personal["ciudad"] = "Guayaquil"

# Agregar teléfono si no existe
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0985829645"

# 4. Eliminar una Clave
del informacion_personal["Edad"]

# 5. Imprimir el Diccionario Final
print("Diccionario de Informacion Personal:")
print(informacion_personal)