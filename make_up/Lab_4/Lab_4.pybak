def sepiaTint():
  picture = makePicture(pickAFile())
  greyScaleNew(picture)
  for p in getPixels(picture):
    red = getRed(p)
    blue = getBlue(p)
    if (red < 63):
      red = red*1.1
      blue = blue*0.9
    if (red > 62 and red < 192):
      red = red*1.15
      blue = blue*0.85
    if (red > 191):
      red = red*1.08
      if (red > 255):
        red = 255
      blue = blue*0.93
    
    setBlue(p, blue)
    setRed(p, red)
    
def grayPosterize(pic):
  for p in getPixels(pic):
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    luminance = (r+g+b)/3
    if luminance < 64:
      setColor(p,black)
    else:
      setColor(p,white)