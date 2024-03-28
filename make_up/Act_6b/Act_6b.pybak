def main():
  picture = makePicture(pickAFile())
  h = getHeight(picture)
  width = getWidth(picture)/5
  adjust = 6
  t1=getWidth(picture)
  t2 = (t1/adjust)
  pic = makeEmptyPicture((t1/adjust)*(adjust*2), h, black)
  for i in range(0, adjust):
    coloredBar(picture, pic, t2*i, t2 *(i+1))
  show(pic)
  
def coloredBar(picture, pic, startx, endx):
  h = getHeight(picture)
  z = startx*2
  for x in range(startx, endx):
    for y in range (0,h):
      px = getPixel(picture, x, y)
      npx = getPixel(pic, z, y)
      color = getColor(px)
      setColor(npx, color)
    z = z+1
  
main()