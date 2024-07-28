guestList = ['kanye west', 'drake', 'lil wayne']

# print invites using list

invite = ", please join us for dinner!"

noShow = 'lil wayne'
guestList.remove(noShow)

print(f"{noShow.title()} cannot make it to dinner tonight at 8 P.M")

guestList.append('beyonce')

print(f"{guestList[0].title()}{invite}")
print(f"{guestList[1].title()}{invite}")
print(f"{guestList[2].title()}{invite}")


