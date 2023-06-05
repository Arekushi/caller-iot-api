class StudentNotFoundException(Exception):
    def __init__(self, ra):
        self.ra = ra
        self.message = f'O estudante com RA: [{ra}] não existe!'
        super().__init__(self.message)
