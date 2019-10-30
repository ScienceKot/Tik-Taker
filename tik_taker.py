# Importing the needed libraries
import pandas as pd
import numpy as np
import random
import os
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB, BernoulliNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier, AdaBoostClassifier
from sklearn.svm import SVC
from tkinter import *
import time
# --------------------- IMPORTING THE LEARNING DATASET ---------------------
# Importing the best X Moves
df = pd.read_csv('X_moves.csv')
table = df[['00-1', '00-2', '01-1', '01-2', '02-1', '02-2', '10-1', '10-2', '11-1', '11-2', '12-1', '12-2', '20-1', '20-2', '21-1', '21-2', '22-1', '22-2']]
res_I= df[['move_I']]
res_J = df[['move_J']]

# Creating the X player
lr_I = AdaBoostClassifier(random_state=0)
lr_I.fit(table, res_I)
lr_J = AdaBoostClassifier(random_state=0)
lr_J.fit(table, res_J)
# Importing the best O Moves
df1 = pd.read_csv('O_moves.csv')
df1 = df1[(df1["winner"]==1) & (df1['move_I']!=-1)]
table = df1[['00-1', '00-2', '01-1', '01-2', '02-1', '02-2', '10-1', '10-2', '11-1', '11-2', '12-1', '12-2', '20-1', '20-2', '21-1', '21-2', '22-1', '22-2']]
res_I= df1[['move_I']]
res_J = df1[['move_J']]
#Creating the O player
lr_I0 = GradientBoostingClassifier(random_state=0)
lr_I0.fit(table, res_I)
lr_J0 = GradientBoostingClassifier(random_state=0)
lr_J0.fit(table, res_J)
def matrixToLine(matrix):
    ''' Converting the board matrix to a line array for algorithms '''
    return [el for line in matrix for el in line]
def forAI(matrix):
    ''' Converting the line array to form that consists only from 0s and 1s using transformator  '''
    l=[]
    for i in matrix:
        l.append(transformator[i][0])
        l.append(transformator[i][1])
    return l
def extractAllNonePlaces(matrix):
    ''' Extranting the all places on game board where there is no X or O '''
    list_of_free_boxes = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                list_of_free_boxes.append([i, j])
    return list_of_free_boxes

def checkForWinning(matrix):
    ''' Checking if the game ended up and what is the result of the game '''
    winner = 0
    if len(extractAllNonePlaces(matrix)) == 0 and winner ==0:
        return {"State" : 1, "winner" : 0}
    for line in matrix:
        if line[0] == line[1] and line[1] == line[2] and line[0] != 0:
            winner = line[0]
            break
    for column in range(len(matrix)):
        if matrix[0][column] == matrix[1][column] and matrix[2][column] == matrix[1][column] and matrix[0][column] != 0:
            winner = matrix[0][column]
            break
    if matrix[0][0] == matrix[1][1] and matrix[1][1] == matrix[2][2] and matrix[1][1] != 0:
        winner = matrix[0][0]
    if matrix[0][2] == matrix[1][1] and matrix[1][1] == matrix[2][0] and matrix[0][2] != 0:
        winner = matrix[0][2]
    if winner == 0:
        return {"State" : 0}
    else:
        return {"State" : 1, "winner" : winner}
def printMatrix(matrix):
    ''' Print the game board in a form that people can understand easily '''
    for line in matrix:
        print (line)
    print("*"*10)
XO = [' ', 'O', 'X']
def printXO(matrix):
    ''' Printing the board of numbers as X and O '''
    XO = [' ', 'O', 'X']
    print('+-+-+-+')
    print('|{}|{}|{}|'.format(XO[matrix[0][0]], XO[matrix[0][1]], XO[matrix[0][2]]))
    print('+-+-+-+')
    print('|{}|{}|{}|'.format(XO[matrix[1][0]], XO[matrix[1][1]], XO[matrix[1][2]]))
    print('+-+-+-+')
    print('|{}|{}|{}|'.format(XO[matrix[2][0]], XO[matrix[2][1]], XO[matrix[2][2]]))
    print('+-+-+-+')
# Is used to convert matrix indexes to array indexes
indexes = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]]
# Is used to transform categorical features to dummy variables
transformator = [[0,0], [1,0], [0,1]]
# I used to tack the score
GAME_SCORES = {'X': 0, 'O':0}
# I'm using tkinter for graphical representation of game board
root  = Tk()
str00 = StringVar()
str00.set('0')
score = Frame(root)
score.grid(row=0)
X_score = Label(score, text='X score - {}'.format(GAME_SCORES['X']))
O_score = Label(score, text='0 score - {}'.format(GAME_SCORES['O']))

X_score.grid(row=0, column=0)
O_score.grid(row=0, column=1)
score.grid(row=0)
board_frame = Frame(root)
board_frame.grid(row=1)

field00 = Label(board_frame, text=str(XO[0]), fg='white', bg='black')
field01 = Label(board_frame, text=str(XO[0]), fg='white', bg='black')
field02 = Label(board_frame, text=str(XO[0]), fg='white', bg='black')
field10 = Label(board_frame, text=str(XO[0]), fg='white', bg='black')
field11 = Label(board_frame, text=str(XO[0]), fg='white', bg='black')
field12 = Label(board_frame, text=str(XO[0]), fg='white', bg='black')
field20 = Label(board_frame, text=str(XO[0]), fg='white', bg='black')
field21 = Label(board_frame, text=str(XO[0]), fg='white', bg='black')
field22 = Label(board_frame, text=str(XO[0]), fg='white', bg='black')

field00.grid(row=0, column=0, padx=5, pady=5)
field01.grid(row=0, column=1, padx=5, pady=5)
field02.grid(row=0, column=2, padx=5, pady=5)
field10.grid(row=1, column=0, padx=5, pady=5)
field11.grid(row=1, column=1, padx=5, pady=5)
field12.grid(row=1, column=2, padx=5, pady=5)
field20.grid(row=2, column=0, padx=5, pady=5)
field21.grid(row=2, column=1, padx=5, pady=5)
field22.grid(row=2, column=2, padx=5, pady=5)
gui_mat = [[field00, field01, field02],
            [field10, field11, field12],
            [field20, field21, field22]]
def change_Table(mat):
    ''' Showing on graphical representation the game board with scores '''
    field00.config(text=XO[mat[0][0]])
    field01.config(text=XO[mat[0][1]])
    field02.config(text=XO[mat[0][2]])
    field10.config(text=XO[mat[1][0]])
    field11.config(text=XO[mat[1][1]])
    field12.config(text=XO[mat[1][2]])
    field20.config(text=XO[mat[2][0]])
    field21.config(text=XO[mat[2][1]])
    field22.config(text=XO[mat[2][2]])
mat = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
GameStats = {"State": 0}
turn = -1
def take_turn():
    ''' THis function will recursively take turns and create games based on players response to game board '''
    # Importing all global variables
    global GameStats, turn, lr_I, lr_I0, lr_J, lr_J0, mat, gui_mat, GAME_SCORES, XO
    # Showing the score based on winned number of games int the past
    X_score.configure(text=str('X score - {}'.format(GAME_SCORES['X'])))
    O_score.configure(text=str('O score - {}'.format(GAME_SCORES['O'])))
    # Checking if the game is on going (GameStats['State'] = 0 )
    if GameStats['State'] == 0:
        # Starting the first turn of every game with a random place
        if turn == -1:
            I = random.randint(0, 2)
            J = random.randint(0, 2)
            mat[int(I)][int(J)] = 1
            gui_mat[int(I)][int(J)].config(text=str(XO[1]))
            turn=1
        elif turn == 1:
            # The turn of X
            X = forAI(matrixToLine(mat))
            I = lr_I.predict_proba([X])
            J = lr_J.predict_proba([X])
            all = np.dot(I.T, J)
            all = all.tolist()
            permise = []
            for pos in extractAllNonePlaces(mat):
                permise.append(all[pos[0]][pos[1]])
            maxi = max(permise)
            for i in range(len(all)):
                for j in range(len(all[0])):
                    if all[i][j] == maxi and [i, j] in extractAllNonePlaces(mat):
                        move_I = i
                        move_J = j
            mat[int(move_I)][int(move_J)] = 2
            gui_mat[int(move_I)][int(move_J)].configure(text=str(XO[2]))
            GameStats = checkForWinning(mat)
            turn = 2
        else:
            # The turn of O
            X = forAI(matrixToLine(mat))
            I = lr_I0.predict_proba([X])
            J = lr_J0.predict_proba([X])
            all = np.dot(I.T, J)
            all = all.tolist()
            permise = []
            for pos in extractAllNonePlaces(mat):
                permise.append(all[pos[0]][pos[1]])
            maxi = max(permise)
            for i in range(len(all)):
                for j in range(len(all[0])):
                    if all[i][j] == maxi and [i, j] in extractAllNonePlaces(mat):
                        move_I = i
                        move_J = j
            mat[int(move_I)][int(move_J)] = 1
            gui_mat[int(move_I)][int(move_J)].configure(text=str(XO[1]))
            GameStats = checkForWinning(mat)
            turn = 1
        root.after(400, take_turn)
    else:
        # If the GameState['State'] = 1 Game if over
        GameStats = checkForWinning(mat)
        print (GameStats)
        # Chencking if the game didn't end with equality
        if GameStats['winner'] != 0:
            GAME_SCORES[XO[GameStats['winner']]] += 1
        # Reseting the board game
        mat=[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                gui_mat[int(i)][int(j)].configure(text=str(XO[0]))
        GameStats['State'] = 0; turn = -1
        root.after(400, take_turn)
take_turn()
# Repeating the process to infinity
root.mainloop()
