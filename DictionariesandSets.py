# Explanation: This prints a dictionary of English-Vietnamese words, using a for loop.

dictionary = {"hello": "xin chào", "world": "thế giới", "python": "pythôn"}
for word, translation in dictionary.items():
    print(f"{word}: {translation}")
