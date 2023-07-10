from Endereco import Endereco
from Agenda import Agenda
class Imovel:

    def __init__(self, numeroIPTU: float, rua: str, numero: int, cep: str, tipo: str, utilizacao: str,estado: str = 'BA', cidade: str='Salvador') -> None:
        self._numeroIPTU: float = numeroIPTU
        self._tipo: str = tipo
        self._utilizacao: str = utilizacao
        self._endereco: Endereco = Endereco(rua, numero, cep, estado, cidade)
        self._agenda = Agenda()

    @property
    def endereco(self) -> Endereco:
        return self._endereco

    @endereco.setter
    def endereco(self, endereco: Endereco):
        self._endereco = endereco

    @property
    def numeroIPTU(self) -> float:
        return self._numeroIPTU

    @numeroIPTU.setter
    def numeroIPTU(self, valor: float):
        self._numeroIPTU = valor

    @property
    def tipo(self) -> str:
        return self._tipo

    @tipo.setter
    def tipo(self, valor: str):
        self._tipo = valor

    @property
    def utilizacao(self) -> str:
        return self._utilizacao

    @utilizacao.setter
    def utilizacao(self, valor: str):
        self._utilizacao = valor

    def alugarImovel(self, data: str) -> bool:
        self._agenda.adicionar_data_alugado(data)
        return True

    def estaDisponivel(self, data) -> bool:
        if self._agenda.obter_estado(data):
            return True

        return False




