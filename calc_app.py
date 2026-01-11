import os

while True:
    print("\nSimple Calculator")
    print("1. Perform a calculation")
    print("2. Print previous Equations")
    print("3. Exit")
    
    choice = input("Choose an option (1 - 3): ")
    
    if choice == "1":
        try:
            num1 = float(input("Enter a number: "))
            operation = input("Enter an operation (+, -, *, /): ") 
            num2 = float(input("Enter a number: "))
            
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                result = num1 / num2
            else:
                print("Invalid operation. Please use +, -, *, or /.")
                continue

            equation = f"{num1} {operation} {num2}"
            print(f"Result: {result}")
            
            # Log the equation and result to the file
            with open("equations.txt", "a") as file:
                file.write(f"{equation} = {result}\n")
            
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            
    elif choice == "2": 
        if os.path.exists("equations.txt"):
            with open("equations.txt", "r", encoding="utf-8") as file:
                equations = file.readlines()
                if equations:
                    print("Previous Equations:")
                    for equation in equations:
                        print(equation.strip())
                else:
                    print("No previous equations found.")
        else:
            print("The file equations.txt does not exist.")
        
    
    elif choice == "3":
        print("Exiting the calculator. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
            
            
            

            
            
            
            
            
            
            
            