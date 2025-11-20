'''The user enters a string containig a number (eg."45").
Convert it to:
an integer
a float
a string again
print all three values with their types'''

#program
num_str=input("enter the number as String=")

num_int=int(num_str)
num_float=float(num_str)
num_agn_str=str(num_int)

print(num_int,type(num_int))
print(num_float,type(num_float))
print(num_agn_str,type(num_agn_str))