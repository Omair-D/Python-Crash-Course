# Define function to accept items person wants in sandwich
# Make it so it can be as many items as they want
def sandwich(*items):
    print(f"\nMaking a sandwich with:")
    for item in items:
        print(f"- {item}")


sandwich('turkey', 'lettuce', 'tomatoes')
sandwich('american cheese')
sandwich('peanut butter', 'jelly')