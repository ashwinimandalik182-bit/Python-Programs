'''
write a fuction to return the sum of digits of a nmber,n
'''
def sum_digit(n):
    n=str(n)
    total=0
    for digit in n:
        total=total+int(digit)
    return total
print(sum_digit(312))