"""Write a Python script to print a dictionary where the keys are numbers
between 1 and 15 (both included) and the values are square of keys.
Sample Dictionary
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100,
11: 121, 12: 144, 13: 169, 14: 196, 15: 225}"""

""""MI FORMA DE HACERLO
cubos = dict()
c=1

while c<=15:
    keys=c
    cubo=c**3
    cubos.update({keys:cubo})
    c+=1

for x in cubos:
    print(x,cubos[x])
"""

"""LA FORMA DE LA PÁGINA
d=dict()
for x in range(1,16):
    d[x]=x**2
print(d)"""

"""INTERCAMBIANDO VALORES
cuadrado = dict()

inicio=int(input('Introduce desde que valor quieres que empiece a calcular los cuadrados: '))
final=int(input('Introduce en que valor quieres que acaben los cuadrados: '))
aux=0

if(inicio<final):

    for valor in range(inicio,final+1):
        cuadrado[valor]=valor**2

    for valor in cuadrado:
        print(valor,cuadrado[valor])

else: 
    inicio=aux
    aux=final
    final=inicio
    for valor in range(inicio,final+1):
            cuadrado[valor]=valor**2

    for valor in cuadrado:
        print(valor,cuadrado[valor])
"""

"""PREGUNTANDO HASTA QUE EL VALOR INICIAL SEA MENOR"""
cuadrado = dict()
solicitar=1

while solicitar:
    inicio=int(input('Introduce desde que valor quieres que empiece a calcular los cuadrados: '))
    final=int(input('Introduce en que valor quieres que acaben los cuadrados: '))
    if inicio<=final:
        solicitar=0
    else:
        print('Teclee el valor inicial menor que el final')

    for valor in range(inicio,final+1):
            cuadrado[valor]=valor**2

    for valor in cuadrado:
        print(valor,cuadrado[valor])
