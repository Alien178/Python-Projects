information = input("Please write you Information\n")
wordCount = 1
characterCount = 0

for i in information:
    characterCount += 1
    if (i == " "):
        characterCount -= 1
        wordCount += 1

print(characterCount)
print(wordCount)