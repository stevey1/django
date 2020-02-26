from .original import Original
class CallingClass():
    test = '100'
    @staticmethod
    def func():
        return '200'
    def func2(self):
        return 'test'
    def func3(self):
        return self.func2()+'a'
        
    def func4(self):
        return Original().foo()