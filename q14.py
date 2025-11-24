'''write a function to return the count the number of
 digits in a number,n'''
n=input("Enter num:")
def count_digit(n):
    return len(str(n))
print(count_digit(n))