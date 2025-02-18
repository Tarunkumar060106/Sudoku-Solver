# gui.py
import tkinter as tk
from tkinter import messagebox
from solver import solve  # Import the solve function from solver.py
import random

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.root.geometry("500x550")
        self.root.configure(bg="#f8f9fa")
        
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.fixed_cells = set()  # Store fixed (bold) numbers
        self.setup_ui()

    def setup_ui(self):
        """Create Sudoku grid and buttons"""
        frame = tk.Frame(self.root, bg="#f8f9fa")
        frame.pack(pady=10)

        # Define two colors for alternating 3x3 subgrids
        color1 = "white"
        color2 = "#e6e6e6"  # light gray

        for i in range(9):
            for j in range(9):
                # Determine the subgrid's position
                box_x, box_y = j // 3, i // 3
                # Alternate the background color based on the subgrid
                bg_color = color1 if (box_x + box_y) % 2 == 0 else color2

                e = tk.Entry(frame, width=3, font=('Arial', 18), justify='center', bg=bg_color)
                e.grid(row=i, column=j, padx=2, pady=2, ipady=5)
                e.bind("<KeyRelease>", self.validate_input)
                self.entries[i][j] = e

                # Add thick borders for 3x3 subgrids
                if i % 3 == 0 and i != 0:
                    e.grid(row=i, column=j, padx=2, pady=(5, 2))
                if j % 3 == 0 and j != 0:
                    e.grid(row=i, column=j, padx=(5, 2), pady=2)

        # Buttons
        button_frame = tk.Frame(self.root, bg="#f8f9fa")
        button_frame.pack(pady=20)

        solve_btn = tk.Button(button_frame, text="Solve", command=self.solve_sudoku, font=("Arial", 14), bg="#28a745", fg="white", width=8)
        solve_btn.grid(row=0, column=0, padx=10)

        reset_btn = tk.Button(button_frame, text="Reset", command=self.reset_board, font=("Arial", 14), bg="#dc3545", fg="white", width=8)
        reset_btn.grid(row=0, column=1, padx=10)

        randomize_btn = tk.Button(button_frame, text="Randomize", command=self.load_random_example, font=("Arial", 14), bg="#007bff", fg="white", width=8)
        randomize_btn.grid(row=0, column=2, padx=10)


    def validate_input(self, event):
        """Ensure only numbers (1-9) are entered and clear invalid input."""
        for i in range(9):
            for j in range(9):
                entry = self.entries[i][j]
                val = entry.get()
                if val and (not val.isdigit() or not (1 <= int(val) <= 9)):
                    entry.delete(0, tk.END)  # Remove invalid input

    def get_board(self):
        """Retrieve the board from user input."""
        board = []
        for i in range(9):
            row = []
            for j in range(9):
                val = self.entries[i][j].get()
                row.append(int(val) if val else 0)
            board.append(row)
        return board

    def update_board(self, board):
        """Update the GUI with solved board values."""
        for i in range(9):
            for j in range(9):
                if (i, j) not in self.fixed_cells:
                    self.entries[i][j].delete(0, tk.END)
                    if board[i][j] != 0:
                        self.entries[i][j].insert(0, str(board[i][j]))

    def solve_sudoku(self):
        """Solve Sudoku and update the GUI."""
        board = self.get_board()
        if solve(board):
            self.update_board(board)
            messagebox.showinfo("Success", "Sudoku solved!")
        else:
            messagebox.showerror("Error", "No solution exists.")

    def reset_board(self):
        """Clear the board and allow new input."""
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].config(state="normal", font=('Arial', 18), fg="black")
        self.fixed_cells.clear()

    def load_random_example(self):
        """Load a random sample Sudoku puzzle."""
        examples = [
            [
                [5, 3, 0, 0, 7, 0, 0, 0, 0],
                [6, 0, 0, 1, 9, 5, 0, 0, 0],
                [0, 9, 8, 0, 0, 0, 0, 6, 0],
                [8, 0, 0, 0, 6, 0, 0, 0, 3],
                [4, 0, 0, 8, 0, 3, 0, 0, 1],
                [7, 0, 0, 0, 2, 0, 0, 0, 6],
                [0, 6, 0, 0, 0, 0, 2, 8, 0],
                [0, 0, 0, 4, 1, 9, 0, 0, 5],
                [0, 0, 0, 0, 8, 0, 0, 7, 9]
            ],
            [
                [0, 0, 0, 2, 6, 0, 7, 0, 1],
                [6, 8, 0, 0, 7, 0, 0, 9, 0],
                [1, 9, 0, 0, 0, 4, 5, 0, 0],
                [8, 2, 0, 1, 0, 0, 0, 4, 0],
                [0, 0, 4, 6, 0, 2, 9, 0, 0],
                [0, 5, 0, 0, 0, 3, 0, 2, 8],
                [0, 0, 9, 3, 0, 0, 0, 7, 4],
                [0, 4, 0, 0, 5, 0, 0, 3, 6],
                [7, 0, 3, 0, 1, 8, 0, 0, 0]
            ],
            [
                [0, 2, 0, 6, 0, 8, 0, 0, 0],
                [5, 8, 0, 0, 0, 9, 7, 0, 0],
                [0, 0, 0, 0, 4, 0, 0, 0, 0],
                [3, 7, 0, 0, 0, 0, 5, 0, 0],
                [6, 0, 0, 0, 0, 0, 0, 0, 4],
                [0, 0, 8, 0, 0, 0, 0, 1, 3],
                [0, 0, 0, 0, 2, 0, 0, 0, 0],
                [0, 0, 9, 8, 0, 0, 0, 3, 6],
                [0, 0, 0, 3, 0, 6, 0, 9, 0]
            ]
        ]

        # Choose a random board from the examples list
        example_board = random.choice(examples)

        # Clear any existing numbers and fixed cell markings
        self.fixed_cells.clear()
        for i in range(9):
            for j in range(9):
                self.entries[i][j].config(state="normal", font=('Arial', 18), fg="black")
                self.entries[i][j].delete(0, tk.END)
        
        # Update the GUI with the selected board
        for i in range(9):
            for j in range(9):
                if example_board[i][j] != 0:
                    self.entries[i][j].insert(0, str(example_board[i][j]))
                    self.entries[i][j].config(state="disabled", font=('Arial', 18, 'bold'), fg="blue")
                    self.fixed_cells.add((i, j))
