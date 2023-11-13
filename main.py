from random import randint
from sys import exit

def is_number_valid(i, j, num, sudoku):
    # Check if placing 'num' at position (i, j) is valid
    for n in range(4):
        if n != j and sudoku[i][n] == num:
            return False
        if n != i and sudoku[n][j] == num:
            return False

    start_row, start_col = 2 * (i // 2), 2 * (j // 2)
    for x in range(start_row, start_row + 2):
        for y in range(start_col, start_col + 2):
            if x != i and y != j and sudoku[x][y] == num:
                return False
    return True

def generate_sudoku():
    # Generate a solved Sudoku grid
    sudoku = [[0] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            while True:
                num = randint(1, 4)
                if is_number_valid(i, j, num, sudoku):
                    sudoku[i][j] = num
                    break
    return sudoku

def hide_numbers(sudoku):
    # Hide 9 random numbers in the Sudoku grid
    hide_numbers = [[randint(0, 1) == 0 for _ in range(4)] for _ in range(4)]
    count = sum(row.count(True) for row in hide_numbers)
    while count < 9:
        x, y = randint(0, 3), randint(0, 3)
        if not hide_numbers[x][y]:
            hide_numbers[x][y] = True
            count += 1
    return hide_numbers

def print_sudoku(sudoku, hide_numbers):
    # Print the Sudoku grid with hidden numbers
    for i in range(4):
        for j in range(4):
            if hide_numbers[i][j]:
                print("_", end=" ")
            else:
                print(sudoku[i][j], end=" ")
        print()

def user_input(sudoku):
    # Receive user input to fill in Sudoku numbers
    count = 0
    while count < 9:
        while True:
            try:
                print("\nEnter position you want to fill:")
                row = int(input("> Enter row number(0-3): "))
                col = int(input("> Enter column number(0-3): "))
                num = int(input("> Enter number(1-4): "))
                if not (0 <= row < 4 and 0 <= col < 4 and 1 <= num <= 4):
                    raise ValueError("Invalid input! Please try again.")
                elif sudoku[row][col] != 0:
                    raise ValueError("This position is already filled! Please try again.")
                else:
                    break
            except ValueError as e:
                print(e)

        print("\nPossible!")
        sudoku[row][col] = num
        count += 1
        print_sudoku(sudoku, hide_numbers(sudoku))

    print("Congratulations! You win the game!")

def main():
    print("-----------------------------------------------------------------------------------------------------")
    print("\t\t\t\t\tLET'S PLAY SUDOKU!")
    print("-----------------------------------------------------------------------------------------------------")
    unsolved_sudoku = generate_sudoku()
    print_sudoku(unsolved_sudoku, hide_numbers(unsolved_sudoku))
    user_input(unsolved_sudoku)
    input()

if __name__ == "__main__":
    main()
