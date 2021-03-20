# # write your code here
# def print_field(syms):
#     print('---------')
#     print('|', syms[0], syms[1], syms[2], '|')
#     print('|', syms[3], syms[4], syms[5], '|')
#     print('|', syms[6], syms[7], syms[8], '|')
#     print('---------')
#
#
# def win_check(syms):
#     win_lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [6, 4, 2]]
#     lines = 0
#     if syms.count('X') - syms.count('O') > 1 or syms.count('O') - syms.count('X') > 1:
#         print('Impossible')
#         return
#     else:
#         for win_line in win_lines:
#             if syms[win_line[0]] == syms[win_line[1]] == syms[win_line[2]] == 'X':
#                 lines += 1
#                 # print(lines)
#             elif syms[win_line[0]] == syms[win_line[1]] == syms[win_line[2]] == 'O':
#                 lines += 1
#                 # print(lines)
#         if lines > 1:
#             print('Impossible')
#             return
#
#     for win_line in win_lines:
#
#         if syms[win_line[0]] == syms[win_line[1]] == syms[win_line[2]] == 'X':
#             print(f'X wins')
#             return
#         elif syms[win_line[0]] == syms[win_line[1]] == syms[win_line[2]] == 'O':
#             print(f'O wins')
#             return
#     if syms.count('X') + syms.count('O') == 9:
#         print('Draw')
#         return
#     else:
#         print('Game not finished')
#
#
#
#
#
# symbols = input('Enter cells: ')
# print_field(symbols)
# win_check(symbols)


theBoard = {'7': ' ', '8': ' ', '9': ' ',
            '4': ' ', '5': ' ', '6': ' ',
            '1': ' ', '2': ' ', '3': ' '}

board_keys = []

for key in theBoard:
    board_keys.append(key)

''' We will have to print the updated board after every move in the game and 
    thus we will make a function in which we'll define the printBoard function
    so that we can easily print the board everytime by calling this function. '''


def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])


# Now we'll write the main function which has all the gameplay functionality.
def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Move to which place?")

        move = input()

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves.
        if count >= 5:
            if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':  # across the top
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':  # across the middle
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':  # across the bottom
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':  # down the left side
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':  # down the middle
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':  # down the right side
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ':  # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':  # diagonal
                printBoard(theBoard)
                print("\nGame Over.\n")
                print(" **** " + turn + " won. ****")
                break

                # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
        if count == 9:
            print("\nGame Over.\n")
            print("It's a Tie!!")

        # Now we have to change the player after every move.
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

            # Now we will ask if player wants to restart the game or not.
    restart = input("Do want to play Again?(y/n)")
    if restart == "y" or restart == "Y":
        for key in board_keys:
            theBoard[key] = " "

        game()


if __name__ == "__main__":
    game()