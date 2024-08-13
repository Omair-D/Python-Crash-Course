# Modify cats_dogs.py to fail silently if either file is missing
file_names = ['cats.txt', 'dogs.txt']

for filename in file_names:
    print(f"\nReading file: {filename}")
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError: # Account for text file missing
        pass
