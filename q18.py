#created a simple calculater using match case


def cal(a,b,operation):

    match operation:
        case "+":
            return a+b
        case "-":
            return a-b
        case "*":
            return a*b
        case "/":
            if b==0:
                return "Error"
            return a/b
        case _:
            return "SuccesFul!"
a=int(input("enter the a:"))
b=int(input("enter the b:"))
print(cal(a,b,"+"))
print(cal(a,b,"-"))
print(cal(a,b,"*"))
print(cal(a,b,"/"))