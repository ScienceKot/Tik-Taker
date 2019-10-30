# Tik-Taker
This is a system that I taught to play Tic-Tac-Toe

In this project I created a system that learns to play tic-tac-toe. It learns from a dataset of games where pieces (X and O) were randomly put on the game board. Tik-taker is more an evironment for sklearn algorithms to play tic-tac-toe.

This system was created in 3 steps:
  1) The random game generator;
  2) Processing of the data;
  3) Creation of the environment.


* The game generator - game_generator.py
  In this step I generated 5000 games of Tic-Tac-Toe by randomly placing at every turn a piece of X or O. At every turn of the game the algorithm checked if the game ended up and who is the winner. With this algorithm I generated a database of games where every row is a board placement of players and the next move of the player depending on the game board.

* Processing of the data.
  At this step I prepared the dataset that I got from the previous step to be acceseble for sklearn algorithms. To achieve that I went through the following steps:
  1. I deleted all the first turns in every game - because they don't carry with them any information.
  2. I deleted all the last turns in every game - because they also don't carry with them any usefull information.
  3. I deleted all games which resulted in a tie in order to obtain games that will drive the game to the victory of one part.
  4. I applied dummy variable on the row representation of the game board. 0 -> [0, 0], 1 -> [0, 1], 2 -> [1, 0].
      0 | 0 | 1             [0, 0] | [0, 0] | [0, 1]
      0 | 2 | 2    =====>   [0, 0] | [1, 0] | [1, 0]
      1 | 0 | 0             [0, 1] | [0, 0] | [0, 0]
  5. The dataset was split in 2 ones - X_moves (X_moves.csv) & O_moves (O_moves.csv).
  
  The result dataset have the following columns.
    > GameNr - The game number.
    > MoveNr - The number of the turn.
    > 00-1,00-2,01-1,01-2,02-1,02-2,10-1,10-2,11-1,11-2,12-1,12-2,20-1,20-2,21-1,21-2,22-1,22-2
      The dummy representation of the game board.
      Ex. 00-1, 00-2 represent the cell with coordinates [0, 0] in dummy representation.
    > move_I - The row where the next piece should be placed.
    > move_J - The column where the next piece should be placed.
    > winner - The winner of the game.
* The Tik-Taker (tik_taker.py)
  The Tik-Taker is an environent that allows some sklearn machine learning algorithms (supervised ones) to play Tic-Tac-Toe. For an algorithm to be compatible with that environment it should:
    > Have a .fit() function - to train the model.
    > Have the .predict_proba() function to be able to predict the probability for every cell from the game board that placing on that cell the player will win. The algorithms that were tested on that system are:
      + LogisticRegression
      + GaussianNB
      + BernoulliNB
      + DecisionTreeClassifier
      + GradientBoostingClassifier
      + RandomForestClassifier
      + AdaBoostClassifier
      + SVC (with probability=True)
  The game goes in the following way:
    1. Every player is formed from 2 algorithms of the same type, one is predicting the row, another one is predicting the column of the next cell where the piece will be placed.
    2. Every algorithm gets the game board state and returns a list with probabilities, one for row and one for column.
    3. These 2 lists are multiplied (one is reversed). The algorithms got a matrix with probabilities for every cell.
    4. From these cells we extract the probabilities of all free cells.
    5. By picking the cell with the highest probability we choose the next move of the player.
    
      X | O |      2 | 1 | 0    [1 0] | [0 1] | [0 0]            [0.1 0.3 0.6]     0.02 | 0.06 | 0.12
      O | X | O -> 1 | 2 | 1 -> [0 1] | [1 0] | [0 1] -> Algo ->                -> 0.02 | 0.06 | 0.12
        |   |      0 | 0 | 0    [0 0] | [0 0] | [0 0]            [0.2 0.2 0.6]     0.06 | 0.18 | 0.36
        
    ---- | ---- | 0.12
    ---- | ---- | ---- -> THE RESULT -> [2, 2] the highest probability of winning
    0.06 | 0.18 | 0.36
    
    
    Created by Păpăluță Vasile (Science_kot)
    facebook link: https://www.facebook.com/papaluta.vasile.77
    instagram link: https://www.instagram.com/science_kot/
    e-mail: vpapaluta06@gmail.com vasile.papaluta@microlab.utm.md
