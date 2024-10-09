from animal import Animal, Mamifero, Reptil

animal1 = Animal("Gato", 2,)
animal1.exibirInfo()
animal1.somAnimal("MEOW!")
print("-"*50)

mamifero1 = Mamifero("Leo", 10)
mamifero1.exibirInfo()
mamifero1.somAnimal("ROAR")
mamifero1.alimentarFilhotes()
print("-"*50)

reptil1 = Reptil("Tartaruga", 50)
reptil1.exibirInfo()
reptil1.somAnimal("GRUNT")
reptil1.mudarPele()