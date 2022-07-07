#!/usr/bin/env python
# coding: utf-8

# In[104]:


import random

no_of_mines = 10
grid_dimensions = 10,10

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

    minesgrid[x][y]
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

[print(i) for i in grid]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




