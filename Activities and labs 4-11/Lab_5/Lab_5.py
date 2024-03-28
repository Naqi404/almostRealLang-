def main():
  picture = makePicture(pickAFile())
  h = getHeight(picture)
  width = getWidth(picture)/5
  pic = makeEmptyPicture((width*9), h, black)
  coloredBar(picture, pic, 0, width)
  coloredBar(picture, pic, width, width*2)
  coloredBar(picture, pic, width*2, width*3)
  coloredBar(picture, pic, width*3, width*4)
  coloredBar(picture, pic, width*4, width*5)
  show(pic)
  
def coloredBar(picture, pic, startx, endx):
  h = getHeight(picture)
  w1 = startx*2
  for x in range(startx, endx):
    for y in range (0,h):
      px = getPixel(picture, x, y)
      npx = getPixel(pic, w1, y)
      color = getColor(px)
      setColor(npx, color)
    w1 = w1+1
  
main()