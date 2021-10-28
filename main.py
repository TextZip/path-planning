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

class GraphPlanner:
    def __init__(self, start, goal, method, connectivity, debug):
        self.position = start
        self.goal = goal
        self.goal_str = str(self.goal)
        self.position_str = str(self.start)
        self.nrows = 0
        self.ncolumns = 0

        self.method = method
        self.debug = debug
        self.connectivity = connectivity
        self.path = [] # list of previously taken positions

        self.frontier = {} # position: (depth + heuristic)
        self.depth = 0 # current position depth
        self.frontier[self.start_str] = 0
        self.heuristic = 0
        self.explored = []
        self.obstacles = []

    def get_potential_moves(self):
        # list potential moves based on connectivity 
        if self.connectivity == 8:
            self.potential_list = [[self.position[0]-1, self.position[1]-1],
             [self.position[0]+1, self.position[1]+1], 
             [self.position[0], self.position[1]-1], 
             [self.position[0]-1, self.position[1]],
             [self.position[0]+1, self.position[1]], 
             [self.position[0], self.position[1]+1],
             [self.position[0]-1, self.position[1]+1],
             [self.position[0]+1, self.position[1]-1]]
        if self.connectivity == 4:
            self.potential_list = [[self.position[0], self.position[1]-1], 
             [self.position[0]-1, self.position[1]],
             [self.position[0]+1, self.position[1]], 
             [self.position[0], self.position[1]+1]]
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
            else:
                pass
        # check borders
        for item in self.potential_list:
            if  item[0] < 0 or item[0] > self.nrows:
                self.potential_list.remove(item)
            elif item[1] < 0 or item[1] > self.ncolumns:
                self.potential_list.remove(item)
        # check if goal is in potential moves ? 
        if self.goal in self.potential_list:
            print("game over")
            pass
            # add additional stuff here
        # add moves to frontier with their costs 
        for move in self.potential_list:
            self.frontier[str(move)] = ((self.depth+1)+self.find_heuristic(move))

    def find_heuristic(self,move):
        if self.method == "A_star":
            h_cost = pow(pow((move[0] - self.goal[0]),2) + pow((move[1]-self.goal[1]),2),0.5)
        elif self.method == "BFS":
            h_cost = 0
        return h_cost

    def make_move(self):
        # sort the frontier and pick the item with the least cost for BFS and A* (atleast)
        sorted_list = sorted(self.potential_list, key = self.potential_list.get, reverse=True) # gives a list
        






        