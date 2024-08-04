# Make list containing short text messages
# and empty list
texts = ['lol', 'how are u', 'heyyy', 'good morning', 'good night']
sent_messages = []

# Make function that will print each message
# and move each message to the empty list
def send_messages(texts, sent_messages):
    """Print each message, and then move it to sent_messages."""
    print("\nSending all messages:")
    while texts:
        current_message = texts.pop()
        print(current_message)
        sent_messages.append(current_message)

# Adding for a copy of original list
send_messages(texts[:], sent_messages)

print("\nFinal lists:")
print(texts)
print(sent_messages)