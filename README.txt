Foundations of Intelligent Systems
ASSIGNMENT 2

SANDHYA MURALI (sm2290@g.rit.edu)
----------------------------------------------------------------------------------
Files in this directory:

ttt.py:  The python file which consists of the code to play the game TicTacToe.
test.sh: Shell script file that runs the script
tests.txt: output file demonstrating same 2 outputs
----------------------------------------------------------------------------------
Steps to Run the code:

1. Extract zip file
1. OPEN cmd (or terminal if Linux or MAC OSX)
2. GO to the path where the folder is saved
3. RUN ./test.sh
4. Give inputs asked and play the Game



OUTPUT INTERPRETATION:

1. Displays the current state of the board

~ ~ ~ 
~ ~ ~ 
~ ~ ~ 

------------------------

2. User makes his first move by entering the x and y position of the board. x ranges from 0 to 2 and y ranges from 0 to 2

Your Turn

enter x0
enter y0
X ~ ~ 
~ ~ ~ 
~ ~ ~ 

------------------------

3. Computer selects his move by running MINMAX and ALPHABETA prunning
   For each move in both the algorithms, the number of nodes generated in the tree are displayed
   Best row and Best column value is produced and places his coin in that position
   In alpha beta pruning, we can see that the number of nodes visited while creating a tree is drastically reduced as compared to minmax


------------------------
Computer Turn

----------MINMAX--------


best row chosen :  1
best column chosen :  1
total number of states : 59704

X ~ ~ 
~ 0 ~ 
~ ~ ~ 

---------- ALPHA BETA------


best row chosen :  1
best column chosen :  1
total number of states : 4089

X ~ ~ 
~ 0 ~ 
~ ~ ~ 


-----------------------

4. User makes his move by inputting x and y positions

Your Turn 

enter x0
enter y1

X X ~ 
~ 0 ~ 
~ ~ ~ 

------------------------

5. Computer makes his move again and gets best choice as (0,2) as it is likely for the opponent to win if he doesnt place his coin there

Computer Turn

----------MINMAX--------


best row chosen :  0
best column chosen :  2
total number of states : 934

X X 0 
~ 0 ~ 
~ ~ ~ 

---------- ALPHA BETA------


best row chosen :  0
best column chosen :  2
total number of states : 220

X X 0 
~ 0 ~ 
~ ~ ~ 


-----------------------


6. User makes his move


Your Turn 

enter x1
enter y0

X X 0 
X 0 ~ 
~ ~ ~ 

------------------------

7. Computer makes his move again and gets best choice as (2,0) as it is likely for the computer to win

Computer Turn

----------MINMAX--------


best row chosen :  2
best column chosen :  0
total number of states : 29

X X 0 
X 0 ~ 
0 ~ ~ 

---------- ALPHA BETA------


best row chosen :  2
best column chosen :  0
total number of states : 24

X X 0 
X 0 ~ 
0 ~ ~ 


8. It displays to the user that we lost and machine wins

 YOU LOST!
