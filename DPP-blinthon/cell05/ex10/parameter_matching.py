import sys

if len(sys.argv) != 2:
    print("none")
else:
    param = sys.argv[1]
    text = input("What was the parameter? ")
    
    if text == param:
        print("Good job!")
    else:
        print("Nope, sorry...") 