from collections import Counter
import string

def histo(text):
    amount = Counter(text)
    symb = [char for char in amount if char not in string.whitespace]
    symb.sort()
    max_count = max(amount.values())
    for i in range(max_count, 0, -1):
        for char in symb:
            if amount[char] >= i:
                print('#', end=' ')
            else:
                print(' ', end=' ')
        print()
    for char in symb:
        print(char,end=' ')
    print()

stream = input()
histo(stream)