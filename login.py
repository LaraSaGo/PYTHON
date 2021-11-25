'''from utilidades.mathtools import segura

login=dict()

login.update({"nombre":input('Introduce un nombre: ')})
login.update({"correo":input('Introduce un correo electrónico: ')})
passw=input('Introduce una contraseña: ')

if segura(passw):
    print("La contraseña es adecuada")
    login.update({"contraseña":passw})

    passw2=input('Introduce de nuevo la contraseña: ')

    if passw2 != passw:
        input("Las contraseñas no coinciden, vuelva a intentarlo")
    else: 
        print("Login completado")

else:
    print("La contraseña tiene que tener 8 caracteres, un número y una letra")
'''
from utilidades.mathtools import segura

login=dict()

login.update({"nombre":input('Introduce un nombre: ')})
login.update({"correo":input('Introduce un correo electrónico: ')})
passw=0

if segura(passw):
    print('La contraseña es adecuada')
    login.update({"contraseña":passw})