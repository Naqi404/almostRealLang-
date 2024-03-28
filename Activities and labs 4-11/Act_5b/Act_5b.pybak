def main():
  src = makePicture(pickAFile())
  bg = makePicture(pickAFile())
  #chromakeyBlue(src, bg)
  #chromakeyGreen(src, bg)
  chromakeyYellow(src, bg)
  grayPosterize(src)
  show(src)
  
def chromakeyBlue(source,bg):
  for px in getPixels(source):
    x = getX(px)
    y = getY(px)
    if (getRed(px) + getGreen(px) < getBlue(px)):
      bgpx = getPixel(bg,x,y)
      bgcol = getColor(bgpx)
      setColor(px,bgcol)

def chromakeyGreen(source,bg):
  for px in getPixels(source):
    x = getX(px)
    y = getY(px)
    if (getRed(px) + getBlue(px) < getGreen(px)):
      bgpx = getPixel(bg,x,y)
      bgcol = getColor(bgpx)
      setColor(px,bgcol)

def chromakeyYellow(source,bg):
  for p in getPixels(source):
      if getRed(p) > (getGreen(p) + getBlue(p)):
        setColor(p,getColor(getPixel(bg,getX(p),getY(p))))
        

def grayPosterize(pic):
  for p in getPixels(pic):
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    luminance = (r+g+b)/3
    if luminance < 50:
      setColor(p,black)
    elif luminance >= 50 >= 165:
      setColor(p,white)
    else:
      setColor(p, white)