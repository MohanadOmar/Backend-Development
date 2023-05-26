import os
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk, ImageDraw, ImageFont

win = tk.Tk()
win.config(bg="Grey")
win.title("Watermarking")


# Design
img_canvas = tk.Canvas(win, width=300, height=205, bg="grey")
img_canvas.create_text(150, 102, text="Upload Image")
img_canvas.grid(column=0, row=0, columnspan=2)

upload_button = tk.Button(win, text='Upload Img', width=20, command=lambda: upload_img())
upload_button.grid(row=1, column=0)

download_button = tk.Button(win, text='Download Img', width=20, command=lambda: download_img())
download_button.grid(row=1, column=1)


def upload_img():
    global img, f_types, filename
    f_types = [('Jpg Files', '*.jpg')]
    filename = filedialog.askopenfilename(filetypes=f_types)
    img = ImageTk.PhotoImage(Image.open(filename).resize((300, 205)))
    label = tk.Label(win, image=img)
    label.grid(row=0, column=0, columnspan=2)


def download_img():
    with Image.open(filename).convert("RGBA") as base:
        # make a blank image for the text, initialized to transparent text color
        txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

        # get a font
        fnt = ImageFont.truetype("arial", 300)
        # get a drawing context
        d = ImageDraw.Draw(txt)

        # text watermark
        watermark_label = tk.Label(win, text="Watermark-Text")
        watermark_label.grid(row=2, column=0)
        watermark_entry = tk.Entry(win, width=25, bg="white")
        watermark_entry.grid(row=2, column=1)

        file_label = tk.Label(win, text="File-Name")
        file_label.grid(row=3, column=0)
        file_entry = tk.Entry(win, width=25, bg="white")
        file_entry.grid(row=3, column=1)

        submit_button = tk.Button(win, text="Download", width=10, command=lambda: submit())
        submit_button.grid(row=4, column=0, columnspan=2)

        def submit():
            # draw text, half opacity
            d.text((10, 10), watermark_entry.get(), font=fnt, fill=(255, 255, 255, 128))

            out = Image.alpha_composite(base, txt).convert("RGB")

            save_path = "F:\Portfolio Projects\Image Watermarking Desktop App [GUI]\images"
            file_name = file_entry.get()
            complete_name = os.path.join(save_path, file_name)
            out.save(complete_name)


win.mainloop()