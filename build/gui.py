
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\sergi\PycharmProjects\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("700x700")
window.configure(bg = "#232323")


canvas = Canvas(
    window,
    bg = "#232323",
    height = 700,
    width = 700,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    50.0,
    50.0,
    650.0,
    250.0,
    fill="#353535",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat",
    background="#353535",
    activebackground="#353535"
)
button_1.place(
    x=91.0,
    y=198.0,
    width=25.0,
    height=25.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat",
    background="#353535",
    activebackground="#353535"
)
button_2.place(
    x=604.0,
    y=68.0,
    width=27.0,
    height=27.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    358.5,
    145.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#353535",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=123.0,
    y=68.0,
    width=471.0,
    height=153.0
)

canvas.create_text(
    135.0,
    82.0,
    anchor="nw",
    text="Texto Aquí",
    fill="#818181",
    font=("Beiruti Regular", 16 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    140.0,
    379.0,
    image=image_image_1
)
window.resizable(False, False)
window.mainloop()
