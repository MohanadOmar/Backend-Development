from PIL import Image, ImageDraw, ImageFont

# get an image
with Image.open("images/test5.jpg").convert("RGBA") as base:

    # make a blank image for the text, initialized to transparent text color
    txt = Image.new("RGBA", base.size, (255, 255, 255, 0))

    # get a font
    fnt = ImageFont.truetype("arial", 200)
    # get a drawing context
    d = ImageDraw.Draw(txt)

    # draw text, half opacity
    d.text((150, 150), "Hello", font=fnt, fill=(255, 255, 255, 128))

    out = Image.alpha_composite(base, txt)

    out.show()