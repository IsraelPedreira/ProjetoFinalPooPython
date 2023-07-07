from Imovel import Imovel
from Proprietario import Proprietario
numeroIPTU = 1000.0
rua = "Rua Principal"
numero = 10
cep = "12345-678"
tipo = "Residencial"
utilizacao = "Moradia"

propriedade = Imovel(numeroIPTU, rua, numero, cep, tipo, utilizacao, "dwdwdBA", "wddd")
propriedade2 = Imovel(numeroIPTU, rua, numero, cep, "tipo imovel", utilizacao, "dwdwdBA", "wddd")



proprietario = Proprietario("Israel","23232323","2454545453343","rua do prop",345, "3493049-232","estado","ciade")

proprietario.adicionarImovel(propriedade)
proprietario.adicionarImovel(propriedade2)








