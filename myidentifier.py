
class Identifier:
    @staticmethod
    def is_op(c):
        try:
            lexeme = c.lexeme
            return True if lexeme in ['SUB','ADD','DEV','MUL'] else False
        except:
            print(c.lexeme)
            raise NoLexemeError(c)
            return False
    
    @staticmethod
    def is_expop(c):
        try:
            lexeme = c.lexeme
            return True if lexeme in ['SUB','ADD'] else False
        except:
            raise NoLexemeError()
            return False
    @staticmethod
    def is_termop(c):
        try:
            lexeme = c.lexeme
            return True if lexeme in ['DEV','MUL'] else False
        except:
            raise NoLexemeError()
            return False
    
    @staticmethod
    def is_number(c):
        try:
            lexeme = c.lexeme
            return True if lexeme in ['NUMBER'] else False
        except:
            raise NoLexemeError()
            return False
    
    @staticmethod
    def is_paran(c):
        try:
            lexeme = c.lexeme
            return True if lexeme in ['LPARAN','RPARAN'] else False
        except:
            raise NoLexemeError()
            return False
        
    
class NoLexemeError(Exception):        
    def __init__(self):
        Exception.__init__(self,"This class doesn't have the lexeme.") 
    