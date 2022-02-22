
                        #Super Clase (Celulares).
class Guitarras: #Definir como clase con la palabra "class" y terminar con ":" dos puntos.
    def __init__ (self, marca, modelo, mastil, cuerdas,color): #Metodo constructor 
        self.marca= marca                            #*Self.nombre del atributo
        self.modelo= modelo
        self.mastil= mastil                          
        self.cuerdas= cuerdas
        self.color= color                             
    def mostrar_datos(self):                 #Defino una funcion para mostrar los datos de la clase celulares
        return (f"""La guitarra marca: {self.marca}, modelo: {self.modelo}
Tiene un mastil: {self.mastil}
{self.cuerdas} cuerdas
Y color {self.color}""")

                        #Sub Clase (TecladoDeBotones)
class  Electrica(Guitarras):          #Defino una subclase 
    def __init__(self,marca,modelo,mastil,cuerdas,color,jack,pastillas,palanca):    #Defino el metodo contructor
        super().__init__(marca,modelo,mastil,cuerdas,color)  #Defino un metodo contrsuctor con super().__init__                 
        self.jack= jack                                    #en el defino que es lo que quiero heredar
        self.pastillas= pastillas       #Atributos nuevos
        self.palanca= palanca
    def mostrar_datos_electrica(self):        #Defino el método de la clase
        return (f"""Posee jack: {self.jack}
Posee pastillas: {self.pastillas}
Posee palanca: {self.palanca}""")
                        #Sub Clase (TecladoTactil)
class Clasica(Guitarras):
    def __init__(self,marca,modelo,mastil,cuerdas,color,boca):
        super().__init__(marca,modelo,mastil,cuerdas,color)
        self.boca= boca
    def mostrar_datos_clasica(self):
        return (f"Posee boca: {self.boca}")


# Atributos y objetos de la Subclase Celulares
Marca= "Gibson"
Modelo= "Songwriter deluxe"
Mastil= "simple"
Cuerdas= "6"
Color= "marron"
Boca= "si"

# Atributos y objetos de la Subclase
Marca2="Fender"
Modelo2= "Stratocaster"
Mastil2= "doble"
Cuerdas2= "6"
Color2= "roja"
Jack2= "si"
Pastillas2= "single coil"
Palanca2= "si"

Clasica=Clasica(Marca,Modelo,Mastil,Cuerdas,Color,Boca)
Electrica= Electrica(Marca2,Modelo2,Mastil2,Cuerdas2,Color2,Jack2,Pastillas2,Palanca2)


print("-----------------------------------------------------------Clasica--------------------------------------------------------")
print(Clasica.mostrar_datos())
print(Clasica.mostrar_datos_clasica())
print("-----------------------------------------------------------Electrica------------------------------------------------------")
print(Electrica.mostrar_datos())
print(Electrica.mostrar_datos_electrica())
