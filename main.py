import tkinter as tk
from SolverCode.gui import SudokuGUI

if __name__ == "__main__":
    root = tk.Tk()
    
    # Set the desired window dimensions
    window_width = 500
    window_height = 550

    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate position x and y coordinates to center the window
    x = int((screen_width - window_width) / 2)
    y = int((screen_height - window_height) / 2)
    
    # Set the geometry of the window
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    app = SudokuGUI(root)
    root.mainloop()
