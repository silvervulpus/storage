file = open("characters.txt", "r")
character_names = file.read()
for n in character_names:
    print (n)
file.seek(0)
character_list = file.readlines()
for i in character_list:
    print (i)
character_list_length = len(character_list)
character_names_length = len(character_names)
file.seek(0)
file.close()
file = open("characters.txt", "w")
file.write("add this line ")
file.write("Add this line also")
file.close()
lines = ["line one", "line two", "line three"]
file = open("characters.txt", "w")
for item in lines:
    file.write(item + "/n")
file.close()
print (character_names)
print (character_list)
print (character_list_length)
print (character_names_length)

