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

You can executing the script by running python .\main\game_menu.py from the root directory of the repository.

After executing the script, you can start any game mode with the command start [player_1] [player_2], where you can choose between commands [user], [easy], [medium], [hard] for each player.
</p>

<h2>
How does the hard bot work?
</h2>

<p>
Hard bot is implemented by using minimax algorithm. That way we make sure that the bot always plays optimally. I implemented the most easiest version of the algorithm, which causes the code to be longer than it has to be. 
</p>

<h2>
License
</h2>

<p>
MIT
</p>