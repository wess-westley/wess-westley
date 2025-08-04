num1=int(input("input the number you may want to do some caculation on      "))
num2=int(input("the other  number ...."))
operation=input( "chooose the operation  you want to do on the numbers you inputted previously...")

if operation == "+":
    answer= num1 + num2
    print( answer)
elif operation == "-":
    answer= num1 - num2
    print( answer)
elif operation == "*":
    answer=num1 * num2
    print(answer)
elif operation == "/":
    answer=num1 / num2
    print(answer)
else :
    print("error you entered an invalid  operation ")
    
