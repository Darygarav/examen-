from ejercicio import *
import numpy
productos=[]

#menu 
s=True
while s:
    print("------bienvenido al menu de la bodega------")
    print("1. Registrar Producto")
    print("2. Buscar Producto")
    print("3. Imprimir catalogo de Productos")
    print("4. Salir")
    try:
        
        op=int(input("Ingrese una opcion: "))
        if op>=1 and op<=4:
            if op==1:
                print("----Guardado de datos de productos----")
                dia=str(input("Ingrese el día de hoy: "))
                codigodia=codigo(dia)
                nombrep=str(input("Ingrese el nombre del producto: "))
                if len(nombrep)>7:
                    precio=int(input("Ingrese el precio del producto: "))
                    if precio>=0:
                        stock=int(input("Ingrese el stock del producto: "))
                        if stock>0:
                            lis=generadordelistas(codigodia,nombrep,precio,stock)
                            productos.append(lis)
                        else:
                            print("El stock tienen que ser mañor a 0")   
                    else:
                        print("El precio tienen que ser mañor a 0")        
                else:
                    print("Cantidad de caracteres no valida, tienen que ser mañor a 7")
                
            if op==2:
                bus=str(input("ingrese el codigo de su producto: "))
                y=0
                while y in range(len(productos)):
                    
                    if productos[y][0]==bus:
                        if productos [y][3]>0:
                            print(f"Numero de parte: {productos[y][0]}")
                            print(f"Nombre del producto: {productos[y][1]}")
                            print(f"Precio del producto: {productos[y][2]}")
                            exit()
            if op==3:
                s=False
            if op==4:
                print("Hasta luego")
                print("Programa echo por: Darío García")
                print("Version 1.0")
                s=False
        else:
            print("Porfavor ingrese un valor entre 1 a 4 ")
    except ValueError:
        print(" Valor no valido")

"""
lista =[['123612JDHRS','Servidor Huawei',220000]]
print(lista[0][0])

numeroParte=str(input("ingrese un numero: "))
nombre=str(input("ingrese un nombre: "))
precio=int(input("ingrese un precio: "))
producto = [numeroParte,nombre,precio]
lista.append(producto)
print(lista[1][0])
"""
