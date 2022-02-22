# Ejercicio1

Cadena="12,13,122,S,SA,$,%"
Lista= Cadena.split(",")
Lista.pop(3)
Lista.pop(3)
Lista.pop(3)
Lista.pop(3)
print (Lista)

#Ejercicio2


Entrada=0
def validarCuit (Hasta_13_Carcteres):
    Entrada=input("Ingresar Cuit: ")
    Solo_Numeros= Entrada.isnumeric()
    Cadena1= Entrada.split(",")
    Cadena2= Solo_Numeros.split(",")
    Cantidad_de_Caracteres=len(Cadena1)
    if Cantidad_de_Caracteres == 13 and Solo_Numeros >= 0 and Solo_Numeros[2] = int(-):
        Respuesta= "True"
        
    elif Cantidad_de_Caracteres != 13:
        Respuesta="False"
    return (Respuesta)
print (validarCuit(Entrada))
    

