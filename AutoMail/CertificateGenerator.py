from PIL import Image, ImageDraw, ImageFont


names = open("Names.txt")

while 1:
    n = names.readline()
    if not n:
        break
    else:
        msg = n.rstrip('\n')
        ifile = Image.open('Excel.png')
        font_type = ImageFont.truetype('arial.ttf',340)
        draw = ImageDraw.Draw(ifile)
        w,h = draw.textsize(msg, font = font_type)
        draw.text(xy = ((5796-w)/2,1720-80), text = msg ,fill = (0,0,0),font = font_type)
        #sname = 'S1\\'+msg+".png"
        sname = msg+".png"
        ifile.save(sname)
        ifile.close()

