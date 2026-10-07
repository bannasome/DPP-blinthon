import sys

args = sys.argv[1:]

if not args:
    print("none")
else:
    print(f"parameters: {len(args)}")
    for arg in args:
        print(f"{arg}: {len(arg)}")

# python cell05\ex11\count_it.py "Game" "of" "Thrones"