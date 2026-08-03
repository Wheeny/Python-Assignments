balance = 1000

while True:
    menu = """
    
    Select Options
    
    1. Deposit
    2. Withdrawal
    3. Balance Check
    4. Exit
    
    """
    
    print(menu)
    user_input = int(input("Select an option to proceed: "))
    
    match user_input:
        case 1: 
            deposit = float(input("Deposit Amount: "))
            balance += deposit
            print(f"Your balance is: {balance}")
        case 2: 
            withdrawal = float(input("Withdrawal Amount: "))
            balance -= withdrawal
            print(f"Your balance is: {balance}")
        case 3: 
            print(f"Your balance is: {balance}")
        case 4:     
            break
        case _: 
            print("Invalid Input")
    
