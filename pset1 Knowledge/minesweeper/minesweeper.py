import itertools
import random


class Minesweeper():
    """
    Minesweeper game representation
    """

    def __init__(self, height=8, width=8, mines=8):

        # Set initial width, height, and number of mines
        self.height = height
        self.width = width
        self.mines = set()

        # Initialize an empty field with no mines
        self.board = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(False)
            self.board.append(row)

        # Add mines randomly
        while len(self.mines) != mines:
            i = random.randrange(height)
            j = random.randrange(width)
            if not self.board[i][j]:
                self.mines.add((i, j))
                self.board[i][j] = True

        # At first, player has found no mines
        self.mines_found = set()

    def print(self):
        """
        Prints a text-based representation
        of where mines are located.
        """
        for i in range(self.height):
            print("--" * self.width + "-")
            for j in range(self.width):
                if self.board[i][j]:
                    print("|X", end="")
                else:
                    print("| ", end="")
            print("|")
        print("--" * self.width + "-")

    def is_mine(self, cell):
        i, j = cell
        return self.board[i][j]

    def nearby_mines(self, cell):
        """
        Returns the number of mines that are
        within one row and column of a given cell,
        not including the cell itself.
        """

        # Keep count of nearby mines
        count = 0

        # Loop over all cells within one row and column
        for i in range(cell[0] - 1, cell[0] + 2):
            for j in range(cell[1] - 1, cell[1] + 2):

                # Ignore the cell itself
                if (i, j) == cell:
                    continue

                # Update count if cell in bounds and is mine
                if 0 <= i < self.height and 0 <= j < self.width:
                    if self.board[i][j]:
                        count += 1

        return count

    def won(self):
        """
        Checks if all mines have been flagged.
        """
        return self.mines_found == self.mines


class Sentence():
    """
    Logical statement about a Minesweeper game
    A sentence consists of a set of board cells,
    and a count of the number of those cells which are mines.
    """

    def __init__(self, cells, count):
        self.cells = set(cells)
        self.count = count

    def __eq__(self, other):
        return self.cells == other.cells and self.count == other.count

    def __str__(self):
        return f"{self.cells} = {self.count}"

    def known_mines(self):
        """
        Returns the set of all cells in self.cells known to be mines.
        """
        # If the count is equal to the length of the cells set return the cells
        # otherwise return a new set
        if self.count == len(self.cells):
            return self.cells
        else:
            return set()

    def known_safes(self):
        """
        Returns the set of all cells in self.cells known to be safe.
        """
        # If the count is 0 then return the cells set
        # otherwise return a new set
        if self.count == 0:
            return self.cells
        else:
            return set()

    def mark_mine(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be a mine.
        """
        # If cell is in the sentence then remove the cell and update the counter
        if cell in self.cells:
            self.cells.remove(cell)
            self.count -= 1

    def mark_safe(self, cell):
        """
        Updates internal knowledge representation given the fact that
        a cell is known to be safe.
        """
        # If cell is in the sentence, remove the cell
        if cell in self.cells:
            self.cells.remove(cell)


class MinesweeperAI():
    """
    Minesweeper game player
    """

    def __init__(self, height=8, width=8):

        # Set initial height and width
        self.height = height
        self.width = width

        # Keep track of which cells have been clicked on
        self.moves_made = set()

        # Keep track of cells known to be safe or mines
        self.mines = set()
        self.safes = set()

        # List of sentences about the game known to be true
        self.knowledge = []

    def mark_mine(self, cell):
        """
        Marks a cell as a mine, and updates all knowledge
        to mark that cell as a mine as well.
        """
        self.mines.add(cell)
        for sentence in self.knowledge:
            sentence.mark_mine(cell)

    def mark_safe(self, cell):
        """
        Marks a cell as safe, and updates all knowledge
        to mark that cell as safe as well.
        """
        self.safes.add(cell)
        for sentence in self.knowledge:
            sentence.mark_safe(cell)

    def add_knowledge(self, cell, count):
        """
        Called when the Minesweeper board tells us, for a given
        safe cell, how many neighboring cells have mines in them.

        This function should:
            1) mark the cell as a move that has been made
            2) mark the cell as safe
            3) add a new sentence to the AI's knowledge base
               based on the value of `cell` and `count`
            4) mark any additional cells as safe or as mines
               if it can be concluded based on the AI's knowledge base
            5) add any new sentences to the AI's knowledge base
               if they can be inferred from existing knowledge
        """
        # 1) Mark the cell as a move that has been made
        self.moves_made.add(cell)

        # 2) Mark the cell as safe
        self.mark_safe(cell)

        # Find the neighbours of the cell
        neighbours = self.find_neighbours(cell)

        # Update the neighbours set and remove cells with known state
        # Collect the cells to remove
        to_remove = set()
        for neighbour in neighbours:
            # Check cell states for marked mines
            if neighbour in self.mines:
                to_remove.add(neighbour)
                count -= 1

            # Check cell states for marked safes
            if neighbour in self.safes:
                to_remove.add(neighbour)

        # Remove the collected cells in set from the set of neighbours
        neighbours -= to_remove

        # 3) Add a new sentence to the AI's knowledge base
        #    based on the value of 'cell' and 'count'
        new_sen = Sentence(neighbours, count)
        self.knowledge.append(new_sen)

        # 4) Mark any additional cells as safe or as mines
        #    if it can be concluded based ont he AI's knowledge base
        self.update()

        # 5) Add any new sentences to the AI's knowledge base
        #    if they can be inferred from existing knowledge
        self.learn(new_sen)

        # Output the knowledge base
        print("Number of sentences in knowledge base: ", len(self.knowledge))
        print("Sentences Learned: ")
        for sentence in self.knowledge:
            print("\t", sentence.cells, " = ", sentence.count)

    def make_safe_move(self):
        """
        Returns a safe cell to choose on the Minesweeper board.
        The move must be known to be safe, and not already a move
        that has been made.

        This function may use the knowledge in self.mines, self.safes
        and self.moves_made, but should not modify any of those values.
        """
        # Return a safe move that has not been made
        for safe in self.safes:
            if safe not in self.moves_made:
                return safe

        return None

    def make_random_move(self):
        """
        Returns a move to make on the Minesweeper board.
        Should choose randomly among cells that:
            1) have not already been chosen, and
            2) are not known to be mines
        """
        # For all the possible coordinates on the board from 0, 0
        for i in range(0, self.height):
            for j in range(0, self.width):
                # Get the selected action from iteration
                action = (i, j)
                # If the action is not in the marked mines and not a move that has been made
                if action not in self.mines and action not in self.moves_made:
                    # Return the action
                    return action

        return None

    def find_neighbours(self, cell):
        # Get the target cell coordinates
        i, j = cell

        neighbours = set()
        # Get the neighbouring cells surrounding the target cell
        for x in range(max(0, i - 1), min(i + 2, self.height)):
            for y in range(max(0, j - 1), min(j + 2, self.width)):
                # If the cell is not the target cell
                if (x, y) != (i, j):
                    # Add the neighbouring cell into the set
                    neighbours.add((x, y))

        # Return all the neighbouring cells
        return neighbours

    def update(self):
        mines_todo = set()
        safes_todo = set()
        # Get the safe cells and mine cells
        for sentence in self.knowledge:
            for cell in sentence.known_safes():
                safes_todo.add(cell)

            for cell in sentence.known_mines():
                mines_todo.add(cell)

        # Update the mine and safe cells
        for safe in safes_todo:
            self.mark_safe(safe)

        for mine in mines_todo:
            self.mark_mine(mine)

    def learn(self, new_sentence):
        # Remove empty sentences
        for sentence in self.knowledge:
            if sentence.cells == set():
                self.knowledge.remove(sentence)

        # 5) Add any new sentences to the AI's knowledge base
        #    if they can be inferred from existing knowledge
        new_knowledge = []

        # Gather the new knowledge to be added
        for sentence in self.knowledge:
            if new_sentence.cells and sentence.cells != new_sentence.cells:
                if sentence.cells.issubset(new_sentence.cells):
                    new_knowledge.append(Sentence(new_sentence.cells - sentence.cells,
                                                  new_sentence.count - sentence.count))

                if new_sentence.cells.issubset(sentence.cells):
                    new_knowledge.append(Sentence(sentence.cells - new_sentence.cells,
                                                  sentence.count - new_sentence.count))

        # Add the new knowledge to existing knowledge base
        self.knowledge += new_knowledge
