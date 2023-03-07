# Recipe Manager

## Introduction:
In this project, you will be building a Recipe Manager using Python. A recipe manager is an application that helps users manage their collection of recipes, find new recipes, and organize ingredients. With this application, users can store and manage their favorite recipes, search for new recipes, and organize their ingredients.

## Real-life instances:
Recipe managers are widely used in our daily lives, from professional chefs who manage their recipes and menus, to home cooks who want to plan meals and grocery shopping. It can also help individuals with dietary restrictions or preferences to find recipes that fit their specific needs, such as gluten-free or vegetarian diets.

## What you will gain:
By building this project, you will learn how to work with JSON files, read and write data to files, and use Python functions to implement the different features of a recipe manager. You will also learn how to create user interfaces with console-based input and output, and how to manage program flow using conditional statements and loops.

## Your tasks:
You will be given a starter code that loads recipes from a JSON file and provides basic functionality for managing recipes. 
The load_recipes() function loads recipes from a JSON file, while the list_recipes() function lists all the recipes in the recipe book. 
You will need to implement two additional functions: search_by_ingredient() and display_instructions(). 
The search_by_ingredient() function should search for recipes that contain a specific ingredient and display them to the user. 
The display_instructions() function should display the instructions for a selected recipe.

## Hints:

### To implement the search_by_ingredient() function: 
You will need to prompt the user for an ingredient name and search through the list of recipes to find all the recipes that contain that ingredient. You can use a loop to iterate over the list of recipes and another loop to iterate over the list of ingredients for each recipe. Use the 'in' operator to check if the search ingredient is in the list of ingredients.

### To implement the display_instructions() function: 
You will need to prompt the user for the recipe they want to see the instructions for and display the instructions. Use the input() function to prompt the user for the recipe number and use the print() function to display the instructions. You can access the instructions for a recipe using the recipe['instructions'] key-value pair.

## Testing your code: 
To test your code, you can use the main() function provided in the starter code. Run the main() function to test your implementation and make sure it works as expected. Pictures of expected reselt can be found in results folder.

Note: You can add your own recipes to the JSON file or create a new JSON file to store your own recipes.