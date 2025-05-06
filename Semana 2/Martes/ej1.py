print("Welcome to Pizzeria Bella Napoli")
option = input("Please enter a option:\n1-Vegetarian\n2-No Vegetarian\n->")
ingredient = ""
if option == "1":
    ingredient_option = input("Please enter your special ingredient:\n1-Pimiento\n2-Tofu\n->")
    if ingredient_option == "1":
        ingredient = "Pimiento"
    else:
        ingredient = "Tofu"
elif option == "2":
    ingredient_option = input("Please enter your special ingredient:\n1-Peperoni\n2-Jamon\n3-Salmon\n->")
    if ingredient_option == "1":
        ingredient = "Peperoni"
    elif ingredient_option == "2":
        ingredient = "Jamon"
    else:
        ingredient = "Salmon"
    
if option == "1":
    print(f"The pizza is vegetarian and have: Tomate, Mozzarella y {ingredient}")
else:
    print(f"The pizza is no vegetarian and have: Tomate, Mozzarella y {ingredient}")