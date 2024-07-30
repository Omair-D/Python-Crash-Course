# Store a dictionary of peoples favorite numbers (they can have more than one favorite)
favNumbers = {
   'zack': [5, 2, 3, 6],
   'ashley': [10, 67],
   'cody': [12, 21, 7],
   'ryan': [25, 50],
   'maria': [38, 52, 79],
}

# Print name along with their favorite numbers with loop
for person, number in favNumbers.items():
   print(f"{person.title()}'s favorite numbers are:")

   for num in number:
      print(f"\t{num}\n")