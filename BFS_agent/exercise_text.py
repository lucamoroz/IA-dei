import time

class Maze(object):
	"""A pathfinding problem."""

	def __init__(self, grid, location):
		"""Instances differ by their current agent locations."""
		self.grid = grid
		self.location = location
		
	def __hash__(self):
		return hash(self.location)
	
	def __eq__(self,maze):
		return self.location == maze.location
	
	def __ne__(self,maze):
		return self.location != maze.location
	
	def display(self):
		"""Print the maze, marking the current agent location."""
		for r in range(len(self.grid)):
			for c in range(len(self.grid[r])):
				if (r, c) == self.location:
					print('*', end=" ")
				else:
					print(self.grid[r][c], end=" ")
			print("")
		print(" ")

	def moves(self):
		"""Return a list of possible moves given the current agent location."""
		# YOU FILL THIS IN
		

	def neighbor(self, move):
		"""Return another Maze instance with a move made."""
		# YOU FILL THIS IN
		

class Agent(object):
	"""Knows how to find the exit to a maze with BFS."""

	def bfs(self, maze, goal):
		"""Return an ordered list of moves to get the maze to match the goal."""
		# YOU FILL THIS IN
		
			

def main():
    """Create a maze, solve it with BFS, and console-animate."""
    
    grid = ["XXXXXXXXXXXXXXXXXXXX",
            "X     X    X       X",
            "X XXXXX XXXX XXX XXX",
            "X       X      X X X",
            "X XXXXXXXXXXXX X X X",
            "X X   X        X X X",
            "X XXX XXXXXX XXXXX X",
            "X XXX    X X X     X",
            "X    XXX       XXXXX",
            "X XXX   XXXXXX     X",
            "X   XXX X X    X X X",
            "XXX XXX X X XXXX X X",
            "X     X X   XX X X X",
            "XXXXX     XXXX X XXX",
            "X     X XXX    X   X",
            "X XXXXX X XXXX XXX X",
            "X X     X  X X     X",
            "X X XXXXXX X XXXXX X",
            "X X                X",
            "XXXXXXXXXXXXXXXXXX X"]

    maze = Maze(grid, (1,1))
    maze.display()

    agent = Agent()
    goal = Maze(grid, (19,18))
    path = agent.bfs(maze, goal)

    while path:
        move = path.pop(0)
        maze = maze.neighbor(move)
        time.sleep(0.5)
        maze.display()

if __name__ == '__main__':
    main()
