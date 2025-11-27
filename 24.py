#Given a tuple integer create:
#1. a tuple of all even numbrs
#2.a tuple of all odd numbers
numbers=(1,2,3,4,5,6,7,8,9,10)
evn_tuple=()
odd_tuple=()
for num in numbers:
    if num%2==0:
        evn_tuple+=(num,)
    else:
        odd_tuple+=(num,)
print("Even Numbers=",evn_tuple)
print("Odd Numbers=",odd_tuple)
