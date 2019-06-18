# smaeGame

  The game is played on a grid, filled with lettered tiles. The objective is to clear the grid by removing
groups of tiles of the same letter. The tile that doesn’t have any neighboring tile with the same letter
cannot be cleared. Only tiles that are immediately adjacent to each other may be cleared, which means
cross neighboring is not allowed.
You get points for each group you remove and the larger the group, the more points you get. Hint
displays an [X,Y] pair included in the largest block. To get the highest score you need to make large
blocks of one letter.

# Game Scoring schema:
  • P = (n-2)^2 for each group of tiles cleared, n is number of tiles in group, if hint is used p/2
  
  • final score is: score – (number of remaining tiles)
  
  • (score * 5) if you clear all the tiles
