"""4. Write a Python program which accepts the radius of a circle from the user and compute the area."""

from math import pi
r = float(input ("Introduce el radio : "))
print ("El area con radio igual a " + str(r) + " es: " + str(pi * r**2))



"""Otra forma"""

from math import pi
r = float(input ("Introduce el radio : "))
area= pi * r**2
print("El area del circulo es: ", area)


