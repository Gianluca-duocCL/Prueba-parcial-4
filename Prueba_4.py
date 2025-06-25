def menu():
    print('Menú principal')
    print('~'*20)
    print("""
    1.- Comprar entrada.
    2.- Consultar comprador
    3.- Cancelar compra.
    4.- Salir.""")
    op = input('Ingrese su opción: ')
    return op

def validar_codigo_verificacion(codigoVerificacion):
    tieneMayusculas = any(c.isupper() for c in codigoVerificacion)
    tieneNro = any(c.isdigit() for c in codigoVerificacion)
    sinEspacios = ' ' not in codigoVerificacion
    return len(codigoVerificacion) >= 4 and tieneMayusculas and tieneNro and sinEspacios

def Comprar_ticket(diccUsuarios, entradaG, entradaV):
    hayEntradas = True
    if entradaG == 0 and entradaV == 0:
        print('No hay cupos disponibles para ninguna categoría.')
        hayEntradas = False
        
    
    if hayEntradas:
       
        while True:
            codigo = input('Ingrese un código (6 caracteres): ').strip()
            if len(codigo) == 6 and codigo not in diccUsuarios:
                break
            else:
                print('Código inválido o ya registrado. Intente Nuevamente')
        
        while True:
            nombre = input('Ingrese nombre del usuario: ')
            if nombre.replace(' ','').isalpha():
                break
            else:
                print('El nombre solo debe contener letras. Intente nuevamente')
       
        while True:
            tipo = input('Ingrese tipo de usuario [G:/ V: ]: ').upper()
            if tipo == 'G' and entradaG > 0:
                break
            elif tipo == 'V' and entradaV > 0:
                break
            else:
                print('Tipo inválido o sin cupos disponibles. Intente Nuevamente')
     
        while True:
            codigoVerif = input('Ingrese código de verificación: ')
            if validar_codigo_verificacion(codigoVerif):
                break
            else:
                print('Código NO válido. Debe tener mínimo 4 caracteres, al menos 1 mayúscula, 1 número y sin espacios.')
        
        diccUsuarios[codigo] = [nombre, tipo, codigoVerif]  
        if tipo == 'G':
            entradaG -= 1
        else:
            entradaV -= 1
        print(f'¡Entrada registrada con éxito para {nombre}')      
    return diccUsuarios, entradaG, entradaV

def cancelar_compra(diccUsuarios, entradaG, entradaV):
    codigo = input('Ingrese el código del usuario a cancelar: ').strip()
    if codigo in diccUsuarios:
        tipo = diccUsuarios[codigo][1]
        del diccUsuarios[codigo]
        if tipo == 'V':
            entradaG += 1
        else:
            entradaV += 1
        print('Matrícula Cancelada correctamente!')
    else:
        print('No existe usuario con ese código')
    return diccUsuarios, entradaV, entradaG

def buscar_contacto():
    print("\n--- Buscar Comprador ---")
    print("1. Por nombre")
  
    opcion = input("Seleccione opción: ")
    criterio = input("Ingrese término de búsqueda: ")
    
    encontrados = []
    for usuario, entradaG,entradaV in Comprar_ticket():
        if (
            (opcion == "1" and criterio.lower() in nombre.lower())
           
            encontrados.append((nombre, datos)))

    if encontrados:
        for nombre, datos in encontrados:
            print(f"\nNombre: {nombre}")
            print(f"Tipo de entrada: {datos['teléfono']}")
            print(f"Dirección: {datos['dirección']}")
            print(f"Correo: {datos['correo']}")
    else:
        print("No se encontraron coincidencias.")

