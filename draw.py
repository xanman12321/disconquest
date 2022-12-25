from PIL import Image
import colors as c

def convert(m):
    out = [[]]
    y = 0
    for i in m:
        if i == "\n":
            y += 1
            out.append([])
        else:
            out[y].append(c.colors[i])
    return out

def drawr(x,settings):
    err = False
    tlen = len(x[0])
    for i in x:
        if len(i) != tlen:
            err = "Non-rectangular image"
            #if len(i) < tlen:
    width = tlen
    height = len(x)
    p = settings["size"]
    bg = Image.new("RGBA", (width*p, height*p), (0, 0, 0))
    if err:
        return err
    else:
        xpos = 0
        ypos = 0
        for i in x:
            for col in i:
                if len(col) < 4:
                    col = col + (255,)
                pix = Image.new("RGBA", (p, p), col)
                bg.paste(pix, (xpos, ypos))
                xpos += p
            xpos = 0
            ypos += p
        return bg