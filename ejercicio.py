#ejercicio prueba
import numpy as np 
import random

licodigos=[]
linombres=[]
liproductos=[]

#listanum=[]
#licodigos1= np.array()

def generadordelistas(x,y,z,q):
    producto=[x,y,z,q]
    return producto

def a(nom):

    linombres.append(nom)


def codigo(dia):


    if dia == "lunes":
        listanum=[]
        a=random.randint(100000,999999)
        listanum.append(a)
        genco= f"{listanum}-LNT"
        licodigos.append(genco)
        print("su codigo es ",genco)
        
        return genco
        
    if dia == "martes":
        listanum=[]
        a =random.randint(100000,999999)
        listanum.append(a)
        genco= f"{listanum}-MTS"
        licodigos.append(genco)
        print("su codigo es ",genco)
        return genco
        
    if dia == "miercoles":
        listanum=[]
        a =random.randint(100000,999999)
        listanum.append(a)
        genco= f"{listanum}-MCS"
        licodigos.append(genco)
        print("su codigo es ",genco)
        return genco

    if dia == "jueves":
        listanum=[]
        a =random.randint(100000,999999)
        listanum.append(a)
        genco= f"{listanum}-JVS"
        licodigos.append(genco)
        print("su codigo es ",genco)
        return genco
    if dia == "viernes":
        listanum=[]
        a =random.randint(100000,999999)
        listanum.append(a)
        genco= f"{listanum}-VNS"
        licodigos.append(genco)
        print("su codigo es ",genco)
        return genco
    else:
        print("valor no valido")
        
i=True
while i :
    op=int(input("Para volver al menu, ingrese el numero 2: "))
    if op==2:
        i=False




#for i in range(3):
    
    
    #dia=str(input("ingrese el dia de hoy: ")).lower()
    #codigo(dia)
