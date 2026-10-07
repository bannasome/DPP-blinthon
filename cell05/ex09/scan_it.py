import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]
    
    matches = re.findall(keyword, text)
    
    if len(matches) > 0:
        print(len(matches))
    else:
        print("none")

# python cell05\ex09\scan_it.py
# python cell05\ex09\scan_it.py "the"
# python cell05\ex09\scan_it.py "the" "the quick brown fox jumps over the lazy dog"