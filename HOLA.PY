num =int(input("Ingrese el numero que deseo solo acepta números de 3 digitos: "))

centena= num // 100 * 100
decena= (num % 100) // 10 * 10
unidad= num % 10

print(f"centena: {centena}")
print(f"decena: {decena}")
print(f"unidad: {unidad}")
while True:
    codigo = input("Ingrese el siguiente parametros 223 O 245: ")
    parametro = int(codigo)
    if parametro == 223 or parametro == 245:
        print("Ingreso el parametro adecuado")
        break
    else:
        print("Corrobora el parametro  que se te está solicitando")
stUnidades = ["CERO", "UNO", "DOS", "TRES", "CUATRO", "CINCO", "SEIS", "SIETE", "OCHO", "NUEVE", "DIEZ", "ONCE", "DOCE", "TRECE", "CATORCE", "QUINCE"]
stDecenas = ["", "DIEZ", "VEINTE", "TREINTA", "CUARENTA", "CINCUENTA", "SESENTA", "SETENTA", "OCHENTA", "NOVENTA"]
stCentenas = ["", "CIEN", "DOSCIENTOS", "TRESCIENTOS", "CUATROCIENTOS", "QUINIENTOS", "SEISCIENTOS", "SETECIENTOS", "OCHOCIENTOS", "NOVECIENTOS"]

num = int(input("Ingresa el numero que tu desee: "))
if num < 0 or num > 999:
    print ("Numero incorrecto")
else:
    unidades = num % 10
    decidades = num % 100
    decenas = (num // 10) % 10
    centenas = num // 100

    if centenas != 0:
        if centenas == 1:
            if decidades == 0:
                print ("CIEN", end="")
            else:
                print ("CIENTO", end="")
        else:
            print (stCentenas[centenas], end="")
        if decidades != 0:
            print (" ", end="")

    if decidades <= 15:
        if decidades != 0 or centenas == 0:
            print (stUnidades[decidades], end="")
    else:
        if decenas == 1:
            print ("DIECI", end="")
        elif decenas == 2: 
            if unidades == 0:
                print ("VEINTE", end="")
            else:
                print ("VEINTI", end="")
        else:
            print (stDecenas[decenas], end="")
            if unidades != 0:
                print (" Y ", end="")
        if unidades != 0:
            print (stUnidades[unidades], end = "")
    print ("")