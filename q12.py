def evn(a,b):
    print("Even Numbers Between a and b!!")
    i=0
    count=0
    for i in range(a,b+1):
        if i%2==0:
            count+=1
            print("index=",count,"Even Number=",i)
print(evn(3,20))