#Give a list of integets compute the average of all numbersin the List
list=int(input=("Enter list="))
cal=0
for val in list:
    cal+=val
    avg=cal/len(list)
print(avg)