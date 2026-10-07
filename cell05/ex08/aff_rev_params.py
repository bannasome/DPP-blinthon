import sys

if len(sys.argv) < 3:
    print("none")
else:
    for arg in reversed(sys.argv[1:]):
        print(arg)

# python cell05\ex08\aff_rev_params.py
# python cell05\ex08\aff_rev_params.py "coucou"
# python cell05\ex08\aff_rev_params.py "Python" "piscine" "hello"