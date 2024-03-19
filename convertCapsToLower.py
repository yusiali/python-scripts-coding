a = input("enter: ")
a.upper()
output = ""
for x in a:
    if x.isupper():
        x = x.lower()
    output += x
            
        
print(output);