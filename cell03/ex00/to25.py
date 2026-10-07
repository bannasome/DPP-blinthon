value = int(input("Enter a number less than 25\n"))

if value > 25:
    print("Error")
else:
    while value <= 25:
        print(f"Inside the loop, my variable is {value}")
        value += 1
        