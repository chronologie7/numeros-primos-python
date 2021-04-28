import math
import time

primoNumero = 0
calculos = 0
esPrimo = True

numero = int(input("Ingrese hasta que número busca números primos: "))

tiempoInicio = time.time()

primoNumero += 1

print(primoNumero, "-", 2)

for numeroActual in range(3, numero, 2):
    for divisor in range(2, int(math.sqrt(numeroActual)) + 1):
        calculos += 1
        if numeroActual % divisor == 0:
            esPrimo = False
            break
    if esPrimo:
        primoNumero += 1
        print(primoNumero, "-", numeroActual)
    esPrimo = True
print("Calculos:", calculos)
print("Tiempo:", time.time() - tiempoInicio)
