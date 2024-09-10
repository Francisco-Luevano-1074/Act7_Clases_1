print("Introducción a clases")
class Animal:
    Edad=3
    Raza="Chihuas"
    comida="croquetas"
    def come(self):
        print(f"El perro come "+self.comida)
print(Animal)
print("Creando el objeto de la clase Animal")
perro=Animal()
print(f"Edad del perro: {perro.Edad}")
print(f"Raza del perro: {perro.Raza}")
perro.come()


