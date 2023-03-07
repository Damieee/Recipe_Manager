import json

# Load recipes from a JSON file
def load_recipes(filename):
    with open(filename, 'r') as f:
        recipes = json.load(f)
    return recipes

old_recipe=load_recipes("recipe.json")

# Save recipes to a JSON file
def save_recipes(filename):
    with open(filename, 'w') as f:
        json.dump(old_recipe, f)

saved_recipes=save_recipes("new_recipe.json")

def load_new_recipes(filename):
    with open(filename, 'r') as f:
        recipes = json.load(f)['recipes']

    return recipes

# Display a list of all recipes
def list_recipes(recipes):
    print("Recipe Book:")
    for i, recipe in enumerate(recipes):
        print(f"{i+1}. {recipe['name']}")

# Search for recipes by ingredient
def search_by_ingredient(recipes):
    search_ingredient = input("Enter ingredient to search for: ")
    
    "TODO"


# Display instructions for a recipe
def display_instructions(recipe):
    print(f"\nInstructions for {recipe['name']}:\n")

    "TODO"
    

# Main program loop
def main():
    recipes=load_new_recipes(filename="new_recipe.json")
    while True:
        print("\nWhat would you like to do?")
        print("1. List all recipes")
        print("2. Search for recipes by ingredient")
        print("3. Display instructions for a recipe")
        print("4. Quit")
        choice = input("\nEnter your choice: ")
        print("")
        if choice == '1':
            list_recipes(recipes)
        elif choice == '2':
            search_by_ingredient(recipes)
        elif choice == '3':
            list_recipes(recipes)
            print("")
            recipe_choice = int(input("Enter the number of the recipe you want to see the instructions for: "))
            if 1 <= recipe_choice <= len(recipes):
                display_instructions(recipes[recipe_choice - 1])
            else:
                print("Invalid recipe number.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
