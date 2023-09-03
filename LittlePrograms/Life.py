import copy, random, sys, time 

WIDTH = 79 
HEIGHT = 20 

ALIVE = 'O'
DEAD = ' '


nextCells = {} 
# Put random dead and alive into nextCells
for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0, 1) == 0:
            nextCells[(x, y)] = ALIVE
        else:
            nextCells[(x, y)] = DEAD

while True: 
    print('\n' * 50) # draw a new screen 
    cells = copy.deepcopy(nextCells)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x, y)], end='')
        print() 
    print('Press Ctrl-C to quit.')

    # Calculate the next steps' cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            left    = (x - 1) % WIDTH
            right   = (x + 1) % WIDTH
            top     = (y - 1) % HEIGHT
            bottom  = (y + 1) % HEIGHT

            # Count the number of living neighbors 
            numNeighbors = 0 
            if cells[(left, top)] == ALIVE:
                numNeighbors += 1
            if cells[(x, top)] == ALIVE:
                numNeighbors += 1 
            if cells[(right, top)] == ALIVE:
                numNeighbors += 1 
            if cells[(left, y)] == ALIVE: 
                numNeighbors += 1
            if cells[(right, y)] == ALIVE:
                numNeighbors += 1
            if cells[(left, bottom)] == ALIVE:
                numNeighbors += 1
            if cells[(x, bottom)] == ALIVE:
                numNeighbors += 1
            if cells[(right, bottom)] == ALIVE:
                numNeighbors += 1

            # Set cell ALIVE OR DEAD based off Game of life rules 
            if cells[(x, y)] == ALIVE and (numNeighbors == 2 or numNeighbors ==3):
                nextCells[(x, y)] = ALIVE
            elif cells[(x, y)] == DEAD and numNeighbors == 3:
                nextCells[(x, y)] = ALIVE
            else: 
                nextCells[(x, y)] = DEAD

    try:
        time.sleep(1) 
    except KeyboardInterrupt:
        print("Conway's game of life")
        sys.exit()