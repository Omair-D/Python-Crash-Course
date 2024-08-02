# Make the function so the shirts are large by default and the text is I love Python
def make_shirt(size='large', text='I love Python'):
    print(f"\nI would like a size {size} with the message printed {text} for my shirt.")

# Make a large shirt with default message
make_shirt()

# Make a medium shirt with default message
make_shirt('medium')

# Make a small shirt with a different message
make_shirt(size='small', text='Hello World')