# Store 5 words and their meanings in a dictionary
glossary = {
	'variable': 'A named storage location in memory that holds data or objects',
	'string': 'A series of characters.',
	'list': 'A collection of items in a particular order.',
	'comment': 'A note in a program that the Python interpreter ignores.',
	'dictionary': "A collection of key-value pairs.",
	'loop': 'Work through a collection of items, one at a time.',
	'bit': 'Short for "binary digit," which is the smallest piece of information a computer can use',
	'boolean': 'A simple concept that represents "true" or "false" and is used in every programming language',
	'algorithm': 'Can be understood by anyone without knowledge of a specific language, and can help with problem-solving communication'

	
}

# Clean up glossary project just by using a for-loop to display terms and definitions
for term, definition in glossary.items():
	print(f"{term.title()}:\n\t{definition}\n")

