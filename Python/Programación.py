#3
def contar_vocales(texto): 
    vocales= "a,e,i,o,u"
    contador=0
    for i in texto:
        if i in vocales:
            contador= contador + 1
    print (int (contador))
 return (contador)

#4
 def suma_pares(Lista)
    for i in Lista:
        if i % 2==0
            Suma+ = i
Cuit= input(int)
def validar_cuit(Cuit)
caraceteres_validos= "0,1,2,3,4,5,6,7,8,9-"
if len (Cuit) != 13
    return False
for i in Cuit:
    if not i in caracteres_validos:
        return False
if Cuit.count("-")>2
if Cuit[2] != "-" or cuit[11] != "-"
    return False
return True
