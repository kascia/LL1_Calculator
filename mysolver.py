from mytokenizer import Tokenizer
from myparser import Parser

class Solver:
    def __init__(self, strcalc):
        self.strcalc = strcalc
        self.ans=0.0
        
    def calc(self):
        tokenizer = Tokenizer(self.strcalc)
        tokenizer.tokenize()
        tokens = tokenizer.get_tokens()
        
        parser = Parser(tokens)
        parser.parse()
        parser.calc()
        self.ans = parser.get_ans()               
        
    def get_ans(self):        
        return self.ans