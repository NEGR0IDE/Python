print ("+++++++++++++++++++++++++++++++++++++ Operaciones Matemáticas +++++++++++++++++++++++++++++++++++++")

print ("• Ejercicio 1:")
Cant_de_Lap= 150
Cant_de_Per= 7
Resultado= Cant_de_Lap // Cant_de_Per
Resto= Cant_de_Lap % Cant_de_Per
print(f"Cada persona utilizará {Resultado} lapices.")
print (f"Me sobrarán {Resto} lapices.")

print ("• Ejercicio 2:")
Personas= 7
Lap_por_Per= 15
Caja=12
LapicesxPersona=  round(Lap_por_Per * Personas)
Can_de_Cajas= 105 // 12
Sobrante= 105 % 12
print (f"Necesitaría comprar {Can_de_Cajas} cajas.")
print (f"Y me sobrarían {Sobrante} lapices.")

print ("• Ejercicio 3:")
import math
r1= 12.5
r2= 5
Volumen1= 4/3 * math.pi * pow(r1,3)
Volumen2= 4/3 * math.pi * pow(r2,3)
Diferencia= abs (Volumen1 - Volumen2)
print("El volumen de la esfera de radio 5 cm es: ", round(Volumen2,2))
print ("El volumen de la esfera de radio 12.5 cm es:", round(Volumen1,2))
print ("La diferencia entre el volumen de las esferas es: ", round(Diferencia,2))


print ("+++++++++++++++++++++++++++++++++++++ Desafío Aritmética +++++++++++++++++++++++++++++++++++++")

Caja_de_Vino= 6
Cantidad_x_Botella= 0.75
Medida_Estandar= 0.175
Personas_invitadas=20

vasos= Cantidad_x_Botella // Medida_Estandar
resto_de_botella= Cantidad_x_Botella % Medida_Estandar

Botellas= 18
Total_de_Cajas= Botellas / Caja_de_Vino
Total_de_Botellas= Total_de_Cajas / Caja_de_Vino

Resto_de_las_18_Botellas= resto_de_botella * Total_de_Botellas
Sobrante= resto_de_botella / Cantidad_x_Botella
print("La cantidad de vasos llenos de vino por botella son: ", (vasos))
print ("La cantidad que sobrará de cada botella es", round(resto_de_botella,3))
print("La cantidad de personas que estarán en la fiesta es de 21")
print("Si 3 personas no toman alcohol entonces serian 18")
print(f"Necesitará {Total_de_Cajas} en total de cajas de vino y en total serian {Total_de_Botellas} botellas de vino.")
print(f"La cantidad de botellas obtenida es de {Resto_de_las_18_Botellas} si consideramos los las cantidades totales de vino")
print("El numero total de cajas a comprar seria de: ", ())


