secret_number = 13

while True:
    number = int(input("Enter a  number: "))
    if number == secret_number:
        print("You got it!")
        break
    if number > secret_number:
        print("Too high") 
    elif number < secret_number:
        print("Too low") 
    else:
        print("Try again!")
