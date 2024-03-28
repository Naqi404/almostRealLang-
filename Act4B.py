def main():
  pic = makePicture(pickAFile())
  changeColor(pic)
  squareOutline(pic)
  explore(pic)
  
def changeColor(pic):
  px = getPixels(pic)
  color=pickAColor()
  for i in px:
    setColor(i, color)

def squareOutline(picture):
  color2 = pickAColor()
  pixels=getPixels(picture)
  width=getWidth(picture)
  for p in pixels:
    setColor(pixels[0], color2)
    setColor(pixels[1], color2)
    setColor(pixels[2], color2)
    setColor(pixels[3], color2)
    setColor(pixels[4], color2)
    setColor(pixels[5], color2)
    setColor(pixels[width], color2)
    setColor(pixels[width+5], color2)
    setColor(pixels[width*2], color2)
    setColor(pixels[(width*2)+5], color2)
    setColor(pixels[width*3], color2)
    setColor(pixels[(width*3)+5], color2)
    setColor(pixels[width*4], color2)
    setColor(pixels[(width*4)+5], color2)
    setColor(pixels[width*5], color2)
    setColor(pixels[(width*5)+1], color2)
    setColor(pixels[(width*5)+2], color2)
    setColor(pixels[(width*5)+3], color2)
    setColor(pixels[(width*5)+4], color2)
    setColor(pixels[(width*5)+5], color2)
  repaint(picture)   