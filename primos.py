from utilidades.mathtools import isPrime
from utilidades.mathtools import factorial

x=int(input('Introduce un número para saber si es primo o no: '))

if isPrime(x):
    print("El numero es primo")
else:
    print("El numero no es primo")
for f in range(1,13):
    print(f,factorial(f))    