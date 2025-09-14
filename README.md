# Google Tic Tac Toe Solver

- [Google Tic Tac Toe Solver](#google-tic-tac-toe-solver)
  - [Prefix](#prefix)
  - [Minimax Algorithm](#minimax-algorithm)
  - [In Layman's Term](#in-laymen-term)
  - [What To Do Next](#what-to-do-next)
  - [References](#references)
  - [How To Run The Code](#how-to-run-the-code)

## Prefix

This code reliably beats and draw
[Google's search page Tic Tac Toe web game](https://share.google/QIVITPPSO41av2jKh),
using pyautogui for mouse movement and Minimax algorithm to calculate the moves.

> due to pyautogui limitations, remember to recapture board, restart button and
> adjust `RETINA_FACTOR` for the code to work properly.

## Minimax Algorithm

Tic Tac Toe is a two player zero-sum game, gain of one player must equals to the
loss of the other.

strategic form triplet($X$, $Y$, $A$)

1. $X$ is set of strategies of Player 1
2. $Y$ is set of strategies of Player 2
3. $A$ real-value function defined on $X \times Y$

$A(x,y)$ is a real number for every $x \in X$ and $y \in Y$, assuming each
player chooses their respective move unaware of the choice of the other.

Then calculates $A()$ with choicen $x$, $y$

- Where $A$ is positive, win for Player 1
- Where $B$ is positive, win for Player 2

representing the winnings of Player 1 and losses of Player 2.

> Pure strategies meaning each Player plays to win. If Player plays an average
> game (e.g. blocking other from winning), it will be a mixed strategy.

(too much maths man)

## In Layman's Term

Two Player game, maximise player's score while opponent minimise opponent's
score.

The board can be in 3 possible state:

1. If player wins -> $+10$
2. If opponent wins -> $-10$
3. Draw / in the middle of the game -> $0$

Before every move, simulate the game by playing a move and then simulate all the
possible possible moves of the game and determine which resulting state it will
land and compare the score.

The first move with the best score will be the move to play next.

## What To Do Next

1. Add alpha-beta pruning (still deterministic, brute-force)
2. monte carlo tree search (probabilistic)
3. reinforcement learning (agent)

## References

1. [https://muens.io/minimax-and-mcts/](https://muens.io/minimax-and-mcts/)
2. Maschler, Michael; Solan, Eilon; Zamir, Shmuel (2013). Game Theory. Cambridge University Press. ISBN 9781107005488.

## How To Run The Code

1. screen capture the board
2. install requirements
3. run `python -O bot.py`
