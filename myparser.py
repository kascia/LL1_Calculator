from myidentifier import Identifier

class Parser:
    
    def __init__(self, tokens):
        self.ans = 0.0
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
        
        while len(tokens) != 0 and Identifier.is_expop(tokens[0]['instance']):
            tmp = tokens.pop(0)
            print('exprop', tmp['instance'].value)
            ops.append(tmp)
            terms.append(self.take_term(tokens))
        return Expression(terms, ops)
    
    def take_term(self, tokens):
        factors = []
        ops = []
        print('termtoken',tokens)
        factors.append(self.take_factor(tokens))
        
        while len(tokens) != 0 and Identifier.is_termop(tokens[0]['instance']):
            tmp=tokens.pop(0)
            print('termop', tmp['instance'].value)
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
        print('sub', sub['instance'].value)
        number = tokens.pop(0)
        print('number', number['instance'].value)
        ret = Factor(sub = sub, number = number)
        return ret
    
    def product_number(self, tokens):
        number = tokens.pop(0)
        print('number' , number['instance'].value)
        ret = Factor(number)
        return ret
        
        
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
        print(self.factorlist)
        try:
            if Identifier.is_op(self.factorlist[0]['instance']):
                self.factorlist.pop(0)
                self.ans = -1.0*float(self.factorlist.pop(0)['instance'].value)
            else:
                self.ans = float(self.factorlist.pop(0)['instance'].value)
        except:
            self.ans = self.factorlist.pop(0).calc()
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
        
        print(self.termlist)
        self.ans = self.termlist.pop(0).calc()
        option = {'DEV':self.dev, 'MUL':self.mul}
        for i in range(len(self.termlist)/2):
            self.ans = option[self.termlist.pop(0)['instance'].lexeme](self.ans, self.termlist.pop(0))
        
        return self.ans
        
    def dev(self, val,token):
        return val / token.calc()
    def mul(self, val,token):
        return val * token.calc()
            
            
            
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
        option = {'SUB':self.sub, 'ADD':self.add}
        for i in range(len(self.exprlist)/2):
            self.ans = option[self.exprlist.pop(0)['instance'].lexeme](self.ans, self.exprlist.pop(0))
        
        return self.ans
        
    def sub(self, val,token):
        ret = val - token.calc()
        print(ret)
        return ret
    def add(self, val,token):
        ret = val + token.calc()
        print(ret)
        return ret
    
class NoRParanException(Exception):        
    def __init__(self):
        Exception.__init__(self,"No RPARAN Exception.") 
    
    
    