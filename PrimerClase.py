class Persona:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def miFuncion(self):
        print("Hello my name is "+self.name)

p1= Persona("Anyone", 24)
p1.miFuncion() 

# Borrar objetos
#   del p1
# Borrar propiedades del objeto
# del p1.age