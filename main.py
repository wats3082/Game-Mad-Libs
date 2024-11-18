import tkinter as tk
from tkinter import simpledialog
import random

def generate_haiku(color, weapon, theme):
    """Generates a haiku based on user inputs."""
    haikus = [
        f"{color} fades to dusk,\nOur {weapon} strikes without pause—\n{theme}.",
        f"Shadows close around,\nA {weapon} gleams with sorrow's weight—\n{color} whispers 'farewell'.",
        f"{color} spills like ink,\nA {weapon} cuts, sharp with regret—\nThe void calls softly.",
        f"Crimson paints the sky,\nA {weapon} slashes through the air—\n{theme} looms ever still.",
    ]
    return random.choice(haikus)

def copy_to_clipboard(text):
    """Copies the given text to the clipboard."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()  # Ensure it updates
    root.destroy()

def display_haiku(haiku, restart_callback):
    """Creates a window to display the haiku and provide options to copy, restart, or exit."""

    def on_copy():
        copy_to_clipboard(haiku)
        message_label.config(text="Copied to clipboard!")

    def on_try_again():
        window.destroy()
        restart_callback()

    def on_exit():
        quit()
        window.destroy()

    # Create the main window
    window = tk.Tk()
    window.title("Virion Haiku")

    # Set a timeout to close the window automatically after 30 seconds
    window.after(30000, window.destroy)

    # Create a text area to display the haiku
    text_area = tk.Text(window, wrap="word", font=("Helvetica", 14), bg="#f4f4f4", fg="#333")
    text_area.insert("1.0", haiku)
    text_area.config(state="disabled")
    text_area.pack(padx=20, pady=20)

    # Add a button to copy the haiku
    copy_button = tk.Button(window, text="Copy to Clipboard", command=on_copy)
    copy_button.pack(pady=5)

    # Add a "Try Again" button
    try_again_button = tk.Button(window, text="Try Again", command=on_try_again)
    try_again_button.pack(pady=5)

    # Add an "Exit" button
    exit_button = tk.Button(window, text="Exit", command=on_exit)
    exit_button.pack(pady=5)

    # Message label for feedback
    message_label = tk.Label(window, text="", font=("Helvetica", 10), fg="green")
    message_label.pack()

    window.mainloop()

def main():
    """Runs the main haiku generation program."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Get user inputs

    root.geometry("750x250+400+300")

    color = simpledialog.askstring("Input", "Enter a color:")
    if not color: return
    weapon = simpledialog.askstring("Input", "Enter a weapon:")
    if not weapon: return
    theme = simpledialog.askstring("Input", "Enter a theme or feeling (e.g., death, hope, sorrow):")
    if not theme: return

    # Generate a haiku
    haiku = generate_haiku(color, weapon, theme)

    # Display the haiku in a window
    display_haiku(haiku, main)
    time.sleep(5) 
if __name__ == "__main__":
    main()
