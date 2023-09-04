from PIL import Image, ImageTk
from tkinter import Tk, Label


def show_image(image: Image) -> None:
    """
    A function for viewing an image in a Tkinter window.
    """
    root = Tk()
    root.title("Screenshot")
    photo = ImageTk.PhotoImage(image)
    label = Label(image=photo)
    label.pack()
    root.mainloop()
