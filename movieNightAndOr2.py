yusuf = input("Is yusuf going to movie night?('yes' or 'no) ")
kevin = input("Is kevin going to movie night?('yes' or 'no) ")
josh = input("Is josh going to movie night?('yes' or 'no) ")
tony = input("Is tony going to movie night?('yes' or 'no) ")

if(yusuf == "yes" and kevin == "yes" and josh == "yes" and tony == "yes"):
    print("movie night is happening")
elif((yusuf == "yes" and kevin == "yes") or (yusuf == "yes" and josh == "yes") or (yusuf == "yes" and tony == "yes")):
    print("movie night is happening")
elif((kevin == "yes" and josh == "yes") or (kevin == "yes" and tony == "yes")):
    print("movie night is happening")
elif((josh == "yes" and tony == "yes")):
    print("movie night is happening")
else:
    print("movie night is cancelled")