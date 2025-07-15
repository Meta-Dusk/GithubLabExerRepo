#text_opener.py

import tkinter as tk
from tkinter import filedialog

# create the event handler to open a file
def open_file():
    file_path = filedialog.askopenfilename(
        title="Open a Text File",
        filetypes=[("Text files", "*.txt")]
    )
    if file_path:
        lHistory['text'] = f"Selected file: {file_path}"
        try:
            with open(file_path, 'r') as file:
                file_contents.delete('1.0', tk.END)
                file_contents.insert('1.0', file.read())
        except Exception as e:
            file_contents.delete('1.0', tk.END)
            file_contents.insert('1.0', f"Error reading file: {e}")

# create the top level window/frame
top = tk.Tk()
F = tk.Frame(top)
F.pack(fill="both")

top.title("Text File Viewer")

# Label to display the selected file path
lHistory = tk.Label(F, text="", foreground="darkgreen")
lHistory.pack(side="top", fill="x", pady=5)

# Text widget to display file contents
file_contents = tk.Text(F, height=20, width=70, wrap="word")
file_contents.pack(pady=10)

# Button to open the file dialog
bOpenFile = tk.Button(F, text="Open File", command=open_file)
bOpenFile.pack(side="top", padx=5, pady=2)

# Button to quit the application
bQuit = tk.Button(F, text="Quit", command=top.quit)
bQuit.pack(side="top", padx=5, pady=2)

# Now run the eventloop
F.mainloop()
