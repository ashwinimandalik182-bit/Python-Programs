#take input a string and chcek string is palindrome or not
name=input("Enter string=")
rev=""
for ch in name:
    rev=ch+rev
    
if name ==rev:
        print("Palindrome!")
else:
        print("Not Palindrome!")