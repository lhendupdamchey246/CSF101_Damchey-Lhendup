'''number = '23'
x = float(number)
print(x)

x = 23
y = 25.0
print(x + y)
z_float = float(x + y)
print(z_float)
v = int(y)
print(v)
s = '23.2'
x = float(s)
print(x)
word = "python"
x = list(word)
print(x)
y = tuple(word)
print(y)

x = 15
y = 45
print(f"x < 45 and y > 15: {x < 45 and y > 15}")

name = "Sayma"
print(f"welcome: {name} ")
x = list(name)
print(x)

#Basics syntax
#1/While loop
spam = 0
while spam < 5:
    print('Hello World!')
    spam = spam + 1

while True:
    print("Please type your name. ")
    name = input()
    if name == "your name":
        break
print("Thank you!")

while True:
    print("whoe are you?")
    name = input()
    if name != "joe!":
        continue
    print("hello joe, what is the password?")
    password = input()
    if password == "swordfish":
        break
print("Access Granted")

#Loop
print("my name is")
for i in range(5):
    print("Jimmy Five Times ({})".format(str(i)))
print(i)


# For else statement
for i in [1, 2, 3, 4, 5]:
    if i == 3:
        break
else:
    print("done")'''

def our_function():
    print("Hello from a function")

our_function()
