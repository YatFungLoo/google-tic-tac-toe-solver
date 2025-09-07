# Google Tic Tac Toe Solver

- [Google Tic Tac Toe Solver](#google-tic-tac-toe-solver)
  - [Minimax Algorithm](#minimax-algorithm)
  - [Core Idea](#core-idea)
  - [Payoff Matrix](#payoff-matrix)
  - [what to do next](#what-to-do-next)
  - [References](#references)
  - [How to run the code](#how-to-run-the-code)

doing some stuff with pyautogui

Trying to beat this one ->
[https://share.google/QIVITPPSO41av2jKh](https://share.google/QIVITPPSO41av2jKh)

## Minimax Algorithm

this works because tic tac toe is a zero-sum game, only two player, gain of one
player equals to the loss of the other.

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

## Core Idea

Two Player game, I want to maximise the score while opponent wants to minimise
the score.

3 possible state:

1. If I got opps -> +10
2. If opps caught me -> -10
3. Draw / in the middle of the game -> 0

Before every move, play a move and simulate all the possible moves of the game
and determine which resulting state it will land and compare the score.

## Payoff Matrix

9 squares takes 4 plays to justify winning strategies. The strategic form
representing the game as a matrix in a table form, assuming both players select
strategies before the game is played using those strategies in turn.

## what to do next

1. Add alpha-beta pruning (still deterministic, brute-force)
2. monte carlo tree search (probabilistic)
3. reinforcement learning (agent)

## References

1. [https://muens.io/minimax-and-mcts/](https://muens.io/minimax-and-mcts/)


## How to run the code

1. screen capture the board
2. install requirements
3. run `python -O bot.py`
