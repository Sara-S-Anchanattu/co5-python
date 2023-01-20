class time:
    def __init__(self,hr,mn,sc):
        self.__hour = hr
        self.__minute = mn
        self.__second = sc

    def __gt__(self,other):
        if self.__hour>other.__hour:
            return True
        elif other.__hour>other.__hour:
            return False
        elif self.__hour==other.__hour:
            if self.__minute>other.__minute:
                return True
            elif self.__minute>other.__minute:
                return False
            elif self.__minute==other.__minute:
                if self.__second > other.__second:
                    return True
                elif self.__second>other.__second:
                    return False
                elif self.__second==other.__second:
                    print("Time is equal")









h=int(input("enter the hr"))
m=int(input("enter the minutes"))
s=int(input("enter the seconds"))
h1=int(input("enter the hour"))
m1=int(input("enter the minutes"))
s1=int(input("enter the seconds"))

t1= time (h,m,s)
t2= time (h1,m1,s1)


if t1>t2:
    print("t1 is greater")
else:
    print("t2 is greater")