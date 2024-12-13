import tkinter as tk
from tkinter import filedialog, messagebox
import converter

def select_file():
    """Open file selection dialog."""
    return filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])

def select_save_location(extension=".bin"):
    """Open save file dialog."""
    return filedialog.asksaveasfilename(defaultextension=extension)

def convert_image():
    """Convert image to text or binary."""
    input_path = select_file()
    if not input_path:
        return
    output_path = select_save_location(".bin" if messagebox.askyesno("Binary?", "Store in binary format?") else ".txt")
    if not output_path:
        return
    binary = output_path.endswith('.bin')
    converter.image_to_text(input_path, output_path, binary)
    messagebox.showinfo("Success", "Image successfully converted!")

def restore_image():
    """Restore image from text or binary."""
    input_path = select_file()
    if not input_path:
        return
    output_path = select_save_location(".png")
    if not output_path:
        return
    binary = input_path.endswith('.bin')
    converter.text_to_image(input_path, output_path, binary, output_format='png')
    messagebox.showinfo("Success", "Image successfully restored!")

# GUI Setup
root = tk.Tk()
root.title("Image Converter")
root.geometry("400x200")

frame = tk.Frame(root)
frame.pack(pady=20)

btn_convert = tk.Button(frame, text="Convert Image to Text/Binary", command=convert_image, width=30)
btn_convert.pack(pady=10)

btn_restore = tk.Button(frame, text="Restore Image from Text/Binary", command=restore_image, width=30)
btn_restore.pack(pady=10)

root.mainloop()

