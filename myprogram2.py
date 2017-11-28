'''
def age_foo(age):
    new_age = (age) + 50
    return new_age

age = float(input("Enter your age?: "))

if age < 150:
    print(age_foo(age))
else:
    print ("You are far too old")
'''


def Cel_to_Fahr(c):
    if c <= -273.15:
        return ("Invalid Input")
    else:
        f = c*9/5 + 32
        return f
tempuratures = [100, 10, 28, -287, -27]
for c in tempuratures:
    print (Cel_to_Fahr(c))
    cConvert = str(Cel_to_Fahr(c))
    file = open("ftoc.txt", "w+")
    for l in cConvert:
        file = open("ftoc.txt", "w+")
        file.write(cConvert)
        file.seek(0)
        content = file.readlines()
        file.seek(0)
        print(content)
        file.close()

'''
def Length_of_String(f):
    length = f
    return len(f)
f = input("Input a string here for its length ")
if type(f) == int:
    print ("We cannot use len on an int")
elif type(f) == float:
    print ("We cannot use len on a float")
print (Length_of_String(f))
'''
