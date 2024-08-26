def add(num1,num2):
    return num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2

num1=int(input("Enter First Number : "))
num2=int(input("Enter Second Number : "))
choice=0
while choice<5:
    choice=int(input("Select Operation \n1.Addition \n2.Subtraction \n3.Multiply \n4.Divide \n5.Exit \n\n Enter your choice 1,2,3,4,5 : "))
    # if choice==1:
    #     print(num1,"+",num2,"=",add(num1,num2))
    # elif choice==2:
    #     print(num1,"-",num2,"=",sub(num1,num2))
    # elif choice==3:
    #     print(num1,"x",num2,"=",mul(num1,num2))
    # elif choice==4:
    #     print(num1,"/",num2,"=",div(num1,num2))
    # elif choice==5:
    #     break
    # else:
    #     print("invalid choicee")
    
    match choice:
        case 1:
            print(num1,"+",num2,"=",add(num1,num2))
        case 2:
            print(num1,"-",num2,"=",sub(num1,num2))
        case 3:
            print(num1,"x",num2,"=",mul(num1,num2))
        case 4:
            print(num1,"/",num2,"=",div(num1,num2))
        case 5:
            break
        case _:
            print("invalid choice")