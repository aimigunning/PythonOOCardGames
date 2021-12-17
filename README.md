## Blackjack card game
This project is a console based blackjack card game forked from DerekSomerville (https://github.com/DerekSomervilleUofG/PythonOOCardGames)

It includes some generic card game functionality that can be re-used across other card games.

### What is my aim?
I was tasked with adding unit tests to the methods within the PlayingCard functionality and the Blackjack functionality.

I was also tasked with incorporating an Adapter design pattern. This involved setting up an Input and an Output interface defining the methods to be implemented in each of the classes so that playingcard and blackjack could take console input and output or take a list of test values/write the output to a test list.  This shows how the functioning of the game can be amended easily without needing to change playingcard or blackjack.  

Further adapters could be added e.g. getting input from a file or writing output to a file.

## Rules of the game
The rules for this game can be found here: https://en.wikipedia.org/wiki/Blackjack
