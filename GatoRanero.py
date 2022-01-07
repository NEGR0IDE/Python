class Gato:
    especie="mamifero"

    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
        self.alimentos=0

    def etapaDeVida(self):
        if self.edad>1:
            print(self.nombre,"es adulto")
        else:
            print(self.nombre,"Es un perro")

    def alimentoFavorito(self,alimento):
        self.alimentosfavoritos= 
        return alimento in self.alimentos


roberto= Gato("Roberto",48, caca)

print(roberto.nombre, roberto.edad, roberto.alimentos)