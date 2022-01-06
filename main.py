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
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np
from numpy.core.fromnumeric import repeat

class GraphPlanner:
    def __init__(self, start, goal, method, connectivity, nrows = 100, ncolumns = 100, debug=True, obstacles = []):
        self.start = start
        self.position = start
        # print(self.position[0]+1)
        self.goal = goal
        self.goal_str = str(self.goal)
        self.position_str = str(self.position)
        self.nrows = nrows
        self.ncolumns = ncolumns
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
        self.obstacles = obstacles

    def get_potential_moves(self):
        # list potential moves based on connectivity
        if self.connectivity == 8:
            self.pre_potential_list = [[self.position[0] - 1, self.position[1]-1],
                                   [self.position[0]+1, self.position[1]+1],
                                   [self.position[0], self.position[1]-1],
                                   [self.position[0]-1, self.position[1]],
                                   [self.position[0]+1, self.position[1]],
                                   [self.position[0], self.position[1]+1],
                                   [self.position[0]-1, self.position[1]+1],
                                   [self.position[0]+1, self.position[1]-1]]
        if self.connectivity == 4:
            self.pre_potential_list = [[self.position[0], self.position[1]-1],
                                   [self.position[0]-1, self.position[1]],
                                   [self.position[0]+1, self.position[1]],
                                   [self.position[0], self.position[1]+1]]
        # check borders
        for item in self.pre_potential_list:
            if (item[0] >= 0 and item[0] <= self.nrows-1) and (item[1] >= 0 and item[1] <= self.ncolumns-1):
                self.potential_list.append(item)
        # filter out potential moves based on obstacles/wall
        for item in self.obstacles:
            if item in self.potential_list:
                self.potential_list.remove(item)
            else:
                pass
        # print(self.potential_list)
        # filter out potential movies based on explored tiles
        for item in self.explored:
            if item in self.potential_list:
                self.potential_list.remove(item)
        # print(self.potential_list)
        # check if goal is in potential moves ?
        if self.goal in self.potential_list:
            print("game over")
            self.game_over = True
            # print(self.explored)
            # print(self.path)
            # print(self.frontier)
            pass
            # add additional stuff here
        # add moves to frontier with their costs
        for move in self.potential_list:
            move1, move2 = move
            self.frontier[str(move1), str(move2)] = (
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
        # change current position to the new node
        # print(sorted_list[0])
        self.position = self.string_to_array(sorted_list[0])
        self.position_str = sorted_list[0]
        self.explored.append(self.string_to_array(
            sorted_list[0]))  # add to explored list
        self.path.append(self.string_to_array(sorted_list[0]))
        self.frontier.pop(sorted_list[0])  # remove from frontire
        self.depth = self.depth + 1  # adjust new depth

    def string_to_array(self, string):
        array = [int(string[0]), int(string[1])]
        return array


if __name__ == "__main__":
    planner = GraphPlanner(start=[0,1],goal=[5, 9], method='BFS',
                           connectivity=8, obstacles=[[1,1],[1,2],[1,3],[3,1],[2,1],[4,1]])
    def animate(i):
        #data = np.random.rand(10, 10) * 20 #create a zero matrix
        data = np.zeros((planner.nrows,planner.ncolumns),dtype=int)
        if planner.game_over == False:
            planner.get_potential_moves()
            planner.make_move()
            # print(planner.path)
        else:
            pass
            # global data
        # format for frontire
        for item in planner.frontier:
            int_item = planner.string_to_array(item)
            data[int_item[0],int_item[1]] = 22
        # format for explored
        for item in planner.explored:
            data[item[0],item[1]] = 32
        # format for unexplored
            #default 
        # format for obstacles
        for item in planner.obstacles:
            data[item[0],item[1]] = 37 
        # format for present
        # data[planner.position[0],planner.position[1]] = 27
        # format for start location
        data[planner.start[0],planner.start[1]] = 12
        # format for goal location
        data[planner.goal[0],planner.goal[1]] = 17
        cmap = colors.ListedColormap(['white','red','green','yellow','blue','gray','brown'])
        bounds = [0,10,15,20,25,30,35,40]
        # start -  red
        # goal - green
        # frontire - yellow
        # present - blue
        # explored - gray
        # unxplored - white
        # obstacles - black
        norm = colors.BoundaryNorm(bounds, cmap.N)
        global fig
        global ax
        ax.clear()
        ax.imshow(data, cmap=cmap, norm=norm)

            # draw gridlines
        ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
        ax.set_xticks(np.arange(-.5, planner.ncolumns + 0.5, 1))
        ax.set_yticks(np.arange(-.5, planner.nrows + 0.5, 1))
        ax.axes.xaxis.set_ticklabels([])
        ax.axes.yaxis.set_ticklabels([])

    def onClick(event):
        anim.event_source.stop()

    fig, ax = plt.subplots()
    fig.canvas.mpl_connect('button_press_event', onClick)
    anim = FuncAnimation(fig, animate, interval=20)
    # writer = PillowWriter(fps=2)  
    # anim.save("demo_sine.gif", writer=writer)
    plt.show()

