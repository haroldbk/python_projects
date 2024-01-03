# Write your code here :-)
#board = [["-"]*3]*3
board = [["-"]*3 for _ in range(3)]


board[1][0]="X"
#print(board)

for row in board:
    print(f"{row[0]} {row[1]} {row[2]}")

