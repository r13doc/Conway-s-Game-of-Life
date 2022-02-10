import numpy as np

def find(cell, generator):
    cell = np.array(cell)
    gen = generator
    # return back cell if no generations
    if gen == 0:
        return cell.tolist()
    
    def cells(cell, gen):
        cell = np.pad(cell, pad_width=2, mode='constant',
                         constant_values=0)
        copy_cell = np.zeros_like(cell)
        for i in range(1, cell.shape[0] - 1):
            for j in range(1, cell.shape[1] - 1):
                # check summ all eight neighbours
                neighbours = (cell[i-1][j-1] + cell[i-1][j] + cell[i-1][j+1] +
                             cell[i][j-1] + cell[i][j+1] +
                             cell[i+1][j-1] + cell[i+1][j] + cell[i+1][j+1])
                # add new values to new array
                for k in range(1, copy_cell.shape[0] - 1):
                    for l in range(1, copy_cell.shape[1] - 1):
                        if cell[i][j] == 1 and 1 < neighbours < 4:
                            copy_cell[i][j] = 1
                        elif cell[i][j] == 0 and neighbours == 3:
                            copy_cell[i][j] = 1
                        else:
                            copy_cell[i][j] = 0
        
        # check number generations
        while gen > 1:
            gen = gen - 1
            return cells(cropped(copy_cell), gen)
            
        return (cropped(copy_cell)) # .tolist() from numpy to list
        
    
    def cropped(arr):
        coords = np.argwhere(arr)
        x_min_cell, y_min_cell = coords.min(axis=0)
        x_max_cell, y_max_cell = coords.max(axis=0)
        crop = arr[x_min_cell:x_max_cell+1, y_min_cell:y_max_cell+1]                   
        return crop
    
    return cells(cell, gen)


cell = [[1, 1, 1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1, 1, 1]]
gen = 40
find(cell, gen)
