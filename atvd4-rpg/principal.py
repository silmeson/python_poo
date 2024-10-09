from personagem import Personagem, Jogador, Monstro

personagem1 = Personagem("Elfo", 700)
personagem1.detalhes()
personagem1.atacar()

jogador1 = Jogador("Elfo das Águas", "Elfo", 700)
jogador1.detalhes()
jogador1.atacar()
jogador1.usarHabilidade("Conexão com a natureza")

monstro1 = Monstro("Vorath, o Devastador", "Vampiro", 5000, 17000)
monstro1.exibirInformacoes()

monstro1.invocarAliado("Eldrinor", "Dragão")