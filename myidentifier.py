
class Identifier:

    @staticmethod
    def is_op(c):
        return Identifier.has_lexeme(c, ['SUB','ADD','DEV','MUL'])
    
    @staticmethod
    def is_expop(c):
        return Identifier.has_lexeme(c, ['SUB','ADD'])
        
    @staticmethod
    def is_termop(c):
        return Identifier.has_lexeme(c, ['DEV','MUL'])
    
    @staticmethod
    def is_number(c):
        return Identifier.has_lexeme(c, ['NUMBER'])
    
    @staticmethod
    def is_paran(c):
        return Identifier.has_lexeme(c, ['LPARAN','RPARAN'])

    @staticmethod
    def has_lexeme(c, lexemes):
        try:
            return c.lexeme in lexemes
        except:
            raise NoLexemeError()

    
class NoLexemeError(Exception):        
    def __init__(self):
        Exception.__init__(self,"This class doesn't have the lexeme.") 
    