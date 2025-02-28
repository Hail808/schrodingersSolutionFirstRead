import ollama
import tkinter as tk
from tkinter import simpledialog, messagebox

SELECTED_MODEL = 'qwen2.5-coder:0.5b'

def get_response(content):
    response = ollama.chat(
        model=SELECTED_MODEL,
        messages=[
            {
                'role': 'user', 
                'content': content
            }
        ]
    )
    return response['message']['content']


# Create the main window
root = tk.Tk()
root.title("Schrodinger's Solution")

# Create a text box for user input
text_box = tk.Text(root, height=10, width=50)
text_box.pack(pady=20)

def on_submit():
    content = text_box.get("1.0", tk.END).strip()
    if content:
        response_content = get_response(content)
        messagebox.showinfo("Response", response_content)

# Create a button to submit the input
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack(pady=20)

# Run the application
root.mainloop()