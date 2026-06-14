import time
import sys
import os


if os.name == 'nt':
    import msvcrt
else:
    import select

AUTHOR = "Shivank Sharma"

def check_keypress():
    """Detects a keypress instantly without blocking the code loop"""
    if os.name == 'nt': 
        if msvcrt.kbhit():
            msvcrt.getch()  # Clears the key from the buffer so it doesn't spill into your terminal
            return True
    else:  # For Linux / macOS
        # Checks if system standard input has data waiting
        if select.select([sys.stdin], [], [], 0.0)[0]:
            sys.stdin.readline()  # Clears the line from the buffer
            return True
    return False

def run():
    print("-----------------------------------------")
    print("Rules: Fast moving numbers, press ANY KEY at 100\n")
    
    input("Press [ENTER] to start the chaotic rush...")
    print("\nGO! Press ANY KEY to stop counter.")
    
    # flush accidental keys pressed during initial text
    if os.name == 'nt':
        while msvcrt.kbhit():
            msvcrt.getch()
    else:
        # lets input settle
        time.sleep(0.2)
        sys.stdin.flush()

    counter = 0
    
    while True:
        counter += 1
        print(f"\rCurrent Number: {counter}   ", end="", flush=True)
        
        time.sleep(0.01) 
        
        # breaks the moment key pressed
        if check_keypress():
            break

    difference = abs(100 - counter)
    
    print("\n-----------------------------------------")
    print(f"Stopped! You hit: {counter}")
    
    if difference == 0:
        print("Perfect! You hit exactly 100!")
    elif difference <= 3:
        print("Really close!")
    elif difference <= 10:
        print("Good effort")
    else:
        print("Not close buddy")
        
    print(f"Your variance: {counter - 100:+d}")
    print("-----------------------------------------")

