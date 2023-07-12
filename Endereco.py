class Endereco:
    def __init__(self, rua: str, numero: int, cep: str, estado: str, cidade: str):
        self._rua: str = rua
        self._numero: int = numero
        self._cep: str = cep
        self._estado: str = estado
        self._cidade: str = cidade

    @property
    def rua(self) -> str:
        return self._rua

    @rua.setter
    def rua(self, valor: str):
        self._rua = valor

    @property
    def numero(self) -> int:
        return self._numero

    @numero.setter
    def numero(self, valor: int):
        self._numero = valor

    @property
    def cep(self) -> str:
        return self._cep

    @cep.setter
    def cep(self, valor: str):
        self._cep = valor

    @property
    def estado(self) -> str:
        return self._estado

    @estado.setter
    def estado(self, valor: str):
        self._estado = valor

    @property
    def cidade(self) -> str:
        return self._cidade

    @cidade.setter
    def cidade(self, valor: str):
        self._cidade = valor
