import sys

class IO:
    def __init__(self):
        self.strcalc=''
        self.ans=0.0
        
    def get_strcalc(self):
        argv = sys.argv[1:]
        argc = len(argv)
        
        for i in range(argc):
            self.strcalc += argv[i]
            
        return self.strcalc
    
    def print_ans(self,ans):
        self.ans = ans
        print('answer' , self.ans)
    