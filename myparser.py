from myidentifier import Identifier

class Parser:
    tokens=[]
    ans = 0.0
    def __init__(self, tokens):
        self.tokens = tokens
        
        
    def parse(self):
        self.tree = self.take_expression(self.tokens)
        
    def calc(self):
        self.ans = self.tree.calc()
        
    def get_ans(self):
        return self.ans
        
    def take_expression(self, tokens):
        terms = []
        ops = []
        terms.append(self.take_term(tokens))
        
        if len(tokens) == 0:
            return Expression(terms,ops)
        
        while len(tokens) != 0 and Identifier.is_expop(tokens[0]['instance']):
            tmp = tokens.pop(0)
            print(tmp['instance'].value)
            ops.append(tmp)
            terms.append(self.take_term(tokens))
        return Expression(terms, ops)
    
    def take_term(self, tokens):
        factors = []
        ops = []
        factors.append(self.take_factor(tokens))
        if len(tokens) == 0:     
            return Term(factors,ops)
        
        while len(tokens) != 0 and Identifier.is_termop(tokens[0]['instance']):
            tmp=tokens.pop(0)
            print(tmp['instance'].value)
            ops.append(tmp)
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
        ret = Factor(expr = expr)
        return ret
    
    def product_sub(self, tokens):
        
        sub = tokens.pop(0) 
        print(sub['instance'].value)
        number = tokens.pop(0)
        print(number['instance'].value)
        ret = Factor(sub = sub, number = number)
        return ret
    
    def product_number(self, tokens):
        number = tokens.pop(0)
        print(number['instance'].value)
        ret = Factor(number)
        return ret
        
        
class Factor:
    factorlist=[]
    ans=0.0
    def __init__(self,number=None,expr=None,sub=None):
        
        if expr == None:
            if sub == None:
                self.factorlist.append(number)
            else:
                self.factorlist.append(sub)
                self.factorlist.append(number)
        else:
            self.factorlist.append(expr)
    
    def calc(self):
        print(self.factorlist)
        if Identifier.is_op(self.factorlist[0]['instance']):
            self.factorlist.pop(0)
            self.ans = -self.factorlist.pop(0)['instance'].value
        else:
            self.ans = self.factorlist.pop(0)['instance'].value
        return self.ans
            
class Term:
    termlist = []    
    ans=0.0
    def __init__(self, factors, ops):
        self.termlist.append(factors[0])
     
        for i in range(len(ops)):
            self.termlist.append(ops[i])
            self.termlist.append(factors[i+1])

    def calc(self):
        
        print(self.termlist)
        self.ans = self.termlist.pop(0).calc()
        option = {'DEV':self.dev, 'MUL':self.mul}
        for i in range(len(self.termlist)/2):
            
            option[self.termlist.pop(0)['instance'].lexeme](self.ans, self.termlist.pop(0))
        
        return self.ans
        
    def dev(val,token):
        return val / token['instance'].value
    def mul(val,token):
        return val * token['instance'].value    
            
            
            
class Expression:
    exprlist = []
    ans=0.0
    def __init__(self, terms, ops):
        self.exprlist.append(terms[0])
        
        for i in range(len(ops)):
            self.exprlist.append(ops[i])
            self.exprlist.append(terms[i+1])

    def calc(self):
        
        print(self.exprlist)
        
        self.ans = self.exprlist.pop(0).calc()
        option = {'SUB':self.sub, 'ADD':self.add}
        for i in range(len(exprlist)/2):
            
            option[exprlist.pop(0)['instance'].lexeme](self.ans,exprlist.pop(0))
        
        return self.ans
        
    def sub(val,token):
        return val - token['instance'].value
    def add(val,token):
        return val + token['instance'].value    
    
class NoRParanException(Exception):        
    def __init__(self):
        Exception.__init__(self,"No RPARAN Exception.") 
    
    
    