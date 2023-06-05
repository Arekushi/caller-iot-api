class UnauthenticatedException(Exception):
    def __init__(self):
        self.message = f'Não autenticado! Informe um Bearer Token válido.'
        super().__init__(self.message)
