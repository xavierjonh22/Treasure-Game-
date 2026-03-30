import random


def create_board(width, height):
    board = []
    numberOfUndiscoveredTreasures = 0

    for _ in range(height):
        row = []
        for _ in range(width):
            if random.random() >= 0.7:  
                row.append("T")
                numberOfUndiscoveredTreasures += 1
            else:
                row.append("O")
        board.append(row)

    return board, numberOfUndiscoveredTreasures


def display_board(board):
    for row in board:
        print(" ".join(row))


def play_game(board, numberOfUndiscoveredTreasures):
    height = len(board)
    width = len(board[0])

    print(f"Number of treasures hidden: {numberOfUndiscoveredTreasures}")

    while numberOfUndiscoveredTreasures > 0:
        try:
            row = int(input(f"Enter the row number (0 to {height - 1}): "))
            col = int(input(f"Enter the column number (0 to {width - 1}): "))

            if 0 <= row < height and 0 <= col < width:
                if board[row][col] == "T":
                    print("Congratulations! You found a treasure!")
                    board[row][col] = "X"
                    numberOfUndiscoveredTreasures -= 1
                else:
                    print("No treasure here, try again!")


            else:
                print("Invalid input, please enter a valid row and column.")
        except ValueError:
            print("Invalid input, please enter numbers only.")

    print("Congratulations! You've found all the treasures!")
    display_board(board)



def main():
    width = int(input("Enter the width of the grid: "))
    height = int(input("Enter the height of the grid: "))

    board, numberOfUndiscoveredTreasures = create_board(width, height)

    if numberOfUndiscoveredTreasures == 0:
        print("No treasures were placed. Restart the game for another chance!")
    else:
        play_game(board, numberOfUndiscoveredTreasures)



main()