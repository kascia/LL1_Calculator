class Paran:
                
    def __init__(self, value=''):
        self.value=value
        
    @staticmethod
    def new_instance(ch):
        options = {'(': LParan,')':RParan}   
        return options[ch](ch)


class LParan(Paran):
    lexeme = 'LPARAN'

class RParan(Paran):
    lexeme = 'RPARAN'
