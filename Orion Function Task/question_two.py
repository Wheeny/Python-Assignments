def discount(name, original_price, promotional_code):
    if promotional_code.upper() == "SAVE10":
        discount = original_price * 0.1
        return original_price - discount
    elif promotional_code.upper() == "HALFOFF":
        discount = original_price * 0.5
        return original_price - discount
    else:
        return original_price
        
        
        
name = input("Enter the name of an item: ")
original_price = float(input("Enter the original price  of an item: "))
promotional_code = input("Enter promotional code: ")

print(discount(name, original_price, promotional_code))
