# LISTA VACIA DE ASISTENCIA Y PERSONAS RECHAZADAS PARA GUARDAR LAS PERSONAS
asistencia = []
rechazados = []

# LISTA CON CODIGOS GENERICOS DE INVITACION A LA FIESTA
codInvitacion = ["N001", "N002", "N003", "N004", "N005", "N006", "N007", "N008", "N009", "N010", "N011", "N012", "N013", "N014", "N015"]

#CICLO PARA REGISTRAR INVITADOS, PRIMERA PREGUNTA DE VALIDACION CON CODIGO
while True:
    reg = input("Hola bienvenido a la fiesta de disfraces 'The Crazy Hats'. Digite su código de invitación (o 'salir' si no tienes): ").upper()
    #SI DIGITA SALIR EL CICLO CIERRA
    if reg == 'SALIR':
        break
    #SI REPITE UN CODIGO, EL CICLO SE CIERRA
    elif reg not in codInvitacion:
        print("\nLo siento, tu código de invitación no es válido o ya se uso.")
        break

    #AQUI SE REGISTRA LOS DATOS DEL USUARIO 
    print("Perfecto, sigue con la asistencia: ")
    asisNombre = input("¿Cual es tu nombre?: ")
    asisDOC = input("¿Cual es tu tipo de documento? (CC, CE, CONTRASEÑA, PP): ")
    asisEdad = int(input("¿Cual es tu edad?: "))
    asisAltura = int(input("¿Cual es tu altura? (En cm, ejemplo 172): "))
    asisSombrero = input("¿Tienes un sombrero loco? (si/no): ")

    #CONDICIONALES PARA SABER SI CUMPLE O NO CUMPLE
    if asisEdad < 18:
        print("\nEres menor de edad, devuélvete a tu casa.\n")
        #AGREGAR A LISTA DE RECHAZADOS
        rechazados.append(asisNombre + " Razon: Menor de edad "+ " Con codigo: " + reg)
    elif asisAltura < 150:
        print("\nMides muy poco, cómprate unos zapatos altos y devuélvete a tu casa.\n")
        #AGREGAR A LISTA DE RECHAZADOS
        rechazados.append(asisNombre + " Razon: Poca estatura " + " Con codigo: "+ reg)
    elif asisDOC.lower() not in ["cc", "ce", "pp"]:
        print("\nEres un pollito recién salido del cascarón, espera la cédula real.\n")
        #AGREGAR A LISTA DE RECHAZADOS
        rechazados.append(asisNombre + " Razon: Documento no válido " + " Con codigo: " + reg)
    elif asisSombrero.lower() != "si":
        print("\nEs necesario un sombrero loco, vete de aquí.\n")
        #AGREGAR A LISTA DE RECHAZADOS
        rechazados.append(asisNombre + " Razon: No tiene sombrero loco " + " Con codigo: "+ reg)
    else:
        #AGREGAR A LISTA DE ASISTENCIA
        asistencia.append(asisNombre + " Edad: " + str(asisEdad) + " Con codigo: " + reg)
    #ELIMINA EL CODIGO DE INVITACION REGISTRADO
    codInvitacion.remove(reg)

#AL FINALIZAR EL CICLO WHILE SE IMPRIME ESTOS DOS FOR
#(AMBOS CICLOS WHILE CUENTAN CON UNA ESTRUCTURA SIMILAR, TIENEN DOS VARIABLES) i y elemento, una almacena el valor de enumerate, es decir el indice, y el elemento almacena cada dato de la asistencia, todo sera en for para que pueda ser una columna lo que imprima, el i se le suma el 1 para iniciar en 1 y no en 0 
print("\nLista de ingreso aceptada\n")
for i, elemento in enumerate(asistencia):
    print(f"# {i + 1}: {elemento.title()}")

print("\nLista de rechazados\n")
for i, elemento in enumerate(rechazados):
    print(f"# {i + 1}: {elemento.title()}")
