# Calculator Functionality

#Step 1 Take input two variables for functionality working

num3 = int(input("Enter your first number: "))
num2 = int(input("Enter your first number: "))

#Substraction functionality 

def Substract(nmu1,num2):
    if num1 > num2:
        return num1-num2
    else:
        return num2 -num1
    
#multiplication functionality

def Multiplication(num1,num2):
    return num1 * num2

def Division(num1,num2):
    return num1/num2

def Percentage():
    return "100%"
