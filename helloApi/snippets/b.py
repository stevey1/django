from .a import A

class B(object):
    def bar(self, *args):
        a = A()
        return a.foo(*args)