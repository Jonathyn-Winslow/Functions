import pygame # must be at beginning of code

def load_map(filename):
    """This takes the maze text file and turns it into a list for the GUI"""
    maze = []
    with open(filename, 'r') as file:
        for line in file:
            string_values = line.strip().split()
                
            ints = []
            for n in string_values:
                numbers = int(n)
                ints.append(numbers)

            maze.append(ints)
    
    return maze



def start_pos(maze):
    """finds the starting position of the player"""
    for y in range(len(maze)): # goes through the rows of the maze
        for x in range(len(maze[0])): # goes through the columns. we need to do this because this is a 2D array
            if maze[y][x] == 3: # 3 is the player
                player = (x, y) # creates a tuple with the players location
                maze[y][x] = 0 # sets the player value to empty space to ensure the collision check doesn't get confused
                return player # returns the tuple
            

            
keys = pygame.key.get_pressed() #must be in the while running loop to work aka game loop
def move(position, direction, maze):
    """filler"""
    x, y = position
    dx, dy = direction

    new_x = x + dx
    new_y = y + dy

    if maze[new_y][new_x] != 1 and maze[new_y][new_x] != 5:
        return (new_x, new_y)
    
    return position
    


def get_direction(keys):
    """Utilizes pygame to take arrow key inputs and turns them into a direction tuple"""
    if keys[pygame.K_UP]:
        return (0, -1)
    elif keys[pygame.K_DOWN]:
        return (0, 1)
    elif keys[pygame.K_LEFT]:
        return (-1, 0)
    elif keys[pygame.K_RIGHT]:
        return (1, 0)
    else:
        return (0, 0)
    


def direction_scramble(keys):
    """Uses pygame to create direction tuples based on arrow key inputs but scrambles the directions"""
    if keys[pygame.K_UP]:
        return (1, 0)
    elif keys[pygame.K_DOWN]:
        return (-1, 0)
    elif keys[pygame.K_LEFT]:
        return (0, 1)
    elif keys[pygame.K_RIGHT]:
        return (0, -1)
    else:
        return (0, 0)
    


def wall_swap(maze, position):
    """will swap all walls and empty spaces without effecting anything else"""
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if (x, y) == position:
                continue
            elif maze[y][x] == 1:
                maze[y][x] = 0
            elif maze[y][x] == 0:
                maze[y][x] = 1
            
    return maze



def load_level(level):
    """will load the maze and starting position for the level"""
    if level == 1:
        filename = 'maze1.txt'
    elif level == 2:
        filename = 'maze2.txt'
    elif level == 3:
        filename = 'maze3.txt'

    maze = load_map(filename)
    position = start_pos(maze)

    return maze, position



def switch_level(level, position):
    """switches the level based on the player's position"""
    if level == 1:
        if position == (x1, y1): # *****will put actual cordinates later when we have the maze
            level = 2
            return level
    elif level == 2:    
        if position == (xA, yA):
            level = 1
            return level
        elif position == (xB, yB):
                level = 3
                return level
    elif level == 3:
        if position == (x3, y3):
            level = 2
            return level
    
    return level



def win(position, level, key_state):
    """checks if the player has won the game by being in the correct position with the key"""
    if position == (x,y) and level == 1 and key_state == True:
        return True
    
    return False



import time
time_limit = 120
start_time = time.time() # all 3 at beginning of code

def time_check(start_time, time_limit):
    """checks if the time limit has been exceeded"""
    current_time = time.time()
    elapsed = current_time - start_time

    if elapsed > time_limit:
        return True
    
    return False



def key_pickup(maze, position, key_state, level): # used to place key, and check if it is picked up

    if level == 3 and not key_state:
        key_x, key_y = 5, 5  # random coords, just change them
    
    # This checks if the player is on the key
        if position == (key_x, key_y):
            key_state = True
            maze[key_y][key_x] = 0
                    
    return key_state, maze