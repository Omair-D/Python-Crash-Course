# Read cats.txt and dogs.txt and print contents
file_names = ['cats.txt', 'dogs.txt']

for filename in file_names:
    print(f"\nReading file: {filename}")
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError: # Account for text file missing
        print("  Sorry, I can't find that file.")