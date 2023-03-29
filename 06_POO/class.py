'''class Person:
    def __init__(self, name ,age, x ):
        self.name= name
        self.age= age
        self.x= x
    def myName(self):
        print("Hello my name is "+ self.name)

   # def myAge(self):
       # print("Hello my age is "  + self.age)
     
    def escribir(self):
        print(self.x)

pl= Person("John",36,10)
pl.myName()
pl.escribir()          '''


"""# instanciar la clase
class MyClass:
    x=5

    def z():"""

class Animal:
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    # Método genérico pero con implementación particular
    def hablar(self):
        # Método vacío
        pass

    # Método genérico pero con implementación particular
    def moverse(self):
        # Método vacío
        pass

    # Método genérico con la misma implementación
    def describeme(self):
        print("Soy un Animal del tipo", type(self).__name__)

# Perro hereda de Animal
class Perro(Animal):
    pass

mi_perro = Perro('mamífero', 10)
mi_perro.describeme()
# Soy un Animal del tipo Perro

class Perro(Animal):
    def hablar(self):
        print("Guau!")
    def moverse(self):
        print("Caminando con 4 patas")

mi_perro= Perro('mamifero',10)
mi_perro.hablar()

class Vaca(Animal):
    def hablar(self):
        print("Muuu!")
    def moverse(self):
        print("Caminando con 4 patas")

class Abeja(Animal):
    def hablar(self):
        print("Bzzzz!")
    def moverse(self):
        print("Volando")

    # Nuevo método
    def picar(self):
        print("Picar!")
