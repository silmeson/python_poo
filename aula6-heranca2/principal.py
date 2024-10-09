from pessoa import Pessoa, Aluno, Professor

p1 = Pessoa("Claudio", 79)
a1= Aluno("Silmeson", 18, "3 ano do Ensino Médio")
prof1 = Professor("Bruno", 40, "ADS")

p1.info()

a1.info()
a1.estudar() 

prof1.info()
prof1.ensinar()