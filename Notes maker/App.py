import customtkinter as ctk
from tkinter import filedialog, messagebox
import os


ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")


app = ctk.CTk()
app.title("Notes App")
app.geometry("500x500")

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


def open_settings():
    settings_win = ctk.CTkToplevel(app)
    settings_win.title("Settings ⚙️")
    settings_win.geometry("350x220")
    settings_win.resizable(False, False)

    # Font size option
    ctk.CTkLabel(settings_win, text="🅰 Text Size", font=("Arial", 14, "bold")).pack(pady=(15, 5))
    font_slider = ctk.CTkSlider(settings_win, from_=10, to=30, number_of_steps=20)
    font_slider.set(current_font_size)
    font_slider.pack(padx=20, pady=5)

    def update_font_size(value):
        global current_font_size
        current_font_size = int(value)
        text_area.configure(font=("Arial", current_font_size))
    
    font_slider.configure(command=update_font_size)

    # Theme option
    ctk.CTkLabel(settings_win, text="Theme", font=("Arial", 14, "bold")).pack(pady=(20, 5))
    theme_option = ctk.CTkOptionMenu(
        settings_win, 
        values=["System", "Light", "Dark"], 
        command=lambda mode: ctk.set_appearance_mode(mode)
    )
    theme_option.pack(pady=5)

    # Close button
    ctk.CTkButton(settings_win, text="Close", command=settings_win.destroy).pack(pady=15)

#  Main Frame
frame = ctk.CTkFrame(app, corner_radius=15)
frame.pack(padx=10, pady=10, fill="both", expand=True)

# Button Bar
button_frame = ctk.CTkFrame(frame)
button_frame.pack(fill="x", pady=(5, 10))

# Buttons

new_btn = ctk.CTkButton(button_frame, text="🆕 New", command=new_note, width=100)
open_btn = ctk.CTkButton(button_frame, text="📂 Open", command=open_note, width=100)
save_btn = ctk.CTkButton(button_frame, text="💾 Save", command=save_note, width=100)
clear_btn = ctk.CTkButton(button_frame, text="🧹 Clear", command=clear_note, width=100)
menu_btn = ctk.CTkButton(button_frame, text="☰", width=40, command=open_settings)


new_btn.pack(side="left", padx=5, pady=5)
open_btn.pack(side="left", padx=5, pady=5)
save_btn.pack(side="left", padx=5, pady=5)
clear_btn.pack(side="left", padx=5, pady=5)
menu_btn.pack(side="left", padx=5, pady=5)

# Text area
current_font_size = 14
text_area = ctk.CTkTextbox(frame, wrap="word", font=("Arial", current_font_size))
text_area.pack(fill="both", expand=True, padx=10, pady=10)

app.mainloop()
