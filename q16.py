'''Write a program  to print all numbers from 1 to 100
 that are divisible by both 3 and 5'''

for i in range(1,100):
    if i%3==0:
        print("Divisible 3=",i)
    elif  i%5==0:
        print("Divisble 5=",i)