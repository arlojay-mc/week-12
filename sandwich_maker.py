"""
Author: Arlo Virta
Date: 2025-11-17
Description: Prompts the user for ingredients in making a sandwich
"""

import pyinputplus as pyip

BREAD_TYPES = [ "french", "whole grain", "brioche", "sourdough" ]
PROTEIN_TYPES = [ "chicken", "turkey", "ham", "roast beef" ]
CHEESE_TYPES = [ "provolone", "swiss", "cheddar", "mozzarella" ]
EXTRA_TOPPINGS = [ "mayo", "mustard", "lettuce", "tomato" ]

def ask_sandwich_construction():
    print("What type of bread?")
    bread_type = pyip.inputChoice(BREAD_TYPES)

    print("What type of protein?")
    protein_type = pyip.inputChoice(PROTEIN_TYPES)

    cheese_type = None
    if pyip.inputYesNo("Would you like cheese (y/n)?- "):
        cheese_type = pyip.inputChoice(CHEESE_TYPES)
    
    toppings = []

    for topping in EXTRA_TOPPINGS:
        if pyip.inputYesNo(f"Would you like {topping} on your sandwich?- ") == "yes":
            toppings.append(topping)
    
    sandwich = {
        "bread": bread_type,
        "protein": protein_type,
        "cheese": cheese_type,
        "toppings": toppings
    }

    return sandwich

def print_sandwich(sandwich):
    bread = sandwich["bread"]
    protein = sandwich["protein"]
    cheese = sandwich["cheese"]
    toppings = sandwich["toppings"]
    
    print(bread.capitalize(), end="")
    print(" bread with ", end="")
    print(protein.lower(), end="")

    if cheese == None:
        print(", no cheese,", end="")
    else:
        print(", " + cheese.lower() + " cheese,", end="")
    
    print(" with the toppings ", end="")
    print(*toppings, sep=", ", end=".\n")


def main():
    sandwich_count = pyip.inputInt("How many sandwiches do you want?- ", min=1)
    sandwiches = []

    for i in range(sandwich_count):
        print(f"=== Sandwich #{i + 1} ===")
        sandwich = ask_sandwich_construction()
        sandwiches.append(sandwich)

        print("Here's your sandwich:")
        print_sandwich(sandwich)
    
    print("=" * 32)
    print(f"Here's a summary of all {sandwich_count} sandwich(es):")
    for i in range(sandwich_count):
        print(f"Sandwich #{i + 1}: ", end="")
        print_sandwich(sandwiches[i])

main()