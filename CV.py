import random
import string
print("generate a random color hex")
print("#{:60x}".format(random.randint(0,0xFFFFFF)))
print("\n generate a random alphabetical string:")
max_length=225
s=""
for i in range(random.randint(1,max_length)):
    s+=random.choice(string.ascii_letters)
print(s)
print("generate a random value between 2 integers,inclusive:")
print(random.randint(0,10))
print(random.randint(-7,7))
print(random.randint(1,1))
print("generate a random multiple of 7 between 0 and 70:")
print(random.randint(0,10)*7)