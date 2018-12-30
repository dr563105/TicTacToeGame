import itertools 

def play_game(game_map, player = 0, row = 0, column = 0, show_game = False):
    try:
        #To check if the position has been played already
        if game_map[row][column] !=0:
            print(f"Position already played. Choose another. ")
            return game_map, False
        #Display column numbers
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not show_game:
            game_map[row][column] = player
        #Display row number
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True

    except IndexError as e:
        print(f"Enter only {list(range(game_size))} row and column choices.", e)
        return game_map, False

    except Exception as e:
        print(f"Something went wrong", e)
        return game_map, False

def game_logic(game_map):
    #Check for identical items in the list
    def same_item_check(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    for row in game_map:
        if same_item_check(row):
            print(f"Winner! Player {row[0]} wins horizontally!!!")
            return True
    for col in range(len(game_map)):
        col_check = []
        for row in game_map:
            col_check.append(row[col])
        if same_item_check(col_check):
            print(f"Winner! Player {col_check[0]} wins vertically!!!")
            return True
    diags = []
    #diagonal check
    for ix in range(len(game_map)):
        diags.append(game_map[ix][ix])
    if same_item_check(diags):
        print(f"Winner! Player {diags[0]} wins diagonally! (\\)")
        return True
    diags_reversed = []
    rows = range(len(game_map))    
    cols = reversed(range(len(game_map)))
    #reverse diagonal check
    for x, iy in zip(rows, cols):
        diags_reversed.append(game_map[x][iy])
    if same_item_check(diags_reversed):
        print(f"Winner! Player {diags_reversed[0]} wins reverse diagonally! (/)")
        return True
    return False
    
current_game_active = True
while current_game_active: 
    game_size = int(input("Enter the size of game you\'d like to play?Value must be above 1!: "))
    game_board = [[0 for i in range(game_size)] for i in range(game_size)]
    game_won = False
    print(f"\nGame board looks like this: ")
    game_board, _ = play_game(game_board,show_game=True)
    players = itertools.cycle(list(range(1,game_size)))   
    while not game_won:
        current_player = next(players)
        print(f"Current player: {current_player}")
        status = False
        while not status:
            row_choice = int(input(f"Which row would you like to play? Enter only {list(range(game_size))}: "))
            col_choice = int(input(f"Which column would you like to play? Enter only {list(range(game_size))}: "))
            game_board, status = play_game(game_board, current_player, row_choice, col_choice)
        if game_logic(game_board):
            game_won = True
            play_again = input("The game is over. Would you like to play again?(y/n) ")
            if play_again.lower() == 'y':
                print("Restarting...")
            elif play_again.lower() == 'n':
                print("Bye!")
                current_game_active = False
            else:
                print("Input only 'y' or 'n'. Exiting... ")
                current_game_active = False