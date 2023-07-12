from Endereco import Endereco
from Imovel import Imovel


class Proprietario:
    def __init__(self, nome: str, cpf: str, identidade: str, rua: str, numero: int, cep: str, estado: str, cidade: str):
        self._imoveis: list[Imovel] = []
        self._nome: str = nome
        self._cpf: str = cpf
        self._identidade: str = identidade
        self._endereco: Endereco = Endereco(rua, numero, cep, estado, cidade)

    @property
    def endereco(self) -> Endereco:
        return self._endereco

    @endereco.setter
    def endereco(self, endereco: Endereco):
        self._endereco = endereco

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, valor: str):
        self._nome = valor

    @property
    def cpf(self) -> str:
        return self._cpf

    @cpf.setter
    def cpf(self, valor: str):
        self._cpf = valor

    @property
    def identidade(self) -> str:
        return self._identidade

    @identidade.setter
    def identidade(self, valor: str):
        self._identidade = valor

    def atualizaEndereco(self, rua: str, numero: int, cep: str, estado=None, cidade=None) -> None:
        self._endereco.rua = rua
        self._endereco.numero = numero
        self._endereco.cep = cep

        if estado is not None:
            self._endereco.estado = estado

        if cidade is not None:
            self._endereco.cidade = cidade

    def adicionarImovel(self, imovel: Imovel) -> bool:
        self._imoveis.append(imovel)
        return True

    def mostrarImoveis(self) -> list[Imovel]:
        return self._imoveis

    def alugarImovel(self, data: str) -> bool:
        for imovel in self._imoveis:
            if imovel.estaDisponivel(data):
                imovel.alugarImovel(data)
                return True
        return False

    def bloquearImovel(self, data: str) -> bool:
        for imovel in self._imoveis:
            if imovel.estaDisponivel(data):
                imovel.bloquearImovel(data)
                return True
        return False
