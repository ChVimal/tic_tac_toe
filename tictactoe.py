import random


def initial_state():
    return ["_", "_", "_", "_", "_", "_", "_", "_", "_"]


def player(board):
    count = {"X": 0, "O": 0}
    for i in board:
        if i in count.keys():
            count[i] += 1
    if count["X"] <= count["O"]:
        return "X"
    else:
        return "O"


class TicTacToe:
    def __init__(self, pX, pO):
        players = {
            "user": self.user,
            "easy": self.easy,
            "medium": self.medium,
            "hard": self.hard,
        }
        self.playerX = players[pX]
        self.playerO = players[pO]
        self.board = initial_state()
        self.winning_combination = (
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        )

    def print_board(self):
        print("---------")
        for i in range(0, 9, 3):
            print(
                "| {} {} {} |".format(
                    self.board[i], self.board[1 + i], self.board[2 + i]
                )
            )
        print("---------")

    def winner(self, board):
        if "_" not in board:
            return "Tie"
        for i in self.winning_combination:
            if {board[i[0]], board[i[1]], board[i[2]]} == set("X"):
                return "X"
            elif {board[i[0]], board[i[1]], board[i[2]]} == set("O"):
                return "O"
        return None

    def random_move(self):
        random.seed()
        while True:
            index = random.choice(range(9))
            if self.board[index] != "_":
                continue
            else:
                self.board[index] = player(self.board)
                break

    def easy(self):
        print('Making move level "easy"')
        self.random_move()

    def medium(self):
        print('Making move level "medium"')
        current_player = player(self.board)
        p_loss = sorted(("X", "X", "_"))
        p_win = sorted(("O", "O", "_"))
        for i in self.winning_combination:
            temp = (self.board[i[0]], self.board[i[1]], self.board[i[2]])
            if p_win == sorted(temp):
                index = temp.index("_")
                self.board[i[index]] = current_player
                return
            elif p_loss == sorted(temp):
                index = temp.index("_")
                self.board[i[index]] = current_player
                return
        self.random_move()

    def hard(self):
        print('Making move level "hard"')
        current_player = player(self.board)

        if self.board == initial_state():
            index = random.choice([0, 1, 2, 3, 5, 6, 7, 8])
            self.board[index] = current_player
            return

        best_score = -10 if current_player == "X" else 10
        index = 0
        for i in range(9):
            if self.board[i] == "_":
                self.board[i] = current_player
                score = self.minimax(self.board, best_score)
                self.board[i] = "_"

                if current_player == "X":
                    score = max(best_score, score)

                if current_player == "O":
                    score = min(best_score, score)

                if score != best_score:
                    best_score = score
                    index = i

        self.board[index] = current_player

    def minimax(self, board, score_of_parent):
        winner = self.winner(board)
        if winner:
            return 1 if winner == "X" else -1 if winner == "O" else 0

        current_player = player(board)
        best_score = -10 if current_player == "X" else 10

        for i in range(9):
            if self.board[i] == "_":
                self.board[i] = current_player
                score = self.minimax(self.board, best_score)
                self.board[i] = "_"

                if current_player == "X":
                    if score > score_of_parent:
                        return score
                    best_score = max(best_score, score)

                if current_player == "O":
                    if score < score_of_parent:
                        return score
                    best_score = min(best_score, score)
        return best_score

    def user(self):
        while True:
            index = input("Enter the position: ")
            if len(index) > 1:
                print("You can enter only one position. Try again.")
            elif not index.isdigit():
                print("You should enter numbers!")
                continue
            elif int(index) not in range(0, 9):
                print("Coordinates should be from 0 to 8!")
                continue
            elif self.board[int(index)] != "_":
                print("This cell is occupied! Choose another one!")
                continue
            self.board[int(index)] = player(self.board)
            break

    def play(self):
        flag = True
        while True:
            self.print_board()
            winner = self.winner(self.board)
            if winner:
                return winner
            elif flag:
                self.playerX()
                flag = False
            else:
                self.playerO()
                flag = True
