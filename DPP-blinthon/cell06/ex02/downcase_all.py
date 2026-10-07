import sys

def downcase_it(s):
    return s.lower()

args = sys.argv[1:]

if not args:
    print("none")
else:
    for arg in args:
        print(downcase_it(arg))

# python cell06\ex02\downcase_all.py "HELLO WORLD" "I understood Arrays well!"