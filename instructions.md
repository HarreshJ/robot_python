Part 1

Write a python program that will display a grid of size 5 X 5

Part 2

Add the following:
- A robot will start at the top left corner of the grid
- Ask a person to type A, W, S, D to move the robot in a direction (assume only a single move per input)
- Move the robot to that position
- Display the path take using 'X' on your grid

Part 3

Add rules to:
- Show a warning and prevent the robot from falling off the grid
- Show a warning and prevent the robot from going back on an already travelled cell

Part 4

Allow for:
- The robot starts on the top left facing right
- When moving in a direction, the robot faces that direction (e.g. after press 'A' / left, the robot will be facing left)
- The command J will make the robot jump 2 cells in the direction is was last facing
  - It can jump over already travelled cell but no land on one

Part 5:

Allow for:
- The command 'R' will make the robot rush in the direction it was last facing until:
  - it meets the edge of the grid or
  - a cell already travelled