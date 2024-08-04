# Make list containing short text messages
texts = ['lol', 'how are u', 'ily', 'good morning', 'good night']

# Make function that will print each message
def send_messages(texts):
    """ Print simple text messages """
    for text in texts:
        print(f"\nMessage: {text}")


send_messages(texts)
