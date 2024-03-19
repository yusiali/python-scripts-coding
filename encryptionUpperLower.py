message = input("Enter a message to encode or decode: ") 
#message = message.upper()           
output = ""                         
for letter in message:              
    if letter.isupper():            
        value = ord(letter) + 16    
        letter = chr(value)         
        if not letter.isupper():    
            value = value- 26            
            letter = chr(value)      
    if letter.islower():
        
        value = ord(letter) + 16    
        letter = chr(value)         
        if not letter.islower():    
            value = value- 26             
            letter = chr(value)            
            
    output = output + letter                
print("Output message: ", output)   
