#Naqi Nadeem

def collage():
  setMediaPath()
  canvas = makeEmptyPicture(736, 1000)
  pic = getMediaPath("pic.jpg")
  picBL = makePicture(pic)
  picBR = makePicture(pic)
  picTR = makePicture(pic)
  picML = makePicture(pic)
  picMR = makePicture(pic)
  picTL = makePicture(pic)
  grayscale(picTR)
  negative(picTL)  
  negative(picMR)
  negative(picBL)
  cyanHue(picML)
  setup(picTL, picBL, picBR, picTR, picML, picMR, canvas)


def cyanHue(picML): #altered version of the cyano program we made earlier in the semester, messed with the numbers and got a nice blue-ish tinge to the image
  for px in getPixels(picML):
    intensity = (getRed(px)+getGreen(px)+getBlue(px))/3 
    setColor(px, makeColor(intensity, intensity, intensity))
  for p in getPixels(picML):
    red = getRed(p) *1
    green = getGreen(p) * 1.8
    blue = getBlue(p) *0.9
    if(blue<63):
      blue = blue*1.4
    if(blue > 62 and blue < 191):
      blue = blue*1.4
    if (blue > 191):
      blue = blue*1.2
    if (blue > 255):
      blue = 255
    setBlue(p, blue)
    setRed(p, red)
    setGreen(p, green)
  #repaint(picML)
  
def luminance(pixel):
  r = getRed(pixel)
  g = getGreen(pixel)
  b = getBlue(pixel)
  return (r+g+b)/3

def grayscale(picTR):  #simple grayscale program, placed at the top right segment
  for p in getPixels(picTR):
    intensity = (getRed(p)+getGreen(p)+getBlue(p))/3
    setColor(p, makeColor(intensity, intensity, intensity))
  #repaint(picTR)
    
def negative(picMR): #one of the main filters being used, in three alternate spots to create contrast from opposing image segments. Also the black sun looks very cool.
  for px in getPixels(picMR):
    red=getRed(px)
    green=getGreen(px)
    blue=getBlue(px)
    negColor=makeColor(255-red, 255-green, 255-blue)
    setColor(px,negColor)
  #repaint(picMR)

def negative(picBL):
  for px in getPixels(picBL):
    red=getRed(px)
    green=getGreen(px)
    blue=getBlue(px)
    negColor=makeColor(255-red, 255-green, 255-blue)
    setColor(px,negColor)
  #repaint(picBL)

def negative(picTL):
  for px in getPixels(picTL):
    red=getRed(px)
    green=getGreen(px)
    blue=getBlue(px)
    negColor=makeColor(255-red, 255-green, 255-blue)
    setColor(px,negColor)
  #repaint(picTL)
      
def setup(picTL, picBL, picBR, picTR, picML, picMR,canvas):
#Top left of the image
  for x in range(0,368):
    for y in range(0, 333):
      sourcePX = getPixel(picTL, x, y)
      color = getColor(sourcePX)
      tarPX = (getPixel(canvas, x, y))
      setColor(tarPX, color)

#Bottom right segment done
  for x in range(369,736):
    for y in range(668,1000):
      sourcePX = getPixel(picBR, x, y)
      color = getColor(sourcePX)
      tarPX = (getPixel(canvas, x, y))
      setColor(tarPX, color)
#Top right segment done
  for x in range(369, 736):
    for y in range(0, 333):
      sourcePX = getPixel(picTR, x, y)
      color = getColor(sourcePX)
      tarPX = (getPixel(canvas, x,y))
      setColor(tarPX, color)
#Middle left segment done
  for x in range(0, 367):
    for y in range(334, 667):
      sourcePX = getPixel(picML, x, y)
      color = getColor(sourcePX)
      tarPX = (getPixel(canvas,x,y))
      setColor(tarPX, color)
#Middle right segment done
  for x in range(369, 736):
    for y in range(334, 667):
      sourcePX = getPixel(picMR, x, y)
      color = getColor(sourcePX)
      tarPX = (getPixel(canvas,x,y))
      setColor(tarPX, color)
#Bottom left segment done
  for x in range(0, 368):
    for y in range(668,1000):
      sourcePX = getPixel(picBL, x, y)
      color = getColor(sourcePX)
      tarPX = (getPixel(canvas,x,y))
      setColor(tarPX, color)
  repaint(canvas)