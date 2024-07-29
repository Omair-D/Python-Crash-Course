# Storing five places I'd like to visit
locations = ['Japan', 'France', 'Bahamas', 'Hawaii', 'Cancun']

# Print list in original order
print(locations)

# Print using sorted() without changing original list
print(sorted(locations))

# List is still original check
print(locations)

# Print with sorted() again but reverse alphabetical without changing original
print(sorted(locations, reverse=True))

# Show list is still original
print(locations)

# Use reverse() to change order of list
locations.reverse()

# Show list is now reversed
print(locations)

# Use reverse again to go to original order
locations.reverse()

# Show it is back to original
print(locations)

# Use sort() to store list alphabetically
locations.sort()

# Show it is now changed
print(locations)

# Use sort() to store reverse alphabetically
locations.sort(reverse=True)

# Show it has changed
print(locations)