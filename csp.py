# Program Developed BY
# NAME : HARI PRIYA M
# REG NO : 212224240047

from itertools import permutations

def is_valid(word1, word2, word3, mapping):
    def get_value(word):
        value = 0
        for ch in word:
            value = value * 10 + mapping[ch]
        return value
    val1 = get_value(word1)
    val2 = get_value(word2)
    val3 = get_value(word3)
    return val1 + val2 == val3

# Taking user input
word1 = input("Enter first word: ").upper()
word2 = input("Enter second word: ").upper()
word3 = input("Enter result word: ").upper()

letters = list(set(word1 + word2 + word3))

# If more than 10 unique letters, not possible
if len(letters) > 10:
    print("Too many unique letters, no solution possible.")
else:
    found = False
    for perm in permutations(range(10), len(letters)):
        mapping = dict(zip(letters, perm))
        if mapping[word1[0]] == 0 or mapping[word2[0]] == 0 or mapping[word3[0]] == 0:
            continue
        if is_valid(word1, word2, word3, mapping):
            print("\nSolution Found:")
            for k, v in mapping.items():
                print(f"{k} = {v}")
            print(f"\n{word1} = {''.join(str(mapping[ch]) for ch in word1)}")
            print(f"{word2} = {''.join(str(mapping[ch]) for ch in word2)}")
            print(f"{word3} = {''.join(str(mapping[ch]) for ch in word3)}")
            found = True
            break
    if not found:
        print("No valid solution found.")
