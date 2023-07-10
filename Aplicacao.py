from Imovel import Imovel
from Proprietario import Proprietario


class Aplicacao:
    listaProprietarios: list[Proprietario] = []

    @staticmethod
    def menuCadastraImovel() -> None:
        print("Digite o valor do iptu")
        valorIPTU: float = float(input())
        print("Digite o tipo do imóvel")
        tipo: str = input()
        print("Digite sua utilização")
        utilizacao: str = input()
        print("Digite nome da rua")
        rua: str = input()
        print("Digite o estado")
        estado: str = input()
        print("Digite a cidade")
        cidade: str = input()
        print("Digite o número do imovel")
        numero: int = int(input())
        print("Digite o cep")
        cep: str = input()

        imovel: Imovel = Imovel(valorIPTU, rua, numero, cep, tipo, utilizacao, estado, cidade)

        print("Deseja adicionar um proprietário a este imóvel ? [S/N]")
        respostaProprietario = input()
        if respostaProprietario == "S":
            print("Digite o cpf do proprietário")
            cpf: str = input()
            for proprietario in Aplicacao.listaProprietarios:
                if proprietario.cpf == cpf:
                    proprietario.adicionarImovel(imovel)



    @staticmethod
    def menuCadastraProprietario() -> None:
        print("Digite seu nome ")
        nome: str = input()
        print("Digite seu cpf ")
        cpf: str = input()
        print("Digite sua identidade ")
        identidade: str = input()
        print("Digite o número da sua casa")
        numero: int = int(input())
        print("Digite o cep")
        cep: str = input()
        print("Digite o nome da rua")
        rua: str = input()
        print("Digite o estado")
        estado: str = input()
        print("Digite sua cidade ")
        cidade: str = input()

        proprietario = Proprietario(nome, cpf, identidade, rua, numero, cep, estado, cidade)

        Aplicacao.listaProprietarios.append(proprietario)

    @staticmethod
    def mostraImoveis() -> None:
        print("Digite o cpf do proprietario")
        cpf: str = input()

        for proprietario in Aplicacao.listaProprietarios:
            if cpf == proprietario.cpf:
                for imovel in proprietario.mostrarImoveis():
                    index = 1
                    print(f"Imóvel [{index}]: ")
                    print(imovel.tipo)
                    print(imovel.utilizacao)
                    print(f"Rua: {imovel.endereco.rua}, {imovel.endereco.numero}. CEP: {imovel.endereco.cep}")
                    index+=1

    @staticmethod
    def alugaImovel()->None:
        print("Digite o cpf do proprietario que deseja alugar a residência")
        cpf: str = input()
        for proprietario in Aplicacao.listaProprietarios:

            if proprietario.cpf == cpf:
                print("Digite a data [DD/MM/AAAA]: ")
                data: str = input()

                if proprietario.alugarImovel(data):
                    print("Casa alugada com sucesso")
                else:
                    print("Não foi possível alugar a casa")

    @staticmethod
    def app() -> None:
        while True:
            print('-=-=-' * 15)
            print('-=-=--=- Boas Vindas, selecione algumas das opções do menu abaixo -=-=--=-')
            print("[1] - Cadastrar proprietário")
            print("[2] - Cadastrar imovel")
            print("[3] - Alugar imovel")
            print("[4] - Bloquear imovel")
            print("[5] - Mostrar imóveis")
            print("[6] - Sair")
            print('-=-=-' * 15)
            opcaomenu: int = int(input())
            if opcaomenu == 1:
                Aplicacao.menuCadastraProprietario()
            elif opcaomenu == 2:
                Aplicacao.menuCadastraImovel()
            elif opcaomenu == 3:
                Aplicacao.alugaImovel()
            elif opcaomenu == 5:
                Aplicacao.mostraImoveis()
            elif opcaomenu == 6:
                break

def main() -> None:
    app = Aplicacao
    app.app()

if __name__ == "__main__":
    main()