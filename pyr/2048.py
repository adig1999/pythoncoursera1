"""
Clone of 2048 game.
"""

import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    nline=[]
    itr=0
    while itr < len(line):
        #making the new list
        nline.append(0)
        itr += 1


    key=0
    for dummy_j in line:
        #inserting elements
        if dummy_j != 0:
            nline[key] = dummy_j
            key += 1


    task=0
    while task < len(line)-1:
        #shifting
        if(nline[task] == 0):
            break;
        if nline[task] == nline[task+1]:
            nline[task]*=2
            nline[task+1]=0
            task+=2
        else:
            task+=1


    fline=[]
    itf=0
    while itf < len(nline):
        #final list
        fline.append(0)
        itf += 1

    kar=0
    for dummy_j in nline:
        #shifting into final list
        if dummy_j != 0:
            fline[kar] = dummy_j
            kar += 1


    return fline

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, _gridheight_, _gridwidth_):
        # replace with your code
        self._gridheight_=_gridheight_
        self._gridwidth_=_gridwidth_
        self._grid_={}

        up_list = [(0, col) for col in range(self._gridwidth_)]
        down_list = [(self._gridheight_-1, col) for col in range(self._gridwidth_)]
        left_list = [(row, 0) for row in range(self._gridheight_)]
        right_list = [(row, self._gridwidth_-1) for row in range(self._gridheight_)]
        self._tiles_ = {UP:up_list, DOWN:down_list, LEFT:left_list, RIGHT:right_list}

        self.reset()

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code

        self._grid_=[[0 for col in range(self._gridwidth_)] for row in range(self._gridheight_)]
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        string=""

        for row in range(self._gridheight_):
            string+="["
            for col in range(self._gridwidth_):
                if col == self._gridwidth_-1:
                    string += str(self._grid_[row][col])
                else:
                    string += str(self._grid_[row][col])+","
            string+="]"+"\n"
        return string

    def get__gridheight_(self):
        """
        Get the height of the board.
        """
        return self._gridheight_

    def get__gridwidth_(self):
        """
        Get the width of the board.
        """

        return self._gridwidth_

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        change_tile= False

        for itr in self._tiles_[direction]:
            temp_list=[]


            curr_row=itr[0]
            curr_col=itr[1]


            while 0 <= curr_row < self._gridheight_ and 0 <= curr_col < self._gridwidth_:

                temp_list.append(self._grid_[curr_row][curr_col])
                curr_row += OFFSETS[direction][0]
                curr_col += OFFSETS[direction][1]


            temp_list=merge(temp_list)

            curr_row = itr[0]
            curr_col = itr[1]
            index = 0

            while 0 <= curr_row < self._gridheight_ and 0 <= curr_col < self._gridwidth_:
                if self._grid_[curr_row][curr_col] != temp_list[index]:
                    change_tile = True

                self._grid_[curr_row][curr_col] = temp_list[index]
                curr_row += OFFSETS[direction][0]
                curr_col += OFFSETS[direction][1]
                index += 1

        if change_tile == True:
            self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        val=1

        new_row = random.randrange(0,self._gridheight_)
        new_col = random.randrange(0,self._gridwidth_)

        while val != 0:
            new_row=random.randrange(0,self._gridheight_)
            new_col=random.randrange(0,self._gridwidth_)
            val=self._grid_[new_row][new_col]

        num=random.random()

        if num < 0.1:
            self._grid_[new_row][new_col]=4
        else:
            self._grid_[new_row][new_col]=2



    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid_[row][col]=value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid_[row][col]


poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
