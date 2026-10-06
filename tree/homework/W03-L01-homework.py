#1
score = int(input("What score did you get?"))
if score >= 60:
    print("Passed!")
if score >= 95:
    print("Excellent!")
print("Done")

#2
print(10 == 10) #true
print("10" == 10) #false
print(4 != 5) #true

#3
age = int(input("Your age?"))
if age >= 18:
    print("Enjoy the show!")
    
#4
cat_food = 2
if cat_food <3:
    print("Cat food is running low - time to stock up")

#5
secret = "thawpaw"
password = input("Password?")
if secret == password:
    print("Welcome back, Clan leader")
