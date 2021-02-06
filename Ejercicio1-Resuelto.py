#Pedirle por pantalla nombre , horas trabajadas, precio por hora
#Devolver lo que cobrara esa persona ese mes


nombre=input("Dime tu nombre: ")
horasTrabajadas=int(input("¿Cuántas horas trabaste en el mes?: "))
precio = int(input("¿Cuál es el valor de la hora trabajada?: "))

salario= horasTrabajadas * precio

print("El empleado/a ", nombre, " este mes cobrara: ", salario)
