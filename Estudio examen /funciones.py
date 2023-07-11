

import random 
import numpy as np
lidatos=[["dario",2078,1212,"chile",36], ["feli", 2178,9540,"chile",37]]
liasientos_normi=[1,2,3,4,5,6,7,'x','x',10,11,12,'x','x','x',16,'x',18,19,20,21,22,23,24,25,26,27,'x',29,30]
liasientos_vip=['x',32,33,34,35,36,'x',38,'x',40,41,'x']
liasientos=[]
liasientos.extend(liasientos_normi)
liasientos.extend(liasientos_vip)
asiento_normal=78900
asiento_vip=240000



def asientos ():
    ii=True
    while ii:
                    print ("-----Asientos disponibles-----")
                    print(liasientos)
                    try:
                        op2=int(input("Para volver al menu, ingrese el numero 2: "))
                    
                        if op2>0:
                            if op2==2:
                                ii=False
                    except ValueError:
                        print("Valor no valido")



def compra_asientos ():
    asiento_normal=78900
    asiento_vip=240000

    print ("-----Compra de asientos-----")
    nom=str(input("Ingrese su nombre: ")).lower()
    rut=int(input("Ingrese su rut: "))
    telefono=int(input("Ingrese su telefono: "))
    
        
    banco=str(input("Ingrese su banco: ")).lower()
    tipobanco=str(input("¿Es usted usuario de Banco Duoc? ingrese si o no: ")).upper()
    if tipobanco==("si").upper(): 
        asiento_normal=78900*0.85
        asiento_vip=240000*0.85
        
    lugar=int(input("Escoga un asiento:  "))
    if lugar>=1 and lugar<=30:
        if lugar in liasientos_normi:
            print(f"El valor del asientos es de: {asiento_normal} ")
            datos=[nom,rut,telefono,banco,lugar]
            lidatos.append(datos)
            for i in range(len(liasientos_normi)):
                if liasientos_normi [i]==lugar:
                        liasientos_normi.remove(lugar)
                        liasientos_normi.insert(i,"x")
                        print(lidatos)
                        print(liasientos_normi)
        else:
            print("El asiento seleccionado, no esta disponible")
    if lugar>=31 and lugar<=36:
        if lugar in liasientos_vip:
            print(f"El valor del asientos es de: {asiento_vip} ")
            datos=[nom,rut,telefono,banco,lugar]
            lidatos.append(datos)
            for i in range(len(liasientos_vip)):
                if liasientos_vip [i]==lugar:
                        liasientos_vip.remove(lugar)
                        liasientos_vip.insert(i,"x")
                        print(lidatos)
                        print(liasientos_vip)
        else:
            print("El asiento seleccionado, no esta disponible")
            

def anular_pasaje ():
    print ("-----Anular vuelo-----")
    anrut=int(input("Ingrese su numero de rut: "))
    try:
        for e in range(len(lidatos)):
            if lidatos[e][1] == anrut:
                del lidatos[(e)]
                print("Datos eliminados")
                break
    except ValueError:
        print("valor no valido")
        
    anpasaje=int(input("Ingrese su numero de asiento: "))
    try:
        if anpasaje>=1 and anpasaje<=42:
            if not anpasaje in liasientos:
                for a in range(len(liasientos)):
                    if a==anpasaje:
                        liasientos.pop(a-1)
                        print(liasientos)
                        liasientos.insert(a-1,anpasaje)
                        print(liasientos)
                        print("Vuelo anulado")
            else:
                print("El asiento ingresado no se puede anular")

            
    except ValueError:
        print("Valor ingresado no valido")
        
def mod_datos ():
    print ("-----Modificacion de datos del pasajero-----")
    asire=int(input("Ingrese su numero de asiento: "))
    rutre=int(input("Ingrese su numero de rut: "))
    try:
        for x in range(len(lidatos)):
            if lidatos [x][4]==asire:
                print("asiento encontrado")
                for i in range(len(lidatos)):
                    if lidatos [i][1]==rutre:
                        print("rut encontrado")
                        print("-----Modificacion de datos-----")
                        print("Datos a modificar: ")
                        print("1.- Modificar nombre pasajeros ")
                        print("2.- Modificar telefono ")
                        op1=int(input("Ingrese su opcion: "))
                        try:
                            if op1==1:
                                nomc=str(input("Ingrese su nuevo nombre: "))
                                for x in range(len(lidatos)):
                                    if lidatos [x][1]==rutre:
                                        lidatos[x][0]=nomc
                                        print(lidatos)
                                        
                                        print("Nombre modoficado")
                                        break
                            if op1==2:
                                telc=int(input("Ingrese su nuevo telefono: "))
                                for x in range(len(lidatos)):
                                    if lidatos [x][1]==rutre:
                                        lidatos[x][2]=telc
                                        print(lidatos)
                                        
                                        print("telefono modoficado")
                                        break
                            
                            else:
                                print("esa opcion no existe")
                        except ValueError:
                            print("Ingrese un numero")
            
            
            
    except ValueError:
        print("Valor ingresado no valido")
#anular_pasaje()
#comprea_asientos()



