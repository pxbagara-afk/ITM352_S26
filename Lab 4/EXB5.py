# 1. Turn string into a list of words
sentence=input("Enter a sentence: ")
words=sentence.split(" ")
print("List of words:", words)

#2. Revverse the list of words
words.reverse()
print("Reversed list of words:", words)

#3. Join the reversed list back into a single string
reversed_sentence=" ".join(words)
print("Reversed sentence:", reversed_sentence)
