# Pong-Game-Using-Turtle-in-Python
The provided code is an implementation of the classic game Pong using the Python Turtle module. Pong is a two-player game where each player controls a paddle and tries to hit a ball back and forth across the screen. The objective is to prevent the ball from passing the player's paddle while trying to make the ball pass the opponent's paddle.

The code begins by importing the necessary modules: turtle, tkinter, and winsound. The turtle module is used for creating the game graphics, tkinter is used to change the icon of the turtle window, and winsound is used to play sound effects during the game.

The code defines several functions to move the paddles up and down. These functions are bound to specific keys on the keyboard using the window.onkeypress() function. When a key is pressed, the corresponding function is called to move the paddle in the desired direction.

The code then initializes the turtle window and sets its properties, such as the title, background color, and size. It also sets the speed of the window to 0, which means the animations will be as fast as possible.

Next, the code creates the left and right paddles using the turtle.Turtle() class. The paddles are square-shaped and have a red color. They are positioned on the left and right sides of the window using the goto() function.

After that, the code creates the ball using the turtle.Turtle() class. The ball is circular and also has a red color. It is positioned at the center of the window using the goto() function. The ball has two attributes, dx and dy, which represent the change in the x and y coordinates of the ball, respectively. These attributes control the movement of the ball.

The code also creates a scoreboard using the turtle.Turtle() class. The scoreboard is positioned at the top of the window and displays the scores of both players. The scores are initially set to 0.

The main game loop starts with a while True loop. Inside the loop, the window is updated using the window.update() function. This function refreshes the window and allows the animations to be displayed.

The ball is then moved by updating its x and y coordinates based on its dx and dy attributes. The ball's position is updated using the setx() and sety() functions.

The code checks if the ball hits the horizontal walls of the window. If it does, the ball's dy attribute is reversed to make it bounce off the walls. The winsound.PlaySound() function is used to play a sound effect when the ball hits the walls.

The code also checks if the ball misses the paddles and hits the vertical walls. If it does, the ball is reset to the center of the window, the direction of the ball is changed, and the score of the corresponding player is increased. The scoreboard is updated to display the new scores.

The code keeps track of the number of bounces the ball has made. If the number of bounces is a multiple of 3, the speed of the ball is increased by modifying its dx and dy attributes.

The game loop also checks if either player has reached a score of 10. If a player reaches a score of 10, the game ends, and a message is displayed on the scoreboard declaring the winner. The winsound.PlaySound() function is used to play a sound effect when a player wins. After a short delay, the turtle window is closed using the window.bye() function.

Finally, the game loop checks if the ball hits the paddles. If it does, the ball's dx attribute is reversed to make it bounce off the paddles. The winsound.PlaySound() function is used to play a sound effect when the ball hits the paddles.

Overall, the code implements the game logic of Pong using the Python Turtle module and provides a basic graphical interface for the game.
