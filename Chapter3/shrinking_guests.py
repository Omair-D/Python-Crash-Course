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

print('---------------------')
print('I can only invite two people for dinner')

# Pop guests from list and print message

guestList.pop(1)

print(guestList.pop(1).title(), "you are uninvited")

guestList.pop(2)

print(guestList.pop(2).title(),"you are uninvited")

# Last two names invite message

print(guestList[0].title(), "you are still invited")
print(guestList[1].title(), "you are still invited")

print(guestList)

# Clear list

del guestList[1]
del guestList[0]

print(guestList)
