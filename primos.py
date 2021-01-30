#from timeit import default_timer as timer
import datetime

numero = int (input("Ingrese hasta que número busca números primos: "))

"Entrega una lista de números primos entre 2 y numero."
cantidad = 0
calculos = 0
#start = timer()
tiempo_inicio = datetime.datetime.now()
for i in range(1, numero+1, 2):
    # Bajando los cálculos a la mitad ya que los números primos son impares
    # A excepción del 2
    if i == 1:
        i = 2
    contador = 0
    for x in range(1, i+1):
         calculos += 1 # Contador que cuenta la cantidas de cálculos realizados
         if i % x == 0:
             contador += 1

             if contador == 2:
                  print(i, end=" ")
                  cantidad += 1 # Contador que cuenta la cantidad de 
                                # Números primos encontrados
    
              
#end = timer()
tiempo_termino = datetime.datetime.now()
print('\n\n',cantidad, 'números primos entre 2 y', numero, '.',
             '\n', calculos, 'cálculos.', 
             '\nEn:',tiempo_termino - tiempo_inicio, 'segundos y microsegundos.')

