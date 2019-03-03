import numpy as np
from copy import copy

class MineSweeperAgent():

    def __init__(self, environment, visual):
        self.env = environment
        self.visual = visual
        self.old_maze = None

    def play(self):
        self.env.click_square(0,0)
        self.env.render_env()
        self.basic_solution(ground = self.env.mine_ground_copy)
        return


    def basic_solution(self, ground):
        old_ground = None
        while not np.array_equal(old_ground, ground):
            old_ground = copy(ground)
            ground = self.basic_solver(ground)
                
        
    def basic_solver(self, ground):
        for row in range(ground.shape[0]):
            for column in range(ground.shape[1]):
                if ground[row,column] == -1 :
                    continue
                else:
                    if ground[row,column] == 0 :
                        self.query_all_neighbours(row,column)
                    
                    elif ground[row,column] == 8:
                        self.flag_all_neighbours(row,column)
                    
                    else:
                        if self.get_bomb(row,column) == ground[row,column]:
                            self.query_all_neighbours(row,column)
                        elif self.get_unexplored(row,column) == ground[row,column]:
                            self.flag_all_neighbours(row,column)
    

    def query_all_neighbours(self,row,column):
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if (row + i >= 0 and column + j >= 0 
                    and row + i < self.env.mine_ground_copy.shape[0] and column + j < self.env.mine_ground_copy.shape[1]):
                        if self.env.mine_ground_copy[row+i,column+j] == -1:
                            self.env.click_square(row+i,column+j)
                            self.env.render_env()


    def flag_all_neighbours(self,row,column):
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if (row + i >= 0 and column + j >= 0 
                    and row + i < self.env.mine_ground_copy.shape[0] and column + j < self.env.mine_ground_copy.shape[1]):
                    if self.env.mine_ground_copy[row+i,column+j] == -1:
                        self.env.add_mine_flag(row+i,column+j)
                        self.env.render_env()
    
    def get_bomb(self,row,column):
        bomb_count = 0
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if (row + i >= 0 and column + j >= 0 
                    and row + i < self.env.mine_ground_copy.shape[0] and column + j < self.env.mine_ground_copy.shape[1]):
                    if self.env.flags.astype(bool)[row+i,column+j] == True:
                        bomb_count = bomb_count + 1   
        return bomb_count
    
    def get_unexplored(self,row,column):
        unexplored_count = 0
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if (row + i >= 0 and column + j >= 0 
                    and row + i < self.env.mine_ground_copy.shape[0] and column + j < self.env.mine_ground_copy.shape[1]):
                    if self.env.mine_ground_copy[row+i,column+j] == -1:
                        unexplored_count = unexplored_count + 1   
        return unexplored_count

                    
            
