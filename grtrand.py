class time:
    def __init__(self,hr,mn,sc):
        self.__hour = hr
        self.__minute = mn
        self.__second = sc

    def __add__(self,other):
        return 'time is: ' + str(self.__hour+other.__hour)+':' +str(self.__minute+other.__minute)+':' +str(self.__second+other.__second)


h=int(input("enter the hr"))
m=int(input("enter the minutes"))
s=int(input("enter the seconds"))
h1=int(input("enter the hour"))
m1=int(input("enter the minutes"))
s1=int(input("enter the seconds"))

t1= time (h,m,s)
t2= time (h1,m1,s1)
print(t1+t2)