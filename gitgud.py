file = open("kyloth.txt", "w+")
git = ["you ", "gotta "]
gud = ["git ", "gud "]
yaknow = ["you ", "know "]
for p in yaknow:
    file.write(p)
for i in git:
    file.write(i)
for n in gud:
    file.write(n)
for n in gud:
    file.write(n)
for n in gud:
    file.write(n)
for p in yaknow:
    file.write(p)
for i in git:
    file.write(i)
for n in gud:
    file.write(n)
for n in gud:
    file.write(n)
for n in gud:
    file.write(n)
file.seek(0)
content = file.readlines()
file.seek(0)
file.close()
print (content)
