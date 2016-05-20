class Op:
                
    def __init__(self, value=''):
        self.value=value
        
    @staticmethod
    def new_instance(ch):
        options = {'+': Add, '-':Sub, '*':Mul , '/':Dev}   
        return options[ch](ch)


class Sub(Op):
    lexeme = 'SUB'

class Add(Op):
    lexeme = 'ADD'

class Dev(Op):
    lexeme = 'DEV'

class Mul(Op):
    lexeme = 'MUL'
