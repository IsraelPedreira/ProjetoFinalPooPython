from Endereco import Endereco
class Imovel:

    def __init__(self, numeroIPTU: float, rua: str, numero: int, cep: str, tipo: str, utilizacao: str,estado: str = 'BA', cidade: str='Salvador') -> None:
        self._numeroIPTU: float = numeroIPTU
        self._tipo: str = tipo
        self._utilizacao: str = utilizacao
        self._endereco: Endereco = Endereco(rua, numero, cep, estado, cidade)

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



