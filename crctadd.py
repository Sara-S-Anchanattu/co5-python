class time:
    def __init__(self,hr,mn,sc):
        self.__hour = hr
        self.__minute = mn
        self.__second = sc

    def __add__(self,other):


        t3.__hour=t1.__hour+t2.__hour
        t3.__minute=t1.__minute+t2.__minute
        t3.__second=t1.__second+t2.__second
        if t3.__second>59 :
            t3.__second-=60
            t3.__minute+=1
        if t3.__minute>59:
            t3.__minute-=60
        t3.__hour=t3.__hour+1
        return(str(t3.__hour)+":"+str(t3.__minute)+":"+str(t3.__second))


h=int(input("enter the hr"))
m=int(input("enter the minutes"))
s=int(input("enter the seconds"))
h1=int(input("enter the hour"))
m1=int(input("enter the minutes"))
s1=int(input("enter the seconds"))
#return 'time is: ' + str(self.__hour + other.__hour) + ':' + str(self.__minute + other.__minute) + ':' + str(
    #self.__second + other.__second)





t1= time (h,m,s)
t2= time (h1,m1,s1)
t3=time(0,0,0)
print(t1+t2)
