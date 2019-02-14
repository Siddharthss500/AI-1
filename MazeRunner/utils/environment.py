import matplotlib
matplotlib.use('tkAgg')
from pylab import *
from matplotlib import colors


class Environment():
    ProbabilityOfBlockedMaze = 0.4
    DimensionOfMaze = 10

    def __init__(self):
        self.maze = None
        self.maze_copy = None
        self.colormesh = None

        # The default colormap of our maze - 0: Black, 1: White, 2: Grey
        self.cmap = colors.ListedColormap(['black', 'white', 'grey'])
        self.norm = colors.BoundaryNorm(boundaries = [0, 1, 2, 3], ncolors = 3)

    def generate_maze(self, n = DimensionOfMaze, p = ProbabilityOfBlockedMaze):
        self.n = n
        self.p = p

        self.maze = np.array([list(np.random.binomial(1, 1 - p, n)) for _ in range(n)])
        self.maze[0, 0] = 1
        self.maze[n-1, n-1] = 1

        # Create a copy of maze to render and update
        self.maze_copy = self.maze.copy()

    def render_maze(self, timer = 1e-7):
        # Create a mask for the particular cell and change its color to green
        masked_maze_copy = np.ma.masked_where(self.maze_copy == -1, self.maze_copy)
        self.cmap.set_bad(color = 'green')

        # Plot the new maze
        if self.colormesh is None:
            self.colormesh = plt.pcolormesh(masked_maze_copy,
                                            cmap = self.cmap,
                                            norm = self.norm,
                                            edgecolor = 'k',
                                            linewidth = 0.5,
                                            antialiased = False)
        else:
            self.colormesh.set_array(masked_maze_copy.ravel())
        plt.xticks([])
        plt.yticks([])
        plt.ion()
        plt.show()
        plt.pause(timer)

    def update_color_of_cell(self, row, column):
        self.maze_copy[row, column] = -1

    def reset_color_of_cell(self, row, column):
        self.maze_copy[row, column] = 2

