class Number:
    lexeme = 'NUMBER'
    def __init__(self, value=0.0):
        self.value=value

    @staticmethod
    def new_instance(value):
        return Number(value)