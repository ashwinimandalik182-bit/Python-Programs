list=[1,2,3,4,3,2,5,6,7]
l=set()
dup=set()
for num in list:
    if num in l:
     dup.add(num)
    else:
        l.add(num)
print("Repeated Elements=",dup)