# Python----GameOfLife
Game of life in python

Conways’s Game Of Life is a Cellular Automation Method created by John Conway. This game was created with Biology in mind but has been applied in various fields such as Graphics, terrain generation,etc..

<img src="images/image.png"/>

The “game” is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves, or, for advanced “players”, by creating patterns with particular properties.

<img src="images/screen1.png"/>

Because the Game of Life is built on a grid of nine squares, every cell has eight neighboring cells,as shown in the given figure. A given cell (i, j) in the simulation is accessed on a grid [i][j], where i and j are the row and column indices, respectively. The value of a given cell at a given instant of time depends on the state of its neighbors at the previous time step. Conway’s Game of Life has four rules.
If a cell is ON and has fewer than two neighbors that are ON, it turns OFF
If a cell is ON and has either two or three neighbors that are ON, it remains ON.
