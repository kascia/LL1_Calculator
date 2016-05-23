from myidentifier import Identifier

class Parser:
    
    def __init__(self, tokens):
        self.ans = 0.0
        self.tokens = tokens
        
    def parse(self):
        self.tree = self.make_parsetree()

    def make_parsetree(self):
        self.tree = self.take_expression(self.tokens)
        return self.tree

    def calc(self):
        self.ans = self.tree.calc()
        
    def get_ans(self):
        return self.ans
        
    def take_expression(self, tokens):
        terms = []
        ops = []
        terms.append(self.take_term(tokens))
        
        while len(tokens) != 0 and Identifier.is_expop(tokens[0]['instance']):
            ops.append(tokens.pop(0))
            terms.append(self.take_term(tokens))
        return Expression(terms, ops)
    
    def take_term(self, tokens):
        factors = []
        ops = []
        factors.append(self.take_factor(tokens))
        
        while len(tokens) != 0 and Identifier.is_termop(tokens[0]['instance']):
            ops.append(tokens.pop(0))
            factors.append(self.take_factor(tokens))
        return Term(factors,ops)
    
    
    
    def take_factor(self, tokens):
        options = { 'LPARAN':self.product_lparan, 
                   'SUB':self.product_sub, 
                   'NUMBER':self.product_number}
        return options[tokens[0]['instance'].lexeme](tokens)
        

    def product_lparan(self,tokens):
        tokens.pop(0)
        expr = self.take_expression(tokens)
        if tokens.pop(0)['instance'].lexeme != 'RPARAN':
            raise NoRParanException
        return Factor(expr = expr)
    
    def product_sub(self, tokens):
        
        sub = tokens.pop(0) 
        number = tokens.pop(0)
        return Factor(sub = sub, number = number)
    
    def product_number(self, tokens):
        number = tokens.pop(0)
        return Factor(number)
        
        
class Factor:
    
    def __init__(self,number=None,expr=None,sub=None):
        self.factorlist=[]
        self.ans=0.0
        if expr == None:
            if sub == None:
                self.factorlist.append(number)
            else:
                self.factorlist.append(sub)
                self.factorlist.append(number)
        else:
            self.factorlist.append(expr)
    
    def calc(self):
        if Expression.is_expr(self.factorlist[0]):
            self.ans = self.factorlist.pop(0).calc()
            return self.ans
        else:
            if Identifier.is_op(self.factorlist[0]['instance']): # and self.factorlist[0]['instance'].lexeme is 'SUB':
                self.factorlist.pop(0)
                self.ans = -1.0*float(self.factorlist.pop(0)['instance'].value)
            else:
                self.ans = float(self.factorlist.pop(0)['instance'].value)
        return self.ans
            
class Term:
    
    def __init__(self, factors, ops):
        self.termlist = []    
        self.ans=0.0
        self.termlist.append(factors[0])
     
        for i in range(len(ops)):
            self.termlist.append(ops[i])
            self.termlist.append(factors[i+1])

    def calc(self):
        self.ans = self.termlist.pop(0).calc()
        option = {'DEV':lambda a,b : a / b, 'MUL':lambda a,b : a * b}
        for i in range(len(self.termlist)/2):
            self.ans = option[self.termlist.pop(0)['instance'].lexeme](self.ans, self.termlist.pop(0).calc())
        
        return self.ans
    
    @staticmethod
    def is_term(c):
        return c.__class__.__name__ is 'Term'

class Expression:
    
    def __init__(self, terms, ops):
        self.exprlist = []
        self.ans=0.0
        self.exprlist.append(terms[0])
        
        for i in range(len(ops)):
            self.exprlist.append(ops[i])
            self.exprlist.append(terms[i+1])

    def calc(self):
        
        self.ans = self.exprlist.pop(0).calc()
        option = {'SUB':lambda a,b : a - b, 'ADD':lambda a,b : a + b}
        for i in range(len(self.exprlist)/2):
            self.ans = option[self.exprlist.pop(0)['instance'].lexeme](self.ans, self.exprlist.pop(0).calc())
        
        return self.ans
            
    @staticmethod
    def is_expr(c):
        return c.__class__.__name__ is 'Expression'
    
class NoRParanException(Exception):        
    def __init__(self):
        Exception.__init__(self,"No RPARAN Exception.") 
    
    
    