#Colecciones
#Listas

lista = [12, "mundo", True , "una oracion de letras", [1,"cadena",2]]

valor = lista[1]
print(valor)

#Muestra el elemento de una lista dentro de otra lista:
varAux = lista[4][2]
print(varAux)

#Cambia un elemento por otro:
lista[1]= 233
print(lista)

#Muestra el último elemento de atrás hacia adelante:
variable = lista[-2]
print(variable)

#Muestra los elementos desde la posición 0 hasta la 2:
variable = lista[0:3]
print(variable)

variable = lista[0:5:2]
print(variable)
