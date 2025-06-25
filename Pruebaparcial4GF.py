def menu():
    print('Menú De compra para Avengers ahora si te fuiste Thanos')
    print('~'*20)
    print("""
    1.- Comprar entrada.
    2.- Buscar Comprador.
    3.- Cancelar Compra.
    4.- Salir.""")
    op = input('Ingrese su opción: ')
    return op

def validar_codigo_verificacion(codigoverificacion):
    Mayuscula = any(c.isupper() for c in codigoverificacion)
    Numero = any(c.isdigit() for c in codigoverificacion)
    Sin = ' ' not in codigoverificacion
    return len(codigoverificacion) >= 6 and Mayuscula and Numero and Sin
    



def Comprar_entrada(diccentrada):
        while True:
            nombre = input('Ingrese nombre del comprador: ')
            if nombre.replace(' ','').isalpha():
                break
            else:
                print('El nombre solo debe contener letras. Intente nuevamente')
        
        while True:
            tipo = input('Ingrese tipo de entrada [G / V]: ').upper()
            if tipo == 'G' :
                break
            elif tipo == 'V' :
                break
            else:
                print('Tipo invalido .Intente Nuevamente')
        while True:
            codigoVerifcacion = input('Ingrese código de verificación: ')
            if validar_codigo_verificacion(codigoVerifcacion):
                break
            else:
                print('Codigo no valido. Debe tener minimo 6 caracteres, al menos 1 mayuscula, 1 numero y sin espacios, intente otra vez.')
        diccentrada[nombre] = [tipo, codigoVerifcacion]  
        
        print(f'Codigo validado ¡Entrada registrada con exito! {nombre}')      
        return diccentrada

def cancelar_entrada(diccentrada):
    nombre = input('Ingrese el nombre del titular a cancelar: ').strip()
    if nombre in diccentrada:
        diccentrada[nombre][0]
        del diccentrada[nombre]
        print('¡Compra cancelada correctamente!')
    else:
        print(f'No se encuentra el nombre con una entrada comprada ')
    return diccentrada 
def buscar_(diccentrada):
    if not diccentrada:
        print("No hay usuarios guardados.")
        return
    
    nombre = input("Ingrese el nombre a buscar: ").strip()
    
    if nombre in diccentrada:
        print(f"usuario encontrado: {nombre}")
        print(f"Tipo de entrada: ", diccentrada[nombre][0], "Codigo de verificacion: ", diccentrada[nombre][1])
    else:    
        print(" user no encontrado.")

    
import Pruebaparcial4GF as fc

opcion = ''
usuarios = {}

while opcion != '4':
    opcion = fc.menu()
    if opcion == '4':
        print('Programa Terminado.')
    elif opcion == '1':
        print(' Nueva Compra')
        usuarios = fc.Comprar_entrada(usuarios)
        print(usuarios)
    elif opcion == '2':
        print('buscar comprador')
        fc.buscar_(usuarios)
    elif opcion == '3':
        print('Cancelar Compra')
        usuarios = fc.cancelar_entrada(usuarios)
        print(usuarios)
   
    else:
        print('Error: Opción NO Existe')

