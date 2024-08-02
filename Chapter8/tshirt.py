# Write function make_shirt() that has two parameters
def make_shirt(size, text):
    print(f"\nI would like a size {size} with the message printed {text} for my shirt.")

# Call function with positional arguments
make_shirt('large', 'I <3 New York')

# Call function with keyword arguments
make_shirt(size='medium', text='Hello World')