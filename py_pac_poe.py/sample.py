board = {}
turn = "X"
print("----------------------\nLet's play Py-Pac-Poe!\n----------------------")

def render_board():
    global board
    print(f"  A   B   C\n1) {board['a1']} |  {board['b1']}  |  {board['c1']}  \n------------\n2)  {board['a2']}  |  {board['b2']}  |  {board['c2']}  \n------------\n3)  {board['a3']}  |  {board['b3']}  |  {board['c3']}  ")
    get_winner()

def init_game():
	# Use the global keyword to update global variables
	global board, turn
	board = {
	'a1': "", 
    'b1': "", 
    'c1': "",
	'a2': "", 
    'b2': "", 
    'c2': "",
	'a3': "", 
    'b3': "", 
    'c3': ""
	}

def get_winner():
    if board.get("a1") == board.get("b1") and board.get("b1") == board.get("c1") and board.get("a1"):
        print(f"{board.get('a1')} is the winner!")
    elif board.get("a2") == board.get("b2") and board.get("b2") == board.get("c2") and board.get("a2"):
        print(f"{board.get('a2')} is the winner!")
    elif board.get("a3") == board.get("b3") and board.get("b3") == board.get("c3") and board.get("a3"):
        print(f"{board.get('a3')} is the winner!")
    elif board.get("a1") == board.get("a2") and board.get("a3") == board.get("a1") and board.get("a1"):
        print(f"{board.get('a1')} is the winner!")
    elif board.get("b1") == board.get("b2") and board.get("b3") == board.get("b1") and board.get("b1"):
        print(f"{board.get('b1')} is the winner!")
    elif board.get("c1") == board.get("c2") and board.get("c3") == board.get("c1") and board.get("c1"):
        print(f"{board.get('c1')} is the winner!")
    elif board.get("a1") == board.get("b2") and board.get("c3") == board.get("a1") and board.get("a1"):
        print(f"{board.get('a1')} is the winner!")
    elif board.get("a3") == board.get("b2") and board.get("c1") == board.get("a3") and board.get("a3"):
        print(f"{board.get('a3')} is the winner!")
    elif len(board.values()) == 9 and "" not in board.values():
        print("TIE")
    else:
        get_move()
    return True

def get_move():
    global turn 
    move = input(f"Player {turn}'s move (example B2): ").lower()
    if move in board.keys():
        if board.get(move):
            print("Bogus move! Please enter a valid move.")
            get_move()
        else:
            board[move] = turn
            if turn == "X":
                turn = "O"
            else:
                turn = "X"
            render_board()
    else: 
        print("Bogus move! Please enter a valid move.")
        get_move()

init_game()
render_board()