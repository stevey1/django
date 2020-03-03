class B():
    def __init__(self): 
        self.b = 'b'

class B1():
    def __init__(self,b): 
        self.b = b
class V1(B1):
    #since child class has __init__, super class' __init__ won't be excuted.
    #if child class doesn't has __init__, super class' __init__ will be excuted.
    def __init__(self,b): 
        self.d = b

class V2(B1):
    def __init__(self,b,c): 
        super().__init__(b)
        self.c = c
class V(B):
    def __init__(self): 
        self.d = 'b'    
    a='inside of class'
    def si(self):
        self.a ='set by instance'

    def gi(self):
        return self.a
    @classmethod
    def sc(cls):
        cls.a ='set by class'

    @classmethod
    def gc(cls):
        return cls.a
