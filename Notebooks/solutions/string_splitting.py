
#1. Convert the string ``'cisco systems'`` to upper case and title case (``Cisco Systems``).
mystring = "great britain"
print(mystring.upper())
print(mystring.title())

#2. Split this string into a list of words:

logline = 'String splitting can be done via the split method.'
print(logline.split())

#3. Test whether the string contains any words beginning with ``s`` and ending with ``ing:``.
words = logline.split()
for word in words:
    word = word.lower()
    if word.startswith("s") and word.endswith("ing"):
        print(word)

#4. Use list indexing to obtain a list of bi-grams, i.e. pairs of words occuring next to each other. The first bi-gram in the sentence is `["String", "splitting"]`.
for i in range(len(words) - 1):
    print(words[i:i+2])
