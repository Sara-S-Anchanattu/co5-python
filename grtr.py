class greater:
    def __init__(self,a):
        self.a=a

    def __gt__(self,other):
        if self.a>other.a:
            return True
        else:
            return False

ob1 =greater(7)
ob2=greater(55)
if ob1>ob2:
    print("ob1 is greater")
else:
    print("ob2 is greater")