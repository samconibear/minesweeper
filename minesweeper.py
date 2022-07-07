import random
from itertools import chain
import pickle

no_of_mines = 10
grid_dimensions = 10,10

training_cutoff = 0.5*(grid_dimensions[0]*grid_dimensions[1])

def generate_mines_grid(grid_dimensions, no_of_mines):
    no_of_positions = grid_dimensions[0]*grid_dimensions[1] - 1
    mines = random.sample(range(no_of_positions), k = no_of_mines)
    grid = []
    for y in range(grid_dimensions[1]):
        grid_layer = []
        for x in range(grid_dimensions[0]):
            cell = x+grid_dimensions[0]*(y)
            if cell in mines:
                grid_layer.append(1)
            else:
                grid_layer.append(0)
        grid.append(grid_layer)
    return grid

def generate_plain_grid(grid_dimensions):
    grid = []
    for y in range(grid_dimensions[1]):
        grid_layer = []
        for x in range(grid_dimensions[0]):
            cell = x+(grid_dimensions[0]*(y+1))
            grid_layer.append(0)
        grid.append(grid_layer)
    return grid

def check_surrounding():
    minesgrid = generate_mines_grid(grid_dimensions, no_of_mines)
    grid =  generate_plain_grid(grid_dimensions)
    for y in range(grid_dimensions[1]):
        for x in range(grid_dimensions[0]):
            for yi in range(3):
                for xi in range(3):
                    try:
                        if minesgrid[(y-1)+yi][(x-1)+xi] == 1:
                            if (y-1)+yi < 0:
                                break
                            if (x-1)+xi < 0:
                                break
                            grid[y][x] = grid[y][x]+1
                        if minesgrid[y][x] == 1:
                            grid[y][x] = 9
                    except:
                        pass
    return grid

def generate_display_grid(grid_dimensions):
    grid = []
    for y in range(grid_dimensions[1]):
        grid_layer = []
        for x in range(grid_dimensions[0]):
            cell = x+(grid_dimensions[0]*(y+1))
            grid_layer.append(10)
        grid.append(grid_layer)
    return grid

def random_choice(display):
    while True:
        x = random.choice(range(grid_dimensions[0]))
        y = random.choice(range(grid_dimensions[1]))
        if display[y][x] == 10:
            return x, y

def game():
    xtrain_data = []
    ytrain_data = []
    score = 0

    minefield = check_surrounding()
    display = generate_display_grid(grid_dimensions)
    
    run = True
    while run:
        #[print(i) for i in display]
        #print(f'-------------( SCORE = {score})-------------')

        ''' FOR PLAYER INPUT
        player_input_x = int(input('x: '))
        player_input_y = int(input('y: '))
        player_input = player_input_x, player_input_y
        '''

        ''' FOR RANDOM INPUT '''
        player_input = random_choice(display)

        y = player_input[1]
        x = player_input[0]

        display_1d = list(chain.from_iterable(display)) # converts the display to a 1D array
        cell_chosen = x + (y*grid_dimensions[0])

        xtrain_data.append(display_1d)
        ytrain_data.append(cell_chosen)

        surrounding = minefield[y][x]
        display[y][x] = surrounding
        if surrounding == 9:
            run = False
            #print('BOOM')
            return score, xtrain_data, ytrain_data
        else:
            score += 1
            if score == grid_dimensions[0]*grid_dimensions[1] - 1:
                print('holy shit you won')
                return score, xtrain_data, ytrain_data


def create_training_data():
    x_train, y_train = [], []
    k=0
    while k < 10_000_000:
        game1 = game()
        score = game1[0]
        xtrain_data = game1[1]
        ytrain_data = game1[2]
        if score >= training_cutoff:
            for turn in ytrain_data:
                y_train.append(turn)
            for turn in xtrain_data:
                x_train.append(turn)

        if k % 500_000 == 0:
            print('')
        if k % 100_000 == 0:
            print(f'{k} played - {len(x_train)} score {int(training_cutoff)}+', end=' | ')
        k += 1

    print('\nDONE')
    pickle.dump(x_train, open('x.p', 'wb'))
    pickle.dump(y_train, open('y.p', 'wb'))
    print(x_train)
#create_training_data()
'''
x = pickle.load(open('x.p', 'rb'))
y = pickle.load(open('y.p', 'rb'))
print(x[88])
print(y[88])
'''