choice = input("Would you like to; Add, Subtract, Divide, Times, Modulus(Remainder): ")


if choice.lower() == "add":
    xAdd = int(input("\nEnter the first number you would like to add: "))
    yAdd = int(input("\nEnter the second number you would like to add: "))
    
    print(f"\nThe two numbers ({xAdd} and {yAdd}) added together is {xAdd + yAdd}")
    
if choice.lower() == "subtract":
    xSub = int(input("\nEnter the first number you would like to subtract from: "))
    ySub = int(input("\nEnter the second number you would like to subtract by: "))
    
    print(f"\nThe two numbers ({xSub} and {ySub}) subtracted is {xSub - ySub}")
    
if choice.lower() == "divide":
    xDiv = int(input("\nEnter the number you would like to divide: "))
    yDiv = int(input("\nEnter the number you would like to divide by: "))
        
    print(f"\nThe two numbers {xDiv} divided by {yDiv} equals {xDiv / yDiv}")
    
if choice.lower() == "times":
    xTimes = int(input("\nEnter the number you would like to multiply: "))
    yTimes = int(input("\nEnter the number you would like to multiply by: "))
            
    print(f"\nThe two numbers {xTimes} multiplied by {yTimes} equals {xTimes * yTimes}")
    
if choice.lower() == "modulus":
    xMod = int(input("\nEnter the number you would like to divide: "))
    yMod = int(input("\nEnter the number you would like to divide by: "))
        
    print(f"\nThe remainder of the two numbers {xMod} and {yMod} is {xMod % yMod}")
