def main(scaleFactor):
  setMediaPath()
  picture = makePicture(getMediaPath("JPG Images/beach.jpg"))
  smallPicture = makeEmptyPicture(getWidth(picture)/scaleFactor,getHeight(picture)/scaleFactor)
  bigPicture = makeEmptyPicture(getWidth(smallPicture)*scaleFactor,getHeight(smallPicture)*scaleFactor)
  explore(picture)
  scale(scaleFactor,picture,smallPicture)
  explore(smallPicture)
  scale(1.0/scaleFactor,smallPicture,bigPicture)
  explore(bigPicture)
  blurredBigPicture = blur(bigPicture)
  canvas = makeEmptyPicture(getWidth(blurredBigPicture),getHeight(blurredBigPicture))
  explore(blurredBigPicture)
  scale(8.0/10.0,blurredBigPicture, canvas)
  copy(canvas,blurredBigPicture)
  explore(blurredBigPicture)

def scale(scaleFactor,pictureIn,pictureOut):
   sourceX = 0
   for targetX in range(0,getWidth(pictureOut)):
     sourceY = 0
     for targetY in range(0,getHeight(pictureOut)):
       color = getColor(getPixel(pictureIn,int(sourceX),int(sourceY)))
       setColor(getPixel(pictureOut,targetX,targetY), color)
       sourceY = sourceY + scaleFactor
     sourceX = sourceX + scaleFactor

def blur(pictureIn):
  blurredPicture = duplicatePicture(pictureIn)
  for x in range(1, getWidth(pictureIn)-1):
    for y in range(1, getHeight(pictureIn)-1):
      top = getPixel(pictureIn,x,y-1)
      left = getPixel(pictureIn,x-1,y)
      bottom = getPixel(pictureIn,x,y+1)
      right = getPixel(pictureIn,x+1,y)
      center = getPixel(blurredPicture,x,y)
      newRed=(getRed(top)+ getRed(left) + getRed(bottom) + getRed(right) + getRed(center))/5
      newGreen=(getGreen(top) + getGreen(left) + getGreen(bottom)+ getGreen(right)+getGreen(center))/5
      newBlue=(getBlue(top) + getBlue(left) + getBlue(bottom) + getBlue(right)+ getBlue(center))/5
      setColor(center, makeColor(newRed, newGreen, newBlue))
  return blurredPicture

def copy(pictureIn,pictureOut):
  width = getWidth(pictureIn)
  height = getHeight(pictureIn)
  targetX = int(width*0.1)
  for sourceX in range(int(width*0.1),int(width*0.9)):
    targetY = int(height*0.1)
    for sourceY in range(int(height*0.1),int(height *0.9)):
      color = getColor(getPixel(pictureIn,sourceX,sourceY))
      setColor(getPixel(pictureOut,targetX,targetY),color)
      targetY = targetY + 1
    targetX = targetX + 1
    