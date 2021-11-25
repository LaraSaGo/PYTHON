"""3. Write a Python program to guess a number between 1 to 9. Go to the editor
Note : User is prompted to enter a guess. If the user guesses wrong then the 
prompt appears again until the guess is correct, on successful guess, user will
 get a "Well guessed!" message, and the program will exit."""


import random

a = random.randint(1, 10)
b = 0

while a!=b:
    b= int(input("Introduce un numero para adivinarlo: "))
print("Correcto!")

 