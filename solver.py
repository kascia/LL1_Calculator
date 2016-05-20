class Solver:
    def __init__(self, strcalc):
        self.strcalc = strcalc
        self.ans=0.0
        
    def calc(self):
        self.ans=eval(self.strcalc)

    def get_ans(self):        
        return self.ans