#Metodos con Cadenas

cadena="hola mundo"
resultado= cadena.capitalize()
print(resultado)

cadena="hola mundo"
resultado= cadena.count('o')
print("count ", resultado)

cadena="hola mundo"
resultado= cadena.endswith('o')
print("final de cadena ", resultado)

cadena="hola mundo"
resultado= cadena.find('m')
print("find", resultado)

cadena="12121212"
resultado= cadena.isnumeric()
print("es numerica ", resultado)

cadena="HOLA pePito"
resultado= cadena.lower()
print("pasa a minuscula ", resultado)

cadena="HOLA pePito"
resultado= cadena.replace('pePito','mundo')
print("reemplazar ", resultado)

cadena="  HOLA mundo     "
resultado= cadena.strip()
print(resultado)

cadena="  HOLA mundo     "
resultado= cadena.upper()
print(resultado)

cadena="HOLA mundo"
resultado= cadena.zfill(20)
print(resultado)
