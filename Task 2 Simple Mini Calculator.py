while True: 
    print("     MINI CALCULATOR      ")
    num1=float(input("Enter the first number:"))
    num2=float(input("Enter the second number:"))
    print("Choose 1 for Addition")
    print("Choose 2 for Subtraction")
    print("Choose 3 for Multiplication")
    print("Choose 4 for Division")
    print("Choose 5 Exit The Menu")
    choice=int(input("Enter the choice from 1 to 5:"))
    if(choice==1):
        num3=int(num1+num2)
        print("The Addition of the two given numbers is:",num3)
    elif(choice==2):
        num3=int(num1-num2)
        print("The Subtraction of the two given numbers is:",num3)
    elif(choice==3):
        num3=int(num1*num2)
        print("The Multiplication of the given two numbers is:",num3)
    elif (choice==4):
        num3=int(num1/num2)
        print("The Division of the given two numbers is:",num3)
    elif (choice==5):
        print("Exiting the Menu!!!")
        break
    else:
        print("Enter Correct Choice!!")
