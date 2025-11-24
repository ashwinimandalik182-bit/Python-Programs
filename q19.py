#check number is prime or using function
while True:
    def is_prim(n):
        if n<2:
            return False
   
        for i in range(2,n):
            if n%i==0:
                return "not Prime!!"
            return "Prime!!"
    n=int(input("Enter the Number:"))
    print(is_prim(n))
