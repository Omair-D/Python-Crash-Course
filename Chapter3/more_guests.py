guestList = ['kanye west', 'drake', 'lil wayne']

# print invites using list

invite = ", please join us for dinner!"

# print who cannot make it to dinner and remove from list
noShow = 'lil wayne'
guestList.remove(noShow)

print(f"{noShow.title()} cannot make it to dinner tonight at 8 P.M")

# Add new member to list in place of the one we removed
guestList.append('beyonce')

print(f"{guestList[0].title()}{invite}")
print(f"{guestList[1].title()}{invite}")
print(f"{guestList[2].title()}{invite}")

print('-------------------------------')

print("Attention everyone, I found a bigger table for more guests.")

guestList.insert(0, 'ken carson')
guestList.insert(2, 'jaden smith')
guestList.append('brent faiyaz')

print(f"{guestList[0].title()}{invite}")
print(f"{guestList[1].title()}{invite}")
print(f"{guestList[2].title()}{invite}")
print(f"{guestList[3].title()}{invite}")
print(f"{guestList[4].title()}{invite}")
print(f"{guestList[5].title()}{invite}")

