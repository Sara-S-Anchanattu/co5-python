a={
    "d":"orange",
    "c":"banana",
    "z":"carrot"
}
b=list(a.items())
b.sort()
print("Ascending order is:",b)
c=list(a.items())
c.sort(reverse=True)
print("Descending order is:",c)


