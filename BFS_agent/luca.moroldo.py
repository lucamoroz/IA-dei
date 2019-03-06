import time


class Maze(object):
    """A pathfinding problem."""

    def __init__(self, grid, location):
        """Instances differ by their current agent locations."""
        self.grid = grid
        self.location = location

    def __hash__(self):
        return hash(self.location)

    def __eq__(self, maze):
        return self.location == maze.location

    def __ne__(self, maze):
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

    def moves(self) -> 'list':
        """Return a list of possible moves given the current agent location."""
        # I've choosen to represent the moves using row and col indexes. Another (and maybe cleaner) implementation may
        # use an enumeration of possible moves (UP, DOWN, LEFT, RIGHT)

        # init possible moves
        row, col = self.location[0], self.location[1]
        moves = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]

        # remove unavailable moves
        moves = list(filter(self.is_valid_position, moves))
        return moves

    def neighbor(self, move):
        """Return another Maze instance with a move made."""
        # Param 'move' is a tuple (row, col), so we can just return a new maze based on that location
        return Maze(self.grid, move)

    def is_valid_position(self, position: tuple) -> bool:
        """Return true if a position is valid."""
        row = position[0]
        col = position[1]
        # Check that the position is not out of range and that there is no obstacle
        return 0 <= row < len(self.grid) \
               and 0 <= col <= len(self.grid[row]) \
               and self.grid[row][col] == " "


class Agent(object):
    """Knows how to find the exit to a maze with BFS."""

    def bfs(self, maze, goal):
        """Return an ordered list of moves to get the maze to match the goal."""
        # same of maze.location == goal.location
        if maze == goal:
            return [maze.location]

        # init a set with starting location
        visited = set(maze.location)
        # init a list of tuples (location, path_to_previous_location) where path to previous location is an empty list
        queue = list([(maze.location, [])])

        while queue:
            # you can also use queue.pop(), it will find another path to the goal!
            current_pos, path = queue.pop(0)
            # visit neighbors (ie available moves)
            for position in Maze(maze.grid, current_pos).moves():
                # skip iteration if already visited (use keyword 'continue' to reduce nested if)
                if position in visited:
                    continue
                # if this move brings the agent to the goal then return the path
                if position == goal.location:
                    return path + [current_pos, position]
                queue.append((position, path + [current_pos]))
                visited.add(position)
        # Path not found
        return None


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

    maze = Maze(grid, (1, 1))
    maze.display()

    agent = Agent()
    goal = Maze(grid, (19, 18))
    path = agent.bfs(maze, goal)

    while path:
        move = path.pop(0)
        maze = maze.neighbor(move)
        time.sleep(0.2)
        maze.display()


if __name__ == '__main__':
    main()

