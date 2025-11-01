<h1>Exp 8 : Solve Cryptarithmetic Problem,a CSP(Constraint Satisfaction Problem) using Python</h1> 
<h3>Name: HARI PRIYA M            </h3>
<h3>Register Number: 2122242420047/h3>
<H3>Aim:</H3>
<p>
    To solve Cryptarithmetic Problem,a CSP(Constraint Satisfaction Problem) using Python
</p>
<h3>Procedure:</h3>
Input and Output
<br>Input:
This algorithm will take three words.
<br> B A S E<br>
    B A L L<br>
           ----------<br>
           G A M E S<br>

Output:
It will show which letter holds which number from 0 – 9.
For this case it is like this.

              B A S E                         2 4 6 1
              B A L L                         2 4 5 5
             ---------                       ---------
            G A M E S                       0 4 9 1 6
Algorithm
For this problem, we will define a node, which contains a letter and its corresponding values.<br>

isValid(nodeList, count, word1, word2, word3)<br>

Input − A list of nodes, the number of elements in the node list and three words.<br>

Output − True if the sum of the value for word1 and word2 is same as word3 value.<br>

Begin<br>
   m := 1<br>
   for each letter i from right to left of word1, do<br>
      ch := word1[i]<br>
      for all elements j in the nodeList, do<br>
         if nodeList[j].letter = ch, then<br>
            break<br>
      done<br>
      val1 := val1 + (m * nodeList[j].value)<br>
      m := m * 10<br>
   done<br>

   m := 1<br>
   for each letter i from right to left of word2, do<br>
      ch := word2[i]<br>
      for all elements j in the nodeList, do<br>
         if nodeList[j].letter = ch, then<br>
            break<br>
      done<br>

      val2 := val2 + (m * nodeList[j].value)
      m := m * 10
   done<br>

   m := 1<br>
   for each letter i from right to left of word3, do<br>
      ch := word3[i]<br>
      for all elements j in the nodeList, do<br>
         if nodeList[j].letter = ch, then<br>
            break<br>
      done<br>

      val3 := val3 + (m * nodeList[j].value)
      m := m * 10
   done<br>

   if val3 = (val1 + val2), then<br>
      return true<br>
   return false<br>
End<br>
<hr>

<h2>Program</h2>

```python

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

```

<h2>Sample Input and Output:</h2>
<img width="500" height="370" alt="Screenshot 2025-11-01 084935" src="https://github.com/user-attachments/assets/913946dd-e7f8-4bd4-8ae7-ef5884e259bc" />

<hr>
<h2>Result:</h2>
<p> Thus a Cryptarithmetic Problem was solved using Python successfully.</p>
