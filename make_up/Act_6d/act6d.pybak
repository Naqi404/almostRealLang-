def main():
  picture = makePicture(pickAFile())
  scaleFactor = 4
  smallPicture = makeEmptyPicture(getWidth(picture)/scaleFactor,getHeight(picture)/scaleFactor)
  bigPicture = makeEmptyPicture(getWidth(smallPicture)*scaleFactor,getHeight(smallPicture)*scaleFactor)
  explore(picture)
  scale(scaleFactor,picture,smallPicture)
  explore(smallPicture)
  scale(1.0/scaleFactor,smallPicture,bigPicture)
  explore(bigPicture)

def scale(scaleFactor,pictureIn,pictureOut):
   sourceX = 0
   for targetX in range(0,getWidth(pictureOut)):
     sourceY = 0
     for targetY in range(0,getHeight(pictureOut)):
       color = getColor(getPixel(pictureIn,int(sourceX),int(sourceY)))
       setColor(getPixel(pictureOut,targetX,targetY), color)
       sourceY = sourceY + scaleFactor
     sourceX = sourceX + scaleFactor
  