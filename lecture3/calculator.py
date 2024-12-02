def addition(x, y):
    return(x+y)
def subtract(x, y):
    return(x-y)
def multiply(x, y):
    return(x*y)
def divide(x, y):
    if y==0:
        return("error")
    return(x/y)
def calculator():
    while True:
        print("select operation")
        print("1. addition")
        print("2. subtract")
        print("3. multiply")
        print("4. divide")
        print("5. exit")
        choice=input("enter 1/2/3/4/5: ")
        if choice=="5":
            print("exiting.")
            break
        if choice not in ['1', '2', '3', '4']:
            print("invalid choice.")
            continue
        num1=float(input("enter 1st number: "))
        num2=float(input("enter 2nd number: "))
        if choice=="1":
            print(f"{num1}+{num2}={addition(num1, num2)}")
        if choice=="2":
            print(f"{num1}-{num2}={subtract(num1, num2)}")
        if choice=="3":
            print(f"{num1}*{num2}={multiply(num1, num2)}")
        if choice=="4":
            print(f"{num1}/{num2}={divide(num1, num2)}")
calculator()





