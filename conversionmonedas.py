change = dict()

c=1

while c<=3:

    divisa=input("Introduce una divisa: ")
    valor=float(input("Introduce el valor en euros: "))
    change.update({divisa: valor})
    c+=1

for x in change:
    print(x,change[x])


divisanueva=0
valornuevo=0

divisanueva=input("Introduce una divisa: ")
valornuevo=float(input("Introduce una cantidad: "))
print('Valor en euros: ', change[divisanueva]*valornuevo)

"""
if(divisanueva==divisa):
    print('valor en euros: ',valornuevo*valor)
else:
    print("Esa moneda no esta en la base de datos")"""