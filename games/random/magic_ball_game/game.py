import random

AUTHOR = "Shivank Sharma"

def run():
    RANDOM_ANSWER = [
        'Yes', 'No', 'Maybe', 'Ask again later', 'Definitely', 
        'I have no idea', 'It is certain', 'Very doubtful', 
        'Without a doubt', 'Better not tell you now', 'My sources say no', 
        'Outlook good', 'Reply hazy try again', 'Concentrate and ask again', 
        'Do not count on it', 'It is decidedly so', 'Most likely', 
        'My reply is no', 'Outlook not so good', 'Signs point to yes', 
        'As I see it, yes', 'Yes - definitely', 'You may rely'
    ]
    
    user_input = input("Enter a question: ")
    
    program_response = random.choice(RANDOM_ANSWER)
    
    return program_response
