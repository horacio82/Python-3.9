#ENTRADA Y SALIDA POR TECLADO
#input
#print

nombre = input("¿Como te llamas?: ")
print("Bienvenido/a ", nombre)


precio = int(input("dime el precio del producto: "))
print("El producto vale ", precio)
print("Hola",nombre, "El producto vale ", precio)

print("Hola %s el producto vale %d." % (nombre, precio))
