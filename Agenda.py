class Agenda:
    def __init__(self):
        self._datas_alugado = []
        self._datas_bloqueado = []

    def adicionar_data_alugado(self, data: str) -> None:
        self._datas_alugado.append(data)


    def adicionar_data_bloqueado(self, data: str) -> None:
        self._datas_bloqueado.append(data)

    def obter_estado(self, data: str) -> bool:
        if data in self._datas_alugado:
            return False
        elif data in self._datas_bloqueado:
            return False
        else:
            return True

    def definir_estado(self, data: str, estado: str) -> None:
        if estado == "alugado":
            if data in self._datas_bloqueado:
                self._datas_bloqueado.remove(data)
            if data not in self._datas_alugado:
                self._datas_alugado.append(data)
        elif estado == "bloqueado":
            if data in self._datas_alugado:
                self._datas_alugado.remove(data)
            if data not in self._datas_bloqueado:
                self._datas_bloqueado.append(data)
        elif estado == "disponível":
            if data in self._datas_alugado:
                self._datas_alugado.remove(data)
            if data in self._datas_bloqueado:
                self._datas_bloqueado.remove(data)