class hun:
    a=0
    b=0
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add1(self):
        print('I m instance method')
        return self.a+self.b
    @classmethod
    def add(cls,a,b):
        print("i m class method")
        return a+b
	
