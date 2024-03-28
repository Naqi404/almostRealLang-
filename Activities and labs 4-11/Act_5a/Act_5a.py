def main():
  picture = makePicture(pickAFile())
  edgeDetect(picture, 5)

def luminance(pixel):
  r = getRed(pixel)
  g = getGreen(pixel)
  b = getBlue(pixel)
  return (r+g+b)/3  

def edgeDetect(picture,threshold):
  color=pickAColor()
  color2=pickAColor()
  color3=pickAColor()
  color4=pickAColor()
  for px in getPixels(picture):
    x = getX(px)
    y = getY(px)
    if y < getHeight(picture)-1 and x< getWidth(picture)-1:
      botrt = getPixel(picture, x+1,y+1)
      thislum = luminance(px)
      brlum = luminance(botrt)
      if abs(brlum-thislum)>threshold:
        setColor(px,color)
      if abs(brlum-thislum) <=  threshold:
        setColor(px,color2)
  show(picture)
  bottom = getHeight(picture)
  for px in getPixels(picture):
    y = getY(px)
    if y < threshold:
      setColor(px,color3)
    if y > bottom:
      setColor(px,color4)
  repaint(picture)