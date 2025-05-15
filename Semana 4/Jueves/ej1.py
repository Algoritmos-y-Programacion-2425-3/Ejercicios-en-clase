dictionary = {}
while True:
    key = input("Please enter what data do you want to enter eg. name, email,gender, phone (or exit if wanna exit):")
    if key == "exit":
        break
    value = input(f"Please enter your {key}:")
    dictionary[key] = value
    for key, value in dictionary.items():
        print(f"{key.title()}: {value}")
print("Your final data is:")
for key, value in dictionary.items():
        print(f"{key.title()}: {value}")
