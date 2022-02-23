# Calculadora para el indice de masa corporal
peso = float(input("Escriba su peso en Kg: "))
estatura = float(input("Digite su estatura en metros, ejemplo 1.65: "))
bmc = peso / estatura ** 2
print(type(bmc))

# en la siguiente linea se mostrará el resultado con muchos decimales
print("Su Índice de masa corporal es : " + str(bmc))

# Añadí otra forma de mostrar el resultado investigando como hacer dos print en la misma linea para mostrar el resultado solo con 2 decimales.
print("Su Indice de masa corporal es : ", end="")
print(round(bmc, 2))

# Trabajé condicionales investigando en la documentación para obtener el resultado esperado.
if bmc >= 0 and bmc <= 15.99:
    print("Usted tiene bajo peso corporal severo")
elif bmc >= 16.00 and bmc <= 16.99:
    print("Usted tiene muy bajo peso corporal")
elif bmc >= 17.00 and bmc <= 18.49:
    print("Usted tiene bajo peso corporal")
elif bmc >= 18.50 and bmc <= 24.99:
    print("Usted tiene un adecuado peso corporal")
elif bmc >= 25.00 and bmc <= 29.99:
    print("Usted tiene sobrepeso")
elif bmc >= 30.00 and bmc <= 34.99:
    print("Usted tiene obesidad leve")
elif bmc >= 35.00 and bmc <= 39.00:
    print("usted tiene obesidad media")
elif bmc >= 40.00:
    print("Usted tiene obesidad morbida")

# Espero que el código haya quedado bien y que no presnete errores en sintaxis y sea eficiente.
