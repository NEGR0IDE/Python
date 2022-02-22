# Ejercicio 3
#Codificar en Python un programa que permita cargar una lista que contenga las notas
#de un curso de 20 alumnos (controlar que las notas válidas son entre 0 y 10) indicando:
Lista= []
Contador= 0
for i in range (0,20):
    Lista.append(int(input("Ingrese la nota: ")))
print (Lista)