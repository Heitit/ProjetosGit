# Calculadora Equação de Segundo Grau

import math

a = int(input('Insira o valor de "a": '))
b = int(input('Insira o valor de "b": '))
c = int(input('Insira o valor de "c": '))

delta = (b**2) - (4*a*c)

if delta == 0:
    resultado = (-b + math.sqrt(delta)) / (2*a)
    print ('A raiz dupla desta equação é', resultado)
elif delta < 0:
    print ('Esta equação não possui raízes reais')
else:
    resultado1 = (-b + math.sqrt(delta)) / (2*a)
    resultado2 = (-b - math.sqrt(delta)) / (2*a)
    resultados = sorted([resultado1, resultado2])
    print ('As raízes da equação são', resultados)