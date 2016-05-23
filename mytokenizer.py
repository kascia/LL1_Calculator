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
        self.tokenize_class(str_, numbers, Number)

    def tokenize_ops(self, str_, ops):
        self.tokenize_class(str_,ops,Op)
    
    def tokenize_parans(self, str_, parans):
        self.tokenize_class(str_,parans,Paran)
    
    def tokenize_class(self, str_, items, Class_):
        findfrom=0
        for i in range(len(items)):
            token = dict()
            index = str_.find(items[i], findfrom)
            findfrom = index + 1
            token['index'] = index
            token['instance'] = Class_.new_instance(items[i])
            self.tokens.append(token)  