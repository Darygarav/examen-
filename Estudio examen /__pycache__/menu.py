





import random 
from funciones import *
import numpy as np



i=True
while i:
    print("------Bienvenido a Vuelos-Duoc------")
    print("1. Ver asientos disponibles \n2. Comprar asiento \n3. Anular vuelo \n4. Modificar datos de pasajero \n5. Salir")
    try:
        op=int(input("Ingrese la acción que quiere realizar: "))
        if op>=1 and op<=5:
            if op==1:
                asientos()
                    
            if op==2:
                compra_asientos()
            if op==3:
                anular_pasaje()
                
            if op==4:
                mod_datos()
            if op==5:
                print(" ")
                print ("-----Adios-----")
                print(" ")
                exit()
        else:
            print("Porfavor ingrese un numero entre 1 y 5")
    except ValueError:
        print("Valor no valido, ingrese solo numeros")