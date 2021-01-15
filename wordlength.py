file = open('beyond_good_and_evil.txt', 'r')
data = file.read()

amountwords = 0
amountletters = 0

line = data.strip()

import re

nospace = re.sub(r'\W+', '', line)

for line in line:
   noline = line.split()
   words = re.sub(r'\W+', '', noline)
   
   amountwords += len(words) 
   amountletters += len(nospace)

print('words: ', amountwords)
print('letters: ', amountletters)

letters_per_word = int(amountletters)/int(amountwords)

print(letters_per_word)