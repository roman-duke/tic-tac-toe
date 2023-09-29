from player import Player
from board import Board
from computer import Computer
import time

print("\nxoxoxoxoxoxoxoxoxoxoxoxoxoxoxo---WELCOME TO THE GAME OF TIC TAC TOE---xoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxoxo\n")
game_version = input("Please select the Game Version that you want:\n" +\
                    "1. Player vs Player\n" +\
                    "2. Player vs Computer\n" +\
                    "3. Computer vs Computer\n\n")

board = Board()

if game_version == "1":
    player1 = Player("x", board); player2 = Player("o", board)
    name1 = input("Enter the name of Player 1. ")
    name2 = input("Enter the name of Player 2. ")
    print(board)

    while (not board.game_win()):
        move = input(f'{name1} Make your move ')
        player1.move(move)
        if board.game_win(): print(f'\n{name1} wins!'); break
        if (" " not in board.moves.values()): print("\nIt's a draw!"); break
        print(board)
        move = input(f'{name2} Make your move ')
        player2.move(move)
        print(board)
        if board.game_win(): print(f'\n{name2} wins!'); break


elif game_version == "2": 
    level = input("Please select the difficulty level that you want:\n" +\
                "1. Easy\n" +\
                "2. Medium\n" +\
                "3. Impossible\n\n")
    
    answer = input("Do you wish to start first? ")

    print(board)

    if answer.lower()=="yes": player = Player("x", board); computer = Computer(board, "o", "x", level); move = input("Make your first move. ")
    elif answer.lower()=="no": player = Player("o", board); computer = Computer(board, "x", "o", level); print('\nComputer to make the first move')
    
    while (not board.game_win()):
        if answer == "no":
            print("Computer is thinking...")
            computer.think()
            print(board)
            if board.game_win(): print("\nComputer wins!"); break
            if (" " not in board.moves.values()): print("\nIt's a draw!"); break
            move = input("Make your move. ")
            player.move(move)
            print(board)
            if board.game_win(): print("You win!"); break

        elif answer=="yes":
            player.move(move)
            print(board)
            if board.game_win(): print("You win!"); break
            if (" " not in board.moves.values()): print("\nIt's a draw!"); break
            print("Computer is thinking...")
            computer.think()
            print(board)
            if board.game_win(): print("\nComputer wins!"); break
            move = input("Make your move. ")


elif game_version == "3":
    print("Watch closely as two AIs take each other on\nYou can aslo learn to play x and o perfectly by observing their moves closely\n")
    print("Hey Mortal!")
    print("We think extremely fast, so our thinking rates shall be slowed down for a mere mortal like you\n")
    time.sleep(1)
    cp1 = Computer(board, "x", "o"); cp2 = Computer(board, "o", "x")
    print(board)

    while (not board.game_win()):
        print("Computer 1 is thinking...")
        time.sleep(2)
        cp1.think()
        print(board)
        if (" " not in board.moves.values()): print("\nIt's a draw!"); break
        print("Computer 2 is thinking...")
        time.sleep(2)
        cp2.think()
        print(board)