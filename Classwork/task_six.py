

"""
for number in range(1, 11):
    if number % 4 == 0:
        print (number)
        
            
            
bases = [4**counter for counter in range(1, 6)]

for base in bases:
    multiples = [base * count for count in range(1, 6)]
    print(f"Multiples of {base}: {multiples}")
 
"""


for number in range(1, 11):
    if number % 4 == 0:
        print (number)
        
        for count in range(5):
            print (number)
            
            
for power in range(1, 6):
    power_of_4 = 4 ** power
    power_of_8 = 8 ** power
    print(f"4^{power} = {power_of_4:<6}  8^{power} = {power_of_8}")

