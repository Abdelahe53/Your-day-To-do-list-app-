
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\GondalF\Desktop\coding files\Python file\app\gui\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1255x716")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 716,
    width = 1255,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    937.0550537109375,
    199.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    315.0550537109375,
    199.0,
    image=image_image_2
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=56.0,
    y=362.0723876953125,
    width=97.66873168945312,
    height=88.9276123046875
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    627.0,
    52.0,
    image=image_image_3
)

canvas.create_text(
    84.0550537109375,
    152.0,
    anchor="nw",
    text="Tasks done",
    fill="#000000",
    font=("Inter", 32 * -1)
)

canvas.create_text(
    56.0550537109375,
    310.0,
    anchor="nw",
    text="Tasks",
    fill="#000000",
    font=("Inter SemiBold", 32 * -1)
)

canvas.create_text(
    110.0550537109375,
    199.0,
    anchor="nw",
    text="3",
    fill="#000000",
    font=("Inter", 36 * -1)
)

canvas.create_text(
    717.0550537109375,
    152.0,
    anchor="nw",
    text="Daily tasks",
    fill="#000000",
    font=("Inter", 32 * -1)
)

canvas.create_text(
    741.0550537109375,
    199.0,
    anchor="nw",
    text="5",
    fill="#000000",
    font=("Inter", 36 * -1)
)

canvas.create_text(
    487.0,
    33.0,
    anchor="nw",
    text="YOUR DAY",
    fill="#FFFFFF",
    font=("Inter Bold", 36 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    50.0,
    52.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    1205.0,
    52.0,
    image=image_image_5
)
window.resizable(False, False)
window.mainloop()