#lista modificable
lista = ["benja morales", "hola", True, 1.53, 5]
#creando una tupla que no se puede modificar
tupla = ("benja morales", "hola", True, 1.53, 5)

lista[3] = "XD"
#tupla[3] = "XD" #esto no

#creando un conjunto (set) (no se accede a los elementos por indice, no se almacenan datos duplicados)
conjunto = {"benja morales", "hola", True, 1.53, 5}

# creando un diccionario
diccionario = {
    'nombre' : "benja"
    ,'edad': 24
    ,'altura': 3.56
    ,'dato_duplicado': "benja"
}
print(diccionario['altura'] + 2)
