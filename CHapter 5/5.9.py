def is_pallindrome(word):
    copy = word.lower()
    value = word.lower()
    reverse = ""
    for letter in reversed(value):
        reverse += letter
        
    return reverse == copy
    
    
print(is_pallindrome("radar"))
