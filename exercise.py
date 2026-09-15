list_of_tuples = []

def listing_tuples(name):
    size =  len(name) 
    if size > 3 and is_prime(size):
        tuple_name = (name, len(name))
        list_of_tuples.append(tuple_name)
    
        return list_of_tuples
        
    else:
        return "Enter a name whose length is both greater than 3 and a prime number"        
    
 

def is_prime(number):
    for count in range(2, int(number)):
        if number % count == 0:
            return False
      
    return True    


count = 0
while count <= 3:
    name = input("Enter name: ")
    print(listing_tuples(name))
    count+=1    
   
