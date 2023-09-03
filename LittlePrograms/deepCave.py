""" Created by Al Sweigart, the God of Python Books"""

import random, sys, time 

# Set up Constants 
WIDTH = 70 # Change this to 10 or 30 
PAUSE_AMOUNT = 0.05 # Try changing this to 0 or 1.0 

print('Deep Cave')
print('Press Ctrl-C to stop')
time.sleep(2)

leftWidth = 20 
gapWidth = 10 

while True:
    # Display the tunnel segment 
    rightWidth = WIDTH - gapWidth - leftWidth
    print(('#' * leftWidth) + (' ' * gapWidth) + ('#' * rightWidth))
    
    # Check for Ctrl-C press during the brief pause 
    try:
        time.sleep(PAUSE_AMOUNT)
    except KeyboardInterrupt:
        sys.exit()

    # Adjust the left side width
    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and leftWidth > 1:
        leftWidth = leftWidth - 1 # Decrease left side width
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
        leftWidth = leftWidth + 1 # Increase the left side width
    else:
        pass # Do nothing to change in left side width

    # Adjust the gap width 
    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and gapWidth > 1:
        gapWidth = gapWidth - 1 
    elif diceRoll == 2 and leftWidth + gapWidth < WIDTH - 1:
        gapWidth = gapWidth + 1
    else:
        pass 