import random

AUTHOR = "Shivank Sharma"

def generate_code():
    return "".join(str(random.randint(0, 9)) for x in range(4))

def get_valid_guess():
    while True:
        guess = input("Enter your 4-digit guess: ").strip()
        if len(guess) == 4 and guess.isdigit():
            return guess
        print("Please enter exactly 4 digits (e.g., 1234).")

def check_guess(secret, guess):
    correct_positions = 0
    correct_digits = 0
    
    secret_matched = [False] * 4
    # it is something like secret_matched = [False, False, False, False]
    guess_matched = [False] * 4
    
    for i in range(4):
        if guess[i] == secret[i]:
            correct_positions += 1
            secret_matched[i] = True
            guess_matched[i] = True
            
    for i in range(4):
        if not guess_matched[i]:
            for j in range(4):
                if not secret_matched[j] and guess[i] == secret[j]:
                    correct_digits += 1
                    secret_matched[j] = True
                    break
                    
    return correct_positions, correct_digits

def run():
    print("=======================================")
    print("      Welcome to CODE CRACKER!         ")
    print("=======================================")
    print("I have generated a secret 4-digit code.")
    print("Can you crack it? You have 10 attempts.")
    print("---------------------------------------")
    
    secret_code = generate_code()
    attempts = 10
    
    for attempt in range(1, attempts + 1):
        print(f"\nAttempt {attempt}/{attempts}")
        guess = get_valid_guess()
        
        positions, digits = check_guess(secret_code, guess)
        
        if positions == 4:
            print(f"\nCongratulations! You cracked the code: {secret_code}")
            return
        
        print(f"Correct Positions: {positions}")
        print(f"Correct Digits (wrong position): {digits}")
        
    print(f"\nYou ran out of attempts.")
    print(f"The secret code was: {secret_code}")