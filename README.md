# rockpaperscissors
Rock Paper Scissors Game

In this project I have created a program to play Rock, Paper, Scissors against a CPU. It's program that picks at random will usually win 50% of the time.

In the file main.py we write a function called player and another called CPU. The CPU function select r, p or s randomly using the random choice module.

Development

The main.py file contains a list that controls the gameplay. When the player and CPU pick the same choice, it prints "It's a tie". Also, when the player beats CPU, it prints "You Win". Viceversa, it prints "You lose".
After the games ends, the program runs a while loop to know if the user would like to play again.
If yes, it starts from the top. Otherwise:
print("BYE! Come again^-^")
