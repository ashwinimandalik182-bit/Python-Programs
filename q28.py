lis1=[1,2,3,4]
lis2=[3,4,5,6,7,8]
set1=set(lis1)
set2=set(lis2)
if set1.intersection(set2):
    print("shares commen Elements!")
else:
    print("No Common Elements!")