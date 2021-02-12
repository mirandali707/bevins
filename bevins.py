import sys
import tkinter

from PIL import Image, ImageTk
FACE_FILEPATH = 'img/bevins_smol.jpg'


def main():
    root = tkinter.Tk()
    root.title("roger bevins iii")

    global background_image
    background_image = Image.open(FACE_FILEPATH)

    # make canvas with image
    canvas = tkinter.Canvas(root, width=background_image.size[0], height=background_image.size[1], name='canvas', borderwidth=0, highlightthickness=0)
    canvas.pack()
    root.resizable(False, False)

    tk_image = ImageTk.PhotoImage(background_image)
    global canvas_image
    canvas_image = canvas.create_image(0, 0, anchor='nw', image=tk_image)

    root.mainloop()


if __name__ == '__main__':
    main()
