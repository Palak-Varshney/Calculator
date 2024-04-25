#CALCULATOR
while(True):
    num1=float(input("Enter num1: "))
    opt=input("Enter any operation '+,-,*,/': ")
    num2=float(input("Enter num2: "))

    if(opt=='+'):
        ans=num1+num2
        print("Answer",ans)
    elif(opt=='-'):
        ans=num1-num2
        print("Answer",ans)
    elif(opt=='*'):
        ans=num1*num2
        print("Answer",ans)
    elif(opt=='/'):
        ans=num1/num2
        print("Answer",ans)
    else:
        print("invalid input")
    if(input("press C to continue: ")in('Cc')):
        continue;
    else:
        print("exit")
        break
   
    

