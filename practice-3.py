
# Write a function that accepts a list of items a person wants on a sandwich. 
# The function should have one parameter that collects as many items as the function call provides 

def accept_items(items : list) -> list:
    """
    This function accepts a list of items a person wants on a sandwich.
    """
    print("\nThe items for your sandwich are: ")

    # It should print a summary of the sandwich that's being ordered
    for item in items:
        print(item)
 

# Call the function three times using a different number of arguments each time.
accept_items(["Cheese", "Chicken", "Lettuce", "Tomatoes"])
accept_items(["Jam", "Peanut Butter"])
accept_items(["Cheese"])