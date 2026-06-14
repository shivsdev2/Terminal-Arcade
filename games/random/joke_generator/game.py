import os
import json
import random

AUTHOR = "Shivank Sharma"

def run():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "jokes.json")
    
    try:
        with open(json_path, "r") as file:
            data = json.load(file)
        
        jokes_list = data.get("jokes", [])
        
        if not jokes_list:
            print("No jokes found, please check for 'jokes.json' file in joke_generator directory.")
            return
        random_joke = random.choice(jokes_list)
        
        print("Here is a random joke for you!")
        print(f"Setup: {random_joke['setup']}")
        input("[ Press Enter to see the punchline]")
        print(f"Punchline: {random_joke['punchline']}\n")
        
    except FileNotFoundError:
        print(f"Error: Could not find jokes.json at {json_path}")
    except json.JSONDecodeError:
        print("Error: jokes.json contains invalid JSON formatting.")
