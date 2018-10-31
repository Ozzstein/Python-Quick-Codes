# Exercises on a names list. The names will be different for each group.
#1. Create a list of everyone's first name in the room
names = ['Fred', 'Wilma', 'Betty', 'Barney',
         'Dino', 'Dino', 'Bambam', 'Ed']

#2. Find the index of your name (using the ``names.index()`` method).
print(names.index("Dino"))

#3. Create an alphabetically sorted list using the ``sorted()`` function.
sorted_names = sorted(names)
print(sorted_names)

#4. Retrieve a list of names after yours in the alphabet.
my_index = sorted_names.index("Dino")
print(sorted_names[my_index+1:])

#5. Are there are any duplicate first names?
if len(set(names)) == len(names):
    print('No duplicates')
else:
    print('Duplicates')
