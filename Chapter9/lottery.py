from random import choice
# Simulate real world lottery

ticketChoice = ['A', 'B', 'F', 'H', 'Z', 20, 3, 4, 6, 9, 1, 15, 42, 76, 21]

winningTicket = []

while len(winningTicket) < 4:
    ticketPull = choice(ticketChoice)

    if ticketPull not in winningTicket:
        print(f"We pulled a {ticketPull}")
        winningTicket.append(ticketPull)

print(f"The winning ticket is {winningTicket}")