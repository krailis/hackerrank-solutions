from collections import OrderedDict

N = int(input())
wordlist = OrderedDict()
for _ in range(N):
    word = input()
    if word in wordlist.keys():
        wordlist[word] += 1
    else:
        wordlist[word] = 1
print(len(wordlist.items()))
for val in wordlist.values():
    print(val, end=" ")
