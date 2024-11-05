class Zwierze:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Kotowate(Zwierze):
    def glos(self):
        print(" Mial")

class KotDomowy(Kotowate):
    def coJe(self):
        print(" Domowy kot lubi mleko")

class Psowate(Zwierze):
    def glos(self):
        print("Aluuuu")

class Pies(Psowate):
    def odglos(self):
        print("Hau Hau!")

class Hiena(Psowate):
    def odglos(self):
        super().glos()
        print("Hi Hi Hi!")

kot = KotDomowy("Burek", 10)
print(list(str(kot)))

print(kot.name)
print(kot.age)
kot.coJe()
kot.glos()

pies = Pies("Onyx", 20)
pies.odglos()
print(pies.name)
print(pies.age)
pies.glos()

hiena = Hiena("Pumba", 5)
print(f"Czesc, jestem hiena {hiena.name}")
hiena.odglos()
