import random

AUTHOR = "Shivank Sharma"

ALPHABETS = ['A','B','C','D','E', 'F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def run():
    print('Translate your message to alien language!')
    while True:
        message = input("Enter your message (or type 'quit' to exit): ")
        if message.lower() in ['quit', 'q', 'exit']:
            print("Exiting Alien Translator. Goodbye!")
            break
        
        translated_message = []
        for char in message:
            if char.upper() in ALPHABETS:
                 #replace with random Alphabetss
                translated_message.append(random.choice(ALPHABETS))
            else:
                # let non alphabets be the same
                translated_message.append(char)
        
        print("Translated to Alien Language: " + ''.join(translated_message) + "\n")

run()