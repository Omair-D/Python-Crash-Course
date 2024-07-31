sandwich_orders = ['turkey sandwich', 'bologna sandwich', 'tuna sandwich', 'chicken sandwich']
finished_sandwiches = []

# Use a loop to print out a message with sandwich and move it into finished_sandwiches list
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)
    
# After loop print message
print('---All orders complete---')
print(finished_sandwiches)