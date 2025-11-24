#Number Guessing Game


secret_num=6
while True:
    guess=int(input("Enter the number:"))
    if guess>secret_num:
        print("To High!!")
    elif guess<secret_num:
        print("To Low!!")
    else:
        print("Correct!!")
        break
    