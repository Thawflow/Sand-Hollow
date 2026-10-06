#1
n = int(input("Give me  a whole number: "))
if n % 2 == 0:	# 如果能够被2整除
    print(n, "is even")
else:
    print(n, "is odd")
    
#2
t = float(input("Temperature: "))
if t>= 100:
    print("Boiling hot")
elif t >= 40:
    print("Warm")
else:
    print("Cool")
