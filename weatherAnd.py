cold = input("Is it cold?('y' or 'n') ")
rain = input("Is it raining?('y' or 'n' ")
if(cold == 'y' and rain == 'y'):
    print("u need a raincoat, boots, and an umbrella.")
elif(cold == 'y' and rain == 'n'):
    print("wear a jacket and you'll be good.")
elif(cold == 'n' and rain == 'y'):
    print("bring an umbrella and boots.")
else:
    print("the weather is perfect.")