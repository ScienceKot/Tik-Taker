# Importing all the libraries needed to generate random games
import random
import json

def extractAllNonePlaces(matrix):
    ''' Extranting the all places on game board where there is no X or O '''
    list_of_free_boxes = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == -1:
                list_of_free_boxes.append([i, j])
    return list_of_free_boxes

def checkForWinning(matrix):
    ''' Checking if the game ended up and what is the result of the game '''
    winner = -1
    if len(extractAllNonePlaces(matrix)) == 0 and winner ==-1:
        return {"State" : 1, "winner" : -1}
    for line in matrix:
        if line[0] == line[1] and line[1] == line[2] and line[0] != -1:
            winner = line[0]
            break
    for column in range(len(matrix)):
        if matrix[0][column] == matrix[1][column] and matrix[2][column] == matrix[1][column] and matrix[0][column] != -1:
            winner = matrix[0][column]
            break
    if matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2] and matrix[1][1] != -1:
        winner = matrix[0][0]
    if matrix[0][2] == matrix[1][1] and matrix[1][1] == matrix[2][0] and matrix[0][2] != -1:
        winner = matrix[0][2]
    if winner == -1:
        return {"State" : 0}
    else:
        return {"State" : 1, "winner" : winner}

def printMatrix(matrix):
    ''' Print the game board in a form that people can understand easily '''
    for line in matrix:
        print (line)
    print("*"*10)
# history is used to save all games
history = []
# Generating 5000 games of Tic-Tac-Toe
for i in range(5000):
    mat = [
        [-1, -1, -1],
        [-1, -1, -1],
        [-1, -1, -1]
    ]
    GameStats = {"State":0}
    # Starting the game with a O move
    zero = True
    counter=1
    game = []
    places_nr = []
    # Playing the game while there is no winner or while there is no equality
    while GameStats["State"]==0:
        if zero==True:
            # The O player turn
            freePlaces = extractAllNonePlaces(mat)
            places = random.choice(freePlaces)
            places_nr.append(places)
            mat[places[0]][places[1]] = 0
            # Moving to the X player
            zero = False
        else:
            # The X player turn
            freePlaces = extractAllNonePlaces(mat)
            places = random.choice(freePlaces)
            places_nr.append(places)
            mat[places[0]][places[1]] = 1
            # Moving to the O player
            zero = True
        # Appending the game board and what the algorithm has chosen
        game.append([i, counter])
        for el in matrixToLine(mat):
            game[-1].append(el)
        GameStats = checkForWinning(mat)
        counter+=1
    i=0
    for el in game:
        if i==len(places_nr)-1:
            el.append(-1)
            el.append(-1)
        else:
            el.append(places_nr[i+1][0])
            el.append(places_nr[i+1][1])
        el.append(GameStats["winner"])
        i+=1
    history.append(game)
json.dump(history, open("Learn_Data.json", 'w'))
for game in history:
    print (game)
