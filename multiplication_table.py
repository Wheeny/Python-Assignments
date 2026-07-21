


for number in range(1,13):
    print(f" 1 x {number:^5} = {number*1:<15} 2 x {number:^5} = {number*2:<15} 3 x {number:^5} = {number*3:<15} 4 x {number:^5} = {number*4:<15} 5 x {number:5} = {number*5:<15} 6 x {number:^5} = {number*6:<15}  x {number:^5} = {number*7:<15} 8 x {number:^5} = {number*8:<15} 9 x {number:^5} = {number*9:<15} 10 x {number:^5} = {number*10:<15} 11 x {number:^5} = {number*11:<15} 12 x {number:^5} = {number*12:<15}")
    print()  
    

        
   
   
           
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

for table in range(1, start + 1):
    
    for number in range(1, end + 1):
        print(f"{number:>2} x {table:^5} = {table * number:<15}", end="")
    print() 
   
