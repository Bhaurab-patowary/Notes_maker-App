import customtkinter
import customtkinter as ctk

from  tkinter import filedialog, messagebox
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


app = customtkinter.CTk()
app.geometry("500x600")
app.resizable(False, False)
app.title("Notes App")

# functions

def new_note():
    text_area.delete("1.0", "end")
    app.title("Untitled - file name")

def save_note():
    note_content = text_area.get("1.0", "end-1c")
    if not note_content.strip():
        messagebox.showwarning("Empty Note", "Write something before saving")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(note_content)
        app.title(f"{os.path.basename(file_path)} - file name")

def open_note():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            text_area.delete("1.0", "end")
            text_area.insert("1.0", f.read())
        app.title(f"{os.path.basename(file_path)} - file name")

def clear_note():
    text_area.delete("1.0", "end")

# UI Components
frame = ctk.CTkFrame(app, corner_radius=15)
frame.pack(padx=10, pady=10, fill="both", expand=True)

# Buttons
button_frame = ctk.CTkFrame(frame)
button_frame.pack(fill="x", pady=(5, 10))

new_btn = ctk.CTkButton(button_frame, text="🆕 New", command=new_note, width=100)
open_btn = ctk.CTkButton(button_frame, text="📂 Open", command=open_note, width=100)
save_btn = ctk.CTkButton(button_frame, text="💾 Save", command=save_note, width=100)
clear_btn = ctk.CTkButton(button_frame, text="🧹 Clear", command=clear_note, width=100)

new_btn.pack(side="left", padx=7, pady=5)
open_btn.pack(side="left", padx=7, pady=5)
save_btn.pack(side="left", padx=7, pady=5)
clear_btn.pack(side="left", padx=7, pady=5)

# Text area
text_area = ctk.CTkTextbox(frame, wrap="word", font=("Arial", 15))
text_area.pack(fill="both", expand=True, padx=10, pady=10)

app.mainloop()
