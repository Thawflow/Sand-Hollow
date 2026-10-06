n = int(input("Give me  a whole number: "))
if n % 2 == 0:
    print(n, "is even")
else:
    print(n, "is odd")

height = int(input("Your height in cm: "))
if height >= 140:
    print("Any roller coaster you like!")
elif height >= 120:
    print("You can ride the small coaster")
else:
    print("Try the carousel first, build some courage")