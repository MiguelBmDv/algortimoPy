asistencia = []
rechazados = []
codInvitacion = ["N001", "N002", "N003", "N004", "N005", "N006", "N007", "N008", "N009", "N010", "N011", "N012", "N013", "N014", "N015"]

while True:
    reg = input("Hola bienvenido a la fiesta de disfraces 'The Crazy Hats'. Digite su código de invitación (o 'salir' si no tienes): ").upper()
    
    if reg == 'SALIR':
        break
    
    elif reg not in codInvitacion:
        print("\nLo siento, tu código de invitación no es válido o ya se uso.")
        break

    
    print("Perfecto, sigue con la asistencia: ")
    asisNombre = input("¿Cual es tu nombre?: ")
    asisDOC = input("¿Cual es tu tipo de documento? (CC, CE, CONTRASEÑA, PP): ")
    asisEdad = int(input("¿Cual es tu edad?: "))
    asisAltura = int(input("¿Cual es tu altura? (En cm, ejemplo 172): "))
    asisSombrero = input("¿Tienes un sombrero loco? (si/no): ")

    if asisEdad < 18:
        print("\nEres menor de edad, devuélvete a tu casa.\n")
        rechazados.append(asisNombre + " Razon: Menor de edad "+ " Con codigo: " + reg)
    elif asisAltura < 150:
        print("\nMides muy poco, cómprate unos zapatos altos y devuélvete a tu casa.\n")
        rechazados.append(asisNombre + " Razon: Poca estatura " + " Con codigo: "+ reg)
    elif asisDOC.lower() not in ["cc", "ce", "pp"]:
        print("\nEres un pollito recién salido del cascarón, espera la cédula real.\n")
        rechazados.append(asisNombre + " Razon: Documento no válido " + " Con codigo: " + reg)
    elif asisSombrero.lower() != "si":
        print("\nEs necesario un sombrero loco, vete de aquí.\n")
        rechazados.append(asisNombre + " Razon: No tiene sombrero loco " + " Con codigo: "+ reg)
    else:
        asistencia.append(asisNombre + " Edad: " + str(asisEdad) + " Con codigo: " + reg)

    codInvitacion.remove(reg)
print("\nLista de ingreso aceptada\n")
for i, elemento in enumerate(asistencia):
    print(f"# {i + 1}: {elemento.title()}")

print("\nLista de rechazados\n")
for i, elemento in enumerate(rechazados):
    print(f"# {i + 1}: {elemento.title()}")
