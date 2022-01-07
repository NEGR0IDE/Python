print("Ingrese dirección que figura en DNI")
calle=input("Ingrese el nombre de la calle :")
numero_casa=int(input("Ingrese el numero de la casa :"))
localidad=input("Ingrese la localidad donde vive :")
residencia=(calle,"numero",numero_casa,localidad)
##########################################################
print("Ingrese dirección actual")
calle=input("Ingrese el nombre de la calle :")
numero_casa=int(input("Ingrese el numero de la casa :"))
localidad=input("Ingrese la localidad donde vive :")
residente=(calle,"numero",numero_casa,localidad)
##########################################################
edad=int(input("Ingrese edad :"))
multas=int(input("Ingrese cantidad de multas :"))
clase=17
while (residencia==residente)=="Maipu" and edad>clase and multas==0:
    print("Renovacion habilitada")
else:
    print("Renovacion inhabilitada")