import tkinter as tk
from tkinter import messagebox
from spellchecker import SpellChecker
from PyDictionary import PyDictionary

def check_spelling():
    text = text_entry.get("1.0", "end-1c")
    spell = SpellChecker()
    dictionary = PyDictionary()
    words = text.split()

    suggestions = {}
    meanings = {}
    for word in words:
        correction = spell.correction(word)
        suggestions[word] = correction
        meanings[word] = dictionary.meaning(correction)

    misspelled = spell.unknown(words)

    if len(misspelled) > 0:
        suggestion_text.config(state="normal")
        suggestion_text.delete("1.0", "end")
        for word in words:
            suggestion_text.insert("end", f"{word}: {suggestions[word]}\n")
            if word in meanings:
                suggestion_text.insert("end", f"Meaning: {meanings[word]}\n\n")
        suggestion_text.config(state="disabled")
        messagebox.showinfo("Spelling Check", "Misspelled words found!")
    else:
        suggestion_text.config(state="normal")
        suggestion_text.delete("1.0", "end")
        suggestion_text.config(state="disabled")
        messagebox.showinfo("Spelling Check", "No misspelled words found!")

# Create the main window
window = tk.Tk()
window.title("Spell Checker")

# Create a text entry field
text_entry = tk.Text(window, height=10, width=50)
text_entry.pack()

# Create a button to check spelling
check_button = tk.Button(window, text="Check Spelling", command=check_spelling)
check_button.pack()

# Create a non-editable text field for suggestions and meanings
suggestion_text = tk.Text(window, height=12, width=50, state="disabled")
suggestion_text.pack()

# Run the main window's event loop
window.mainloop()
