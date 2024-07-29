languages = ['english', 'urdu', 'arabic', 'french', 'mandarin', 'korean', 'spanish']

# Printing exact location
print(languages[2])

# Printing exact location with capitalization
print(languages[2].title())

# Accessing last location of the list
print(languages[-1].title())

# Printing the list
print(languages)

# Changing the value of the first location
languages[0] = 'german'
print(languages)

# Adding elements to a list
languages.append('japanese')
print(languages)

# Inserting elements to a list
languages.insert(0, 'cantonese')
print(languages)

# Removing an item from the list
del languages[1]
print(languages)

# Removing using pop()
popLanguage = languages.pop()

# Printing what got removed
print(popLanguage)

print(languages)

# Removing an item by its value
languages.remove('french')
print(languages)

# Sorting the list
languages.sort()
print(languages)

# Reversing order with sort()
languages.sort(reverse=True)
print(languages)

# Reversing the order of the list
languages.reverse()
print(languages)

# Finding length of list
print(len(languages))