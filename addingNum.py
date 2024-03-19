def add(num):
    ans = 0
    for x in range(num+1):
        ans += x;
    return ans

go = "y"
while(go =="y"):    
    num = int(input("enter number: "))
    ans = add(num)
    go = input("do u want to continue?('y' or 'n'): ")
print(ans)