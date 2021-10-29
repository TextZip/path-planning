# Path planning algo mock
##############################################
# Check if the current node is the goal
# If goal not reached explore potential moves
# Select a move based on the cost function
##############################################

# Features to implement
##############################################
# 8 connected or 4 connected
# A*, BFS, DFS and others selection
# Obstacle generator
##############################################
import numpy as np

grid = np.array([[0, 0, 0, 0, 0, 0, 0, 1, 0, 0],  # Row 0
                 [0, 1, 1, 0, 0, 0, 0, 1, 0, 0],  # Row 1
                 [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # Row 2
                 [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # Row 3
                 [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # Row 4
                 [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # Row 5
                 [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # Row 6
                 [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # Row 7
                 [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # Row 8
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]) # Row 9
        # Columns 0  1  2  3  4  5  6  7  8  9
class GraphPlanner:
    def __init__(self, goal, method, connectivity, debug):
        self.position = [0,0]
        #print(self.position[0]+1)
        self.goal = goal
        self.goal_str = str(self.goal)
        self.position_str = str(self.position)
        self.nrows = 10
        self.ncolumns = 10
        self.game_over = False
        self.potential_list = []

        self.method = method
        self.debug = debug
        self.connectivity = connectivity
        self.path = []  # list of previously taken positions

        self.frontier = {}  # position: (depth + heuristic)
        self.depth = 0  # current position depth
        self.heuristic = 0
        self.explored = []
        self.explored.append(self.position)
        self.obstacles = []

    def get_potential_moves(self):
        # list potential moves based on connectivity
        if self.connectivity == 8:
            self.potential_list = [[self.position[0]- 1,self.position[1]-1],
                                   [self.position[0]+1,self.position[1]+1],
                                   [self.position[0],self.position[1]-1],
                                   [self.position[0]-1,self.position[1]],
                                   [self.position[0]+1,self.position[1]],
                                   [self.position[0],self.position[1]+1],
                                   [self.position[0]-1,self.position[1]+1],
                                   [self.position[0]+1,self.position[1]-1]]
        if self.connectivity == 4:
            self.potential_list = [[self.position[0],self.position[1]-1],
                                   [self.position[0]-1,self.position[1]],
                                   [self.position[0]+1,self.position[1]],
                                   [self.position[0],self.position[1]+1]]
        # check borders
        for item in self.potential_list:
            if item[0] <= 0 or item[0] >= self.nrows:
                self.potential_list.remove(item)
        for item in self.potential_list:    
            if item[1] <= 0 or item[1] >= self.ncolumns:
                self.potential_list.remove(item)
        # filter out potential moves based on obstacles/wall
        for item in self.obstacles:
            if item in self.potential_list:
                self.potential_list.remove(item)
            else:
                pass
        # filter out potential movies based on explored tiles
        for item in self.explored:
            if item in self.potential_list:
                self.potential_list.remove(item)
        # check if goal is in potential moves ?
        if self.goal in self.potential_list:
            print("game over")
            self.game_over = True
            #print(self.explored)
            #print(self.path)
            #print(self.frontier)
            pass
            # add additional stuff here
        # add moves to frontier with their costs
        for move in self.potential_list:
            move1, move2 = move
            self.frontier[str(move1),str(move2)] = (
                (self.depth+1)+self.find_heuristic(move))

    def find_heuristic(self, move):
        if self.method == "A_star":
            h_cost = pow(pow((move[0] - self.goal[0]), 2) +
                         pow((move[1]-self.goal[1]), 2), 0.5)
        elif self.method == "BFS":
            h_cost = 0
        return h_cost

    def make_move(self):
        # sort the frontier and pick the item with the least cost for BFS and A* (atleast)
        sorted_list = sorted(
            self.frontier, key=self.frontier.get, reverse=False)  # gives a list of strings
        # take top most element from the sorted_list and push as the current position and pop the element as well 
        # print(f"sorted list: {sorted_list}")
        self.position = self.string_to_array(sorted_list[0]) # change current position to the new node
        self.position_str = sorted_list[0]
        self.explored.append(self.string_to_array(sorted_list[0])) # add to explored list
        self.path.append(self.string_to_array(sorted_list[0]))
        self.frontier.pop(sorted_list[0]) # remove from frontire 
        self.depth = self.depth +1 # adjust new depth

    def string_to_array(self, string):
        array = [int(string[0]),int(string[1])]
        return array
        

    
if __name__ == "__main__":
    planner = GraphPlanner(goal=[5,9],method='BFS',connectivity=4,debug=True)
    while planner.game_over == False:
        planner.get_potential_moves()
        planner.make_move()
    print(planner.explored)

