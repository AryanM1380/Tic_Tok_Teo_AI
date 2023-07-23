
# Tic-Tac-Toe AI with Minimax Algorithm

This is a Python implementation of the classic Tic-Tac-Toe game where the computer never loses. The game uses the minimax algorithm, a recursive decision-making algorithm, to ensure the computer makes optimal moves and guarantees at least a draw against any opponent.

## Table of Contents
- [Introduction](#introduction)
- [How to Play](#how-to-play)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## Introduction

Tic-Tac-Toe is a two-player game played on a 3x3 grid. Players take turns to place their symbol ('X' or 'O') on the board. The objective is to get three of your symbols in a row, either horizontally, vertically, or diagonally, to win the game.

This project utilizes the minimax algorithm, a widely-used algorithm in game theory, to ensure that the AI opponent never loses. The minimax algorithm searches through all possible moves and assigns scores to each move, allowing the AI to choose the best move based on the current board state.

## How to Play

1. The game starts with an empty 3x3 grid.
2. The player and the AI take turns to make their moves.
3. The player's move is denoted by 'O', and the AI's move is denoted by 'X'.
4. To make a move, the player needs to enter the row and column coordinates of their desired position on the board.
5. The game continues until one of the players wins or the board is full (a tie).

## Requirements

To run this project, you need to have the following installed:

- Python 3.x

## Installation

1. Clone this repository to your local machine or download the ZIP file and extract it.
2. Navigate to the project directory in your terminal.

## Usage

To play the Tic-Tac-Toe game against the AI, follow these steps:

1. Open a terminal and navigate to the project directory.
2. Run the following command:

```
python tic_tac_toe_AI.py
```

3. The game will start, and you will see the empty Tic-Tac-Toe board.
4. Enter the row and column coordinates to make your move. For example, if you want to place your symbol in the top-left corner, enter `0` for the row and `0` for the column.

Enjoy playing against the unbeatable AI!


---

Feel free to customize this README file based on your project's specific details and requirements. You can also add sections like "Contributing," "Acknowledgments," and "Contact" if applicable.
