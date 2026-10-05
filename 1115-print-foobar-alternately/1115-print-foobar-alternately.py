from threading import *
con=Condition()
class FooBar:
    def __init__(self, n):
        self.n = n
        self.turn=1


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            with con:
                while(self.turn!=1):
                    con.wait()
                printFoo()
                self.turn=0
                con.notify_all()



    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            with con:
                while(self.turn!=0):
                    con.wait()
                printBar()
                self.turn=1
                con.notify_all()