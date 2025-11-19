"""
Author: Arlo Virta
Date: 2025-11-17
Description: Prompts the user for ingredients in making a sandwich
"""

import pyinputplus as pyip

BREAD_PRICES = { "french": 2.99, "whole grain": 3.49, "brioche": 3.99, "sourdough": 2.99 }
PROTEIN_PRICES = { "chicken": 0.99, "turkey": 0.99, "ham": 1.29, "roast beef": 1.69 }
CHEESE_PRICES = { "provolone": 1.29, "swiss": 1.69, "cheddar": 1.29, "mozzarella": 1.99 }
TOPPING_PRICES = { "mayo": 0.29, "mustard": 0.29, "lettuce": 0.19, "tomato": 0.29 }

def formatPriceDict(prices):
    compiled = {}

    for (name, price) in prices.items():
        compiled[name] = f"{name.title():<16} ${price:>10,.2f}"
    
    return compiled

# stinky code isolated to this function
def inputMenuIndexed(choices, **keyword_args):
    choice_response = pyip.inputMenu(list(choices.values()), **keyword_args)

    # convert formatted response to choice
    index = list(choices.values()).index(choice_response)
    return list(choices.keys())[index]

def print_subtotal(subtotal):
    print("")
    print(f"Current subtotal: ${subtotal:,.2f}")

def ask_sandwich_construction():
    sandwich_price = 0

    bread_options = formatPriceDict(BREAD_PRICES)
    protein_options = formatPriceDict(PROTEIN_PRICES)
    cheese_options = formatPriceDict(CHEESE_PRICES)


    bread_type = inputMenuIndexed(bread_options, numbered=True, prompt="Please select a bread type:\n")
    sandwich_price += BREAD_PRICES[bread_type]
    print_subtotal(sandwich_price)

    protein_type = inputMenuIndexed(protein_options, numbered=True, prompt="Please select a protein:\n")
    sandwich_price += PROTEIN_PRICES[protein_type]
    print_subtotal(sandwich_price)

    cheese_type = None
    if pyip.inputYesNo("Would you like cheese (y/n)?- ") == "yes":
        cheese_type = inputMenuIndexed(cheese_options, numbered=True, prompt="Please select a cheese:\n")
        sandwich_price += CHEESE_PRICES[cheese_type]
        print_subtotal(sandwich_price)
    

    topping_types = []

    topping_options = formatPriceDict(TOPPING_PRICES)
    topping_options[None] = "[[continue]]" # add "continue" option to end
    
    while len(topping_types) < len(TOPPING_PRICES):
        topping = inputMenuIndexed(topping_options, numbered=True, prompt="Add unlimited toppings:\n")
        if topping == None: break

        if topping in topping_types:
            print("Topping already added!")
        else:
            topping_types.append(topping)
            topping_options[topping] += " (ADDED)"
            
            sandwich_price += TOPPING_PRICES[topping]
            print_subtotal(sandwich_price)
    
    sandwich = {
        "bread": bread_type,
        "protein": protein_type,
        "cheese": cheese_type,
        "toppings": topping_types,
        "price": sandwich_price
    }

    return sandwich

def print_sandwich_receipt(index, sandwich):
    bread = sandwich["bread"]
    protein = sandwich["protein"]
    cheese = sandwich["cheese"]
    toppings = sandwich["toppings"]
    price = sandwich["price"]

    print(f'{f"Sandwich #{index + 1}":^32}')
    item_format = "{:<20} ${:>10,.2f}"

    print(item_format.format(bread.title(), BREAD_PRICES[bread]))

    print(item_format.format(protein.title(), PROTEIN_PRICES[protein]))

    if cheese != None:
        print(item_format.format(cheese.title(), CHEESE_PRICES[cheese]))
    
    for topping in toppings:
        print(item_format.format(topping.title(), TOPPING_PRICES[topping]))
    
    print("")
    print(item_format.format("Subtotal", price))
    print("=" * 32)

def main():
    sandwich_count = pyip.inputInt("How many sandwiches do you want?- ", min=1)
    sandwiches = []
    total = 0

    for i in range(sandwich_count):
        print("")
        print("=" * 32)
        print(f'{f"Sandwich #{i + 1}":^32}')
        sandwich = ask_sandwich_construction()
        sandwiches.append(sandwich)

        print("=" * 32)
        print(f"Sandwich subtotal:   ${sandwich['price']:>10,.2f}")

        total += sandwich["price"]
    
    print("\nReceipt:")
    print("=" * 32)
    for i in range(sandwich_count):
        print_sandwich_receipt(i, sandwiches[i])
    
    print(f"{'Total':<20} ${total:>10,.2f}")

main()