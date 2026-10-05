word1 = input("Enter word 1: ")
word2 = input("Enter word 2: ")

if sorted(word1.lower()) == sorted(word2.lower()):
    print("Word1 and Word2 are Anagrams")
else:
    print("Word1 and Word2 are Not Anagrams")