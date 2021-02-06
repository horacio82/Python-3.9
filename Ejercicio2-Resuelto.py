#Pedir el precio de un producto,
#Devolver el costo del iva de ese producto (21%)
#Devolver el valor total del producto incluido el iva
#usar cadenas con formato para devolver los resultados

precio = float(input("Dime el precio del producto: "))

iva = precio * 0.21
totalProducto = precio + iva

print("El costo del IVA de ese producto es %f." % iva)
print("El costo total del producto es de %f." % totalProducto)

#Con dos decimales:
print("El costo del IVA de ese producto es %.2f." % iva)
print("El costo total del producto es de %.2f." % totalProducto)
