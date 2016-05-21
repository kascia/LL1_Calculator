import re

from number import Number
from paran import Paran
from op import Op

class Tokenizer:
    
    re_number = re.compile('[0-9]+[\.][0-9]+|[0-9]+')
    re_op = re.compile('[\+\-\*\/]')
    re_paran = re.compile('[\(\)]')
    
    def __init__(self, strcalc):
        self.strcalc = strcalc
        self.tokens=[]

   
    def tokenize(self):        
        str_ = self.strcalc
        numbers = self.re_number.findall(str_)
        ops = self.re_op.findall(str_)
        parans = self.re_paran.findall(str_)
        
        self.tokenize_numbers(str_,numbers)
        self.tokenize_ops(str_,ops)
        self.tokenize_parans(str_,parans)
        self.tokens.sort(key=lambda dic: dic['index'])
    
    def get_tokens(self):
        return self.tokens
    
    def tokenize_numbers(self, str_, numbers):
        findfrom = 0
        for i in range(len(numbers)):
            token = dict()
            index = str_.find(numbers[i], findfrom)
            findfrom = index + 1
            token['index'] = index
            token['instance'] = Number(numbers[i])
            self.tokens.append(token)

    def tokenize_ops(self, str_, ops):
        findfrom = 0
        for i in range(len(ops)):            
            token = dict()
            index = str_.find(ops[i], findfrom)
            findfrom = index + 1
            token['index'] = index
            token['instance'] = Op.new_instance(ops[i])
            self.tokens.append(token)
    
    def tokenize_parans(self, str_, parans):
        findfrom=0
        for i in range(len(parans)):
            token = dict()
            index = str_.find(parans[i], findfrom)
            findfrom = index + 1
            token['index'] = index
            token['instance'] = Paran.new_instance(parans[i])
            self.tokens.append(token)  
        