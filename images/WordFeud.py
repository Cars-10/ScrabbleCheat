# word_feud.py

class WordFeud:
    def __init__(self):
        self.wordfeud_board = self.initialize_board()
        self.scrabble_string = self.initialize_tiles()

    @staticmethod
    def initialize_board():
        return [
            ['3W', '.', '.', '2L', '.', '.', '.', '3W', '.', '.', '.', '2L', '.', '.', '3W'],
            ['.', '2W', '.', '.', '.', '3L', '.', '.', '.', '3L', '.', '.', '.', '2W', '.'],
            ['.', '.', '2W', '.', '.', '.', '2L', '.', '2L', '.', '.', '.', '2W', '.', '.'],
            ['2L', '.', '.', '2W', '.', '.', '.', '2L', '.', '.', '.', '2W', '.', '.', '2L'],
            ['.', '.', '.', '.', '2W', '.', '.', '.', '.', '.', '2W', '.', '.', '.', '.'],
            ['.', '3L', '.', '.', '.', '3L', '.', '.', '.', '3L', '.', '.', '.', '3L', '.'],
            ['.', '.', '2L', '.', '.', '.', '2L', '.', '2L', '.', '.', '.', '2L', '.', '.'],
            ['3W', '.', '.', '2L', '.', '.', '.', '2W', '.', '.', '.', '2L', '.', '.', '3W'],
            ['.', '.', '2L', '.', '.', '.', '2L', '.', '2L', '.', '.', '.', '2L', '.', '.'],
            ['.', '3L', '.', '.', '.', '3L', '.', '.', '.', '3L', '.', '.', '.', '3L', '.'],
            ['.', '.', '.', '.', '2W', '.', '.', '.', '.', '.', '2W', '.', '.', '.', '.'],
            ['2L', '.', '.', '2W', '.', '.', '.', '2L', '.', '.', '.', '2W', '.', '.', '2L'],
            ['.', '.', '2W', '.', '.', '.', '2L', '.', '2L', '.', '.', '.', '2W', '.', '.'],
            ['.', '2W', '.', '.', '.', '3L', '.', '.', '.', '3L', '.', '.', '.', '2W', '.'],
            ['3W', '.', '.', '2L', '.', '.', '.', '3W', '.', '.', '.', '2L', '.', '.', '3W']
        ]

    @staticmethod
    def initialize_tiles():
        letter_counts = {
            'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3,
            'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6,
            'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4,
            'V': 2, 'W': 2, 'X': 1, 'Y': 2, 'Z': 1, '_': 2  # '_' represents the blank tiles
        }
        return ''.join([letter * count for letter, count in letter_counts.items()])

    def update_square(self, x, y, value):
        """
        Update the square at (x, y) with the given value.
        """
        if 0 <= x < len(self.wordfeud_board) and 0 <= y < len(self.wordfeud_board[0]):
            self.wordfeud_board[x][y] = value
        else:
            print("Invalid x or y value. Make sure they are within the board's dimensions.")

    def read_square(self, x, y):
        """
        Return the value at the square (x, y). If x or y are out of bounds, return None.
        """
        if 0 <= x < len(self.wordfeud_board) and 0 <= y < len(self.wordfeud_board[0]):
            return self.wordfeud_board[x][y]
        else:
            print("Invalid x or y value. Make sure they are within the board's dimensions.")
            return None

    def display_board(self):
        for row in self.wordfeud_board:
            print(' '.join(row))

    def display_tiles(self):
        print(self.scrabble_string)


# If you want to run some tests directly from this script:
if __name__ == '__main__':
    game = WordFeud()
    game.update_square(7, 7, 'A')  # Place the letter 'A' at the center
    print(game.read_square(7, 7))  # Should display 'A'
    game.display_board()

    game.display_tiles()
