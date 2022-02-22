print("                                         Practica Profesionalizante: Actividad Cadenas")
print("---------------------------------------------------------Ejercicio 1---------------------------------------------------------")

print ("Franco Agustin Vedia Robert")

print("---------------------------------------------------------Ejercicio 2---------------------------------------------------------")

print('''Franco Agustin
Vedia Robert''')

print("---------------------------------------------------------Ejercicio 3---------------------------------------------------------")

print ("Franco Agustin\nVedia Robert")

print("---------------------------------------------------------Ejercicio 4---------------------------------------------------------")

NombreCompleto= "Franco Agustin Vedia Robert"

print("---------------------------------------------------------Ejercicio 5---------------------------------------------------------")

Email= input("Escriba su email: ")

print("---------------------------------------------------------Ejercicio 6---------------------------------------------------------")

print ("En nombre completo hay " + str(len(NombreCompleto)) + " caracteres contando espacios")

print("---------------------------------------------------------Ejercicio 7---------------------------------------------------------")

print ("El quinto elemento de mi nombre es " + NombreCompleto[4])

print("---------------------------------------------------------Ejercicio 8---------------------------------------------------------")

solo_mi_nombre= NombreCompleto[:6]
print(solo_mi_nombre)

print("---------------------------------------------------------Ejercicio 9---------------------------------------------------------")

mes_de_nacimiento= "junio"
print(mes_de_nacimiento.upper())

print("---------------------------------------------------------Ejercicio 10--------------------------------------------------------")

separador=" "
transformar_a_cadena= NombreCompleto.split(separador)
nombres= transformar_a_cadena[0] + " " +transformar_a_cadena[1]
apellidos= transformar_a_cadena[2] + " " + transformar_a_cadena[3]
print (nombres + " " + apellidos.upper())

print("---------------------------------------------------------Ejercicio 11--------------------------------------------------------")

posicion = str (NombreCompleto.find(apellidos))
print("En mis apellido comienzan en la posicion: " + posicion)

print("---------------------------------------------------------Ejercicio 12--------------------------------------------------------")

cambiar_a_nickname=NombreCompleto.replace("Franco Agustin","Negro")
print (cambiar_a_nickname)

print("---------------------------------------------------------Ejercicio 13--------------------------------------------------------")

nickname= "Negro"
adicionando_el_nickname= nickname + " " + NombreCompleto
print(adicionando_el_nickname)

print("---------------------------------------------------------Ejercicio 14--------------------------------------------------------")

cadenaconespacios = " CESIT, MAIPU "
print (cadenaconespacios.strip())

print("---------------------------------------------------------Ejercicio 15--------------------------------------------------------")

AmigosDeFranco= "Roberto, Juan, Pedro, Leonel"
print(AmigosDeFranco.split())

print("-----------------------------------------------------------Desafio-----------------------------------------------------------")
nombre = input("Escriba su nombre: ")
apellido = input("Escriba su apellido: ")
respuesta = (f"Este es el trabajo de: {apellido}, {nombre}")
print(respuesta)