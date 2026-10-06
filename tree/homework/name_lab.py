# PROJECT A
family_name = input("Your family name: ")
given_name = input("Your given name: ")
full_name = given_name + " " + family_name
print(f"{"Name Report":^20}")
print(f"Your full name is {full_name}.")
print(f"{full_name.upper()}")
print(f"There are {len(full_name)} letters in our name")
print(f"First letter is {full_name[0]}")
print(f"Hide your family name: {full_name.replace(family_name,"*")}.")
print(f"Any a in your name: {"a" in full_name.lower()}")
