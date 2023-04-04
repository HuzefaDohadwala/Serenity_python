import subprocess
import tkinter as tk

# Define the function to be called when the button is clicked
def run_script():
    # Use subprocess to launch a new process that runs script2.py
    subprocess.Popen(['python', 'quiz.py'])

# Create the GUI window and button
window = tk.Tk()
button = tk.Button(window, text="Run Script", command=run_script)
button.pack()

# Start the GUI event loop
window.mainloop()
