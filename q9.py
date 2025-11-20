'''Ask the user for principal(p),rate(r),time(t).convert all to float and compute simple intrest:
si=(p*r*t)/100'''

principal=input("enter the p:")
rate=input("enter the rate:")
time=input("enter the Time:")
p=float(principal)
r=float(rate)
t=float(time)
si=(p*r*t)/100
print(si)