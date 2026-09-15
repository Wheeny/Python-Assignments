def StringManipulation(word,letter):
    index = 0
            
    for count in word: 
        if letter == count:
            index+=1
            
    return index
 
 
 
word = "Happy"
letter = 'p'

print(StringManipulation(word,letter))


