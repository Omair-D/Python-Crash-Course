# Read file
my_file = 'learning_python.txt'

with open(my_file) as file_object:
    contents = file_object.read()
# Print content once by reading entire file
print("\nPrinting once: ")
print(contents)

# Print once by looping over the file object
print("\nLooping file: ")
with open(my_file) as file_object:
    for line in file_object:
        print(line.rstrip())

# Store lines in a list
print("\nStore lines in list: ")
with open(my_file) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())