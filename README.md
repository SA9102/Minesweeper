# Minesweeper

Minesweeper game using Python and Pygame.

All code is by me.

## How to install

1. Clone the respository using ```git clone https://github.com/SA9102/Minesweeper.git```
2. Run main.py in Python IDLE (there seems to be unknown compilation issues when using Visual Studio Code, so run it with just the standard Python IDLE)

## Change Log

- 19/09/2022:
  - Bug where other tiles further away become selected has been fixed
  - Changed the look of 'clicked' and 'unclicked' tiles to create a nice 3D effect similar to the Windows 98 version of Minesweeper
  - Made tiles a little bigger
  - The game now only detects one mouse click, when in the previous version the game would detect whenever the mouse button is held down, which resulted in being able to click tiles while holding down the mouse button and moving the mouse
  - Mark a tile by clicking the right mouse button
  - Number of mines remaining is displayed
  - Lose when you click on a mine. All mines will then be shown in red
  - Press the space bar to start a new game
