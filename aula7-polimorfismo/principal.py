from produto import Produto, Livro

produto1 = Produto("Mesa", 847.849)
livro1 = Livro("Casa de Pensão", 54.47, "Aluísio de Azevedo")

produto1.descrever()
livro1.descrever()
livro1.calculaDesconto()