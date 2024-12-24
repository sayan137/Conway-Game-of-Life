import pygame

#initialization
pygame.init()

#useful constants 
black = (0, 0, 0)
grey = (128, 128, 128)
yellow = (255, 255, 0)
width, height = 800, 800
tile_size =  20
grid_height = height // tile_size
grid_width = width // tile_size
fps = 60 

#defining the pygame window as screen 
screen = pygame.display.set_mode((width, height))

#defining the clock 
clock = pygame.time.Clock()

def draw_grid(positions):
    for position in positions:
        col, row = position                                                     #position is the location of position in terms of grid system what i have derived
        top_left = (col * tile_size, row * tile_size)
        pygame.draw.rect(screen, yellow, (*top_left, tile_size, tile_size))                 #transforming the location mapping system from grid to pygame system thus making a rectangle 

    for row in range (grid_height):                                                         #drawing the horizontal lines
        pygame.draw.line(screen, black, (0, row * tile_size), (width, row * tile_size))

    for col in range (grid_width):                                                          #drawing the vertical lines
        pygame.draw.line(screen, black, (col * tile_size, 0), (col * tile_size, height))

def gol_algo(positions):
    all_neighbors = set()
    new_positions = set()

    for position in positions:                          #iterating in the cells' positions what had been selected on window
        neighbors = get_neighbors(position)             # getting the neighbors of that points
        all_neighbors.update(neighbors)                 #adding neighbors of every point upon full iteration of this loop

        neighbors = list(filter(lambda x : x in positions, neighbors))      #finding if the neighbors is already in the position what had been selected

        if len(neighbors) in [2,3]:                            #now neighbor means the live cells what had been selected so if number of alive cell is 2 or 1 in neighbor it will be added to upcoming frame of living cells
            new_positions.add(position)

    for position in all_neighbors:                          # now iterating over the neighbors of every points
        neighbors = get_neighbors(position)                 #getting pos of every neighbor of neighbors
        neighbors = list(filter(lambda x : x in positions, neighbors))      # counting if the neighbor had been in the living cell 

        if len(neighbors) == 3 :                            # if the living cell count is exact 3 then it wil be given life
            new_positions.add(position)

    return new_positions

def get_neighbors(pos):
    x, y = pos
    neighbors = []
    for dx in [-1, 0, 1]:
        if x + dx < 0 or x +dx > grid_width:                #there is no point of launching game outside of the window and a safeside playing by making dy greater than tiles 
            continue 
        for dy in [-1, 0, 1]:
            if y + dy < 0 or y + dy > grid_height:
                continue
            if dx == 0 and dy == 0:                     # if dx=dy=0 then its the same cell !
                continue

            neighbors.append((x + dx , y + dy))         # storing the address touple of neighbors
    return neighbors

def main():
    running = True
    playing = False
    count = 0                                   # just a variable to have a information on how many seconds have been passed
    update_frequency = 60                      # in every 120/ fps = 2 sec the positions will be updated

    positions= set()
    while running:
        clock.tick(fps)                     #maximum 'fps' times the loop will run

        if playing: 
            count += 1

        if count >= update_frequency:
            count = 0
            positions = gol_algo(positions)

        pygame.display.set_caption("Playing" if playing else "paused")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False             #upon clicking the close the loop will stop 

            if event.type == pygame.MOUSEBUTTONDOWN:                    #the grid will be alive or dead with click of mouse
                x, y = pygame.mouse.get_pos()
                col = x // tile_size                                    #coverting the coordinate system from pygame to our own grid system consists of cells
                row = y // tile_size
                pos = (col, row)

                if pos in positions:                #positions are the list of the address touples of living cells
                    positions.remove(pos)
                else:
                    positions.add(pos)
      
            if event.type == pygame.KEYDOWN:                        #upon pressing space game will be stopped or play
                if event.key == pygame.K_SPACE:
                    playing = not playing

                if event.key == pygame.K_c:                         #c will clear the screen 
                    positions = set()
                    playing = False
                    count = 0

        screen.fill(grey)            
        draw_grid(positions)
        pygame.display.update()


    pygame.quit()

if __name__ == "__main__":
    main()


