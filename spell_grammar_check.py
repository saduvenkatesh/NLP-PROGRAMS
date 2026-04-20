# GRAMMAR & SPELL CHECKER 

# Title, why this project?, pipeline, Gui, NLP techniques used, Applications in real world

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
from textblob import TextBlob
import language_tool_python

# Initialize grammar tool
tool = language_tool_python.LanguageTool('en-US')



# FUNCTIONS


def check_spelling(text):
    blob = TextBlob(text)
    return str(blob.correct())


def check_grammar(text):
    matches = tool.check(text)
    corrected_text = language_tool_python.utils.correct(text, matches)
    return corrected_text, matches


def run_checker():
    text = input_text.get("1.0", tk.END).strip()
    
    if not text:
        messagebox.showwarning("Warning", "Please enter some text!")
        return

    # Spell correction
    spelling_corrected = check_spelling(text)

    # Grammar correction
    grammar_corrected, matches = check_grammar(spelling_corrected)

    # Display results
    output_text.delete("1.0", tk.END)
    
    output_text.insert(tk.END, "===== ORIGINAL TEXT =====\n")
    output_text.insert(tk.END, text + "\n\n")

    output_text.insert(tk.END, "===== SPELL CORRECTED =====\n")
    output_text.insert(tk.END, spelling_corrected + "\n\n")

    output_text.insert(tk.END, "===== GRAMMAR CORRECTED =====\n")
    output_text.insert(tk.END, grammar_corrected + "\n\n")

    output_text.insert(tk.END, "===== ERRORS =====\n")
    
    if not matches:
        output_text.insert(tk.END, "No grammar mistakes found ✅\n")
    else:
        for i, match in enumerate(matches, 1):
            output_text.insert(tk.END, f"{i}. {match.message}\n")
            if match.replacements:
                output_text.insert(tk.END, f"   Suggestions: {', '.join(match.replacements[:3])}\n")
            output_text.insert(tk.END, "-"*40 + "\n")


def clear_text():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)


def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            input_text.delete("1.0", tk.END)
            input_text.insert(tk.END, content)


def save_output():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text Files", "*.txt")])
    
    if file_path:
        with open(file_path, 'w', encoding='utf-8') as file:
            content = output_text.get("1.0", tk.END)
            file.write(content)
        messagebox.showinfo("Saved", "File saved successfully!")


# GUI WINDOW


root = tk.Tk()
root.title("Grammar & Spell Checker")
root.geometry("800x600")
root.config(bg="#f0f0f0")

# Title
title = tk.Label(root, text="Grammar & Spell Checker", font=("Arial", 18, "bold"), bg="#f0f0f0")
title.pack(pady=10)

# Input Label
input_label = tk.Label(root, text="Enter Text:", font=("Arial", 12), bg="#f0f0f0")
input_label.pack()

# Input Text Box
input_text = scrolledtext.ScrolledText(root, height=8, width=80)
input_text.pack(pady=5)

# Buttons Frame
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

check_btn = tk.Button(button_frame, text="Check", width=12, command=run_checker, bg="#4CAF50", fg="white")
check_btn.grid(row=0, column=0, padx=5)

clear_btn = tk.Button(button_frame, text="Clear", width=12, command=clear_text, bg="#f44336", fg="white")
clear_btn.grid(row=0, column=1, padx=5)

load_btn = tk.Button(button_frame, text="Load File", width=12, command=load_file, bg="#2196F3", fg="white")
load_btn.grid(row=0, column=2, padx=5)

save_btn = tk.Button(button_frame, text="Save Output", width=12, command=save_output, bg="#FF9800", fg="white")
save_btn.grid(row=0, column=3, padx=5)

# Output Label
output_label = tk.Label(root, text="Output:", font=("Arial", 12), bg="#f0f0f0")
output_label.pack()

# Output Text Box
output_text = scrolledtext.ScrolledText(root, height=12, width=80)
output_text.pack(pady=5)

# Run GUI
root.mainloop()