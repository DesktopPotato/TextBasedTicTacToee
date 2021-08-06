#initialization
valid = False  #Whenever the player enters values for row and column
               #this variable will make sure that they are valid

terminate = False           #program termination

over = False                #game over

first_player = True         #Player 'X' goes first.




#Initialization for the graphical stuff that will display board

vert = '|'   #vertical line
blank = '   '   #blank characters
line = '-' * ((len(blank)*3)+2)    #A horizontal line

grid = ((1,1), (1,2), (1,3), (2,1), (2,2), (2,3), (3,1), (3,2), (3,3))
# The grid has rows and columns


grid_slot = {i:blank for i in grid} #Initializes the grid. Currently,
#each slot is blank. Whenever a player chooses a slot during their
#chance, that slot gets occupied by that particular player

win_condition = (((1,1), (1,2), (1,3)), ((1,1), (2,1), (3,1)),
    ((1,1), (2,2), (3,3)), ((2,1), (2,2), (2,3)), ((3,1), (3,2), (3,3)),
    ((1,3), (2,2), (3,1)), ((1,2), (2,2), (3,2)), ((1,3), (2,3), (3,3)))    
# If the player's grid slots match any of the above tuples,
# the player wins.




#Function initialization

def display_Board():   #Displays the board during the first chance
    for i in range(1,6):
        if i % 2 == 0:
            print(line)   
        else:
            print(blank + vert + blank + vert + blank)  
    print('\n\n')


            
def update_Board():   #Displays the board again after every move
    print('\n\n')
    for i in range(1,6):
        if i == 1:
            print(grid_slot[(1,1)] + vert + grid_slot[(2,1)] + vert +
                  grid_slot[(3,1)])  #Slots for the first row
        elif i == 3:
            print(grid_slot[(1,2)] + vert + grid_slot[(2,2)] + vert +
                  grid_slot[(3,2)])  #Slots for the second row 
        elif i == 5:
            print(grid_slot[(1,3)] + vert + grid_slot[(2,3)] + vert +
                  grid_slot[(3,3)])  #Slots for the third row
        else:
            print(line)
    print('\n\n')


    
def entering():     #The player enters their move
    global first_player   
    
    if first_player == True:   
        entry = format('X', '^3')  #entry is the variable that will
                                   #replace the 'blank' in the chosen
                                   #slot
        print("Player 1's turn!")

    elif first_player == False:
        entry = format('O', '^3')
        print("Player 2's turn!")


    #Asking the user for the row and column to be entered
    column = int(input("Enter column:"))
    row = int(input("Enter row:"))
    valid = ((column, row) in grid) and not ((column, row) in \
            tuple(i for i,j in grid_slot.items()\
                  if j != blank))
    #In the code above, two conditions are being checked:
    #1) The input row and column are not outside the 3x3 grid
    #2) The input row and column were not already occupied by
    # any player in any of the previous chances
    
    while not valid:  #If the input values are not valid, enter loop
        column = int(input("INVALID - Enter column(1-3):"))
        row = int(input("Enter row:"))
        valid = ((column, row) in grid) and not ((column, row) in \
            tuple(i for i,j in grid_slot.items()\
                  if j != blank))
    #Once the loop finishes, the values are valid
    #So, in the next code, we modify the grid slot from being 'blank' 
    #to 'occupied' 
    grid_slot[(column, row)] = entry  


    # When A's turn is done, B takes the next turn
    if first_player == True:
        first_player = False
    elif first_player == False:
        first_player = True

    update_Board()  #Display the board each time a player makes
                    #his/her move



def wincheck():   #To check if a player has won the game
    global over   


    #Mindbending stuff ahead (IMO)
    x = tuple(coord for coord,occupied in grid_slot.items() if\
    occupied == ' X ') # Tuple containing all slots occupied by X
    o = tuple(coord for coord,occupied in grid_slot.items() if\
    occupied == ' O ') # Tuple containing all slots occupied by O

    combx = []  #Initializing an empty list for combinations (nCr)
                #of tuples (taken 3 at once) possible for player X
    combo = []  #Same thing as above, but for O

    #MIND BENDER REGION
    for i, j in enumerate(x):   #Creating combinations and appending   
        for k in range(i + 1, len(x)):
            for z in range(k+1, len(x)):
                combx.append((j, x[k], x[z]))
    for i, j in enumerate(o):
        for k in range(i + 1, len(o)):
            for z in range(k+1, len(o)):
                combo.append((j, o[k], o[z]))
    

    for comb in combx:  #If any of the combinations matches the win
                        #condition, the player wins and the game is over
        if comb in win_condition:
            print("Player 1 wins!")
            over = True
    for comb in combo:    
        if comb in win_condition:
            print("Player 2 wins!")
            over = True

    #Taking the case of a draw game
    draw_var = 9    #Integer assigned to this variable. Every time a 
                    #slot gets filled, the number is decreased.
                    #When this number reaches 0, the game is a draw
    for i, j in grid_slot.items():
        if j != blank:
            draw_var = draw_var - 1
    if draw_var == 0:
        over = True
        print("\nThe game is a draw!\n")
    
    


#program
print("Welcome to the Tic-Tac-Toe Game!\n\n")

while not terminate:  #Main loop
    display_Board() #Displaying the board for the first chance

    while not over: #While game isn't over, this code will keep looping
        entering()  #Players enter the value
        wincheck()  #This function is called each time players enter
                    #their values.
        
    # The loop above keeps carrying on until the game is over.
    # After the game is over, the lines below are executed
    another = input("Game over! Would you like to play another game?(y/n):")

    #To make sure that the player enters y or n.
    while (another != 'y' and another != 'n'):  
        another = input("Please type either y or n:")

    if another == 'n':
        terminate = True #Program terminates

    elif another == 'y': 
        print('Here\'s another game!\n\n')

        #Re-initiazliation and then the main loop continues
        valid = False
        terminate = False
        over = False
        first_player = True
        grid_slot = {i:blank for i in grid}
        
