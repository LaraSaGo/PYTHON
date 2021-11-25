'''3. Write a Python program to display the current date and time.'''

import datetime
fecha = datetime.datetime.now()
print ("Hora actual: ")
print (fecha.strftime("%Y-%m-%d %H:%M:%S"))

