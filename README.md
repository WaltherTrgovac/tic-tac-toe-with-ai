<h1 align="center">
Tic Tac Toe with AI
</h1>

<h2> 
About the project
</h2>

<p>
This project is a simple implementation of tic tac toe where you have different game modes. Each player can either be a real user or a bot. There are 3 different levels for bots; easy, medium, and hard. Easy bots just play a random move, medium bots always either block opponent's winning move or make a winning move, if possible. Hard bots always play optimally.
</p>

<h2>
How to play
</h2>

<p>
You just need raw python in order to run the script.

You can executing the script by running python <code>.\main\game_menu.py from the root</code> directory of the repository.

After executing the script, you can start any game mode with the command start [player_1] [player_2], where you can choose between commands [user], [easy], [medium], [hard] for each player.
</p>

<h2>
How does the hard bot work?
</h2>

<p>
Hard bot is implemented by using [minimax algorithm](https://en.wikipedia.org/wiki/Minimax). That way we make sure that the bot always plays optimally. I implemented the most easiest version of the algorithm, which causes the code to be longer than it has to be. 
</p>

<h2>
Design patterns
</h2>

<p>
I have used this project to implement my first modified design patterns. I have used Singleton creational pattern for the class GameMenu. We want to have only one instance of the class GameMenu becase that is the main loop of the game. That is the reason why Singleton pattern is used. I have also modified it so that if you try to create 2 instances of the class, an Exception is raised.
</p>

<h2>
Testing
</h2>

<p>
Coming soon
</p>

<h2>
License
</h2>

<p>
MIT
</p>