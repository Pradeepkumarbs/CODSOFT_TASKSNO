# CODSOFT AI Internship - Task 2
## Tic-Tac-Toe AI

### Objective
Implement an AI agent that plays the classic Tic-Tac-Toe game against a human player. The AI uses the **Minimax algorithm** to evaluate possible future game states and choose an optimal move.

### Technologies
- Python 3
- Minimax algorithm
- `math` module from the Python standard library

### Features
- Human vs AI gameplay
- 3x3 Tic-Tac-Toe board
- Minimax-based AI
- Input validation
- Win, loss, and draw detection
- The AI evaluates possible moves before selecting its move

### Project Structure

```text
CODSOFT_TASK2_Tic_Tac_Toe_AI/
├── tic_tac_toe.py
├── README.md
└── requirements.txt
```

### How to Run

1. Install Python 3.
2. Open a terminal in this project folder.
3. Run:

```bash
python tic_tac_toe.py
```

No external packages are required.

### How to Play

- You play as `O`.
- The AI plays as `X`.
- Select a position from 1 to 9.

```text
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

### How Minimax Works

The game tree is explored recursively:

- An AI win receives a score of `+1`.
- A human win receives a score of `-1`.
- A draw receives a score of `0`.
- On the AI turn, the algorithm maximizes the score.
- On the human turn, the algorithm minimizes the score.

The AI temporarily plays each available move, evaluates the resulting game state, and selects the move with the highest score.

### Example

```text
You are O. The AI is X.

Enter your move (1-9): 5
AI is thinking...
```

The AI then evaluates the available positions and chooses its optimal move.

### Internship Requirement
The CodSoft Artificial Intelligence internship task document identifies Task 2 as Tic-Tac-Toe AI and specifically suggests Minimax, with or without Alpha-Beta Pruning, to make the AI player unbeatable.

### Future Improvements
- Add Alpha-Beta Pruning for faster search.
- Add difficulty levels.
- Create a graphical interface using Tkinter.
- Add a score tracker across multiple rounds.
- Allow the user to choose X or O.
