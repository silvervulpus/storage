file = open("kyloth.txt", "w+")
git = ["you ", "gotta "]
gud = ["git ", "gud "]
yaknow = ["you ", "know "]

for l in range (2):
    for p in yaknow:
        file.write(p)
    for i in git:
        file.write(i)
    for f in range (3):
        for n in gud:
            file.write(n)
        
file.seek(0)
content = file.readlines()
file.seek(0)
file.close()
print (content)

