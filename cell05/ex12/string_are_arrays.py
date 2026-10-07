import sys

if len(sys.argv) != 2:
    print("none")
else:
    text = sys.argv[1]
    z_count = text.count("z")
    if z_count == 0:
        print("none")
    else:
        print("z" * z_count)
        
# python cell05/ex12/string_are_arrays.py "The character Z is not found in this string"
# python cell05\ex12\string_are_arrays.py "Zaz visits the zoo with Zazie"
