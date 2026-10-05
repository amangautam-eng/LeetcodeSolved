from threading import *
cond=Condition()
lock=Lock()
class Foo:
    def __init__(self):
        self.turn=0


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        with cond:
            printFirst()
            self.turn+=1
            cond.notify_all()



    def second(self, printSecond: 'Callable[[], None]') -> None:
        with cond:
            while(self.turn!=1):
                cond.wait()
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.turn+=1
            cond.notify_all()
        




    def third(self, printThird: 'Callable[[], None]') -> None:

        with cond:
            while(self.turn!=2):
                cond.wait()
        # printThird() outputs "third". Do not change or remove this line.
            printThird()
