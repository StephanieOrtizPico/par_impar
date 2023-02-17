# Programa para determinar si un nùmero es par o impar

# input
x = int(input("Ingresa un nùmero: "))

# processing
r = x%2

# output
if r & 1 == 0:
    print("El numero es par")
else: 
    print("El numero es impar")
