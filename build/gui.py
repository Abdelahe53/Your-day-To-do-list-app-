
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\GondalF\Desktop\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("800x780")
window.configure(bg = "#090909")


canvas = Canvas(
    window,
    bg = "#090909",
    height = 780,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    655.0,
    199.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    151.0,
    199.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    400.0,
    52.0,
    image=image_image_3
)

canvas.create_text(
    66.0,
    152.0,
    anchor="nw",
    text="Tasks done",
    fill="#000000",
    font=("Inter", 32 * -1)
)

canvas.create_text(
    140.0,
    199.0,
    anchor="nw",
    text="3",
    fill="#000000",
    font=("Inter", 36 * -1)
)

canvas.create_text(
    574.0,
    152.0,
    anchor="nw",
    text="Daily tasks",
    fill="#000000",
    font=("Inter", 32 * -1)
)

canvas.create_text(
    645.0,
    199.0,
    anchor="nw",
    text="5",
    fill="#000000",
    font=("Inter", 36 * -1)
)

canvas.create_text(
    260.0,
    32.0,
    anchor="nw",
    text="YOUR DAY",
    fill="#090909",
    font=("Inter Bold", 36 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    51.0,
    51.0,
    image=image_image_4
)

canvas.create_rectangle(
    169.0,
    465.0,
    755.0,
    752.0,
    fill="#090909",
    outline="")

canvas.create_rectangle(
    169.0,
    403.0,
    755.0,
    454.0,
    fill="#090909",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    462.0,
    428.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=182.0,
    y=406.0,
    width=560.0,
    height=43.0
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    748.0,
    52.0,
    image=image_image_5
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    462.0,
    608.5,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=182.0,
    y=469.0,
    width=560.0,
    height=277.0
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
    x=36.0,
    y=406.0,
    width=115.0,
    height=45.0
)

canvas.create_text(
    42.0,
    413.0,
    anchor="nw",
    text="Add task",
    fill="#000000",
    font=("Inter", 24 * -1)
)
window.resizable(False, False)
window.mainloop()
