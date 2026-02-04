
#  Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

fav_song = {}

for i in range(4):
    name = input(f"enter name of friend {i+1}: ")
    song = input("enter favorite song of his/her: ")
    fav_song.update({name : song})

print("The favorite song of friends are:", fav_song)


