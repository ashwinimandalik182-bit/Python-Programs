'''Write a program to continuosly input a number n fromuser and
 print if it is positive or negative until the user enters Quite'''

while True:
    user_input=input("Enter the number(stop until type Quit):")

    if user_input=="Quit":
        break
    num=int(user_input)

    if num>0:
        print("Positive!!")
    elif num<0:
        print("Negative!!")
    else:
        print("Zero")