#!/usr/bin/env python3
import tictactoe
import sys


def menu():
    while True:
        print("\n1. start\n2. exit")
        what_user_want = input("Enter your choice: ")
        if what_user_want not in ("start", "exit", "1", "2"):
            print("Bad parameters!")
            continue
        if what_user_want in ("exit", "2"):
            sys.exit()
        else:
            while True:
                players = input("Choose player: ")
                players = players.split(" ")
                if len(players) > 2:
                    print("Bad parameters!")
                    continue
                if not set(players).issubset({"user", "easy", "medium", "hard"}):
                    print("Bad parameters!")
                    continue
                game = tictactoe.TicTacToe(players[0], players[1])
                print(game.play())
                break


if __name__ == "__main__":
    menu()
