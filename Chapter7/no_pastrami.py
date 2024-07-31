sandwich_orders = ['pastrami', 'pastrami', 'bologna sandwich', 'tuna sandwich', 'chicken sandwich', 'pastrami']
finished_sandwiches = []

print("The deli has ran out of pastrami!")

# Use loop to add sandwich orders to empty list but have no occurence of 'pastrami'
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    finished_sandwiches.append(current_sandwich)
    print(f"I made your {current_sandwich}!")

print("---All orders complete---")
print(finished_sandwiches)