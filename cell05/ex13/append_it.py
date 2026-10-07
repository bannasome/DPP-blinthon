import sys

args = sys.argv[1:]

if not args:
    print("none")
else:
    for arg in args:
        if not arg.endswith("ism"):
            print(f"{arg}ism")

# python cell05\ex13\append_it.py "parallel" "egoism" "human"