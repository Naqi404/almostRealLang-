def main():
  picturein = makePicture(pickAFile())
  explore(picturein)
  small_picture = makeEmptyPicture((getWidth(picturein)/2),getHeight(picturein)/2)
  big_picture = makeEmptyPicture((getWidth(small_picture)*2),getHeight(small_picture)*2)
  scaleDown(picturein,small_picture)
  explore(small_picture)
  scaleUp(small_picture,big_picture)
  explore(big_picture)
  
def scaleDown(picturein,pictureout):
  sourceX = 0
  for targetX in range(0,getWidth(picturein)/2):
    sourceY = 0
    for targetY in range(0,getHeight(picturein)/2):
      color = getColor(getPixel(picturein,sourceX,sourceY))
      setColor(getPixel(pictureout,targetX,targetY), color)
      sourceY = sourceY + 2
    sourceX = sourceX + 2
def scaleUp(picturein,pictureout):
  sourceX = 0
  for targetX in range(0,getWidth(picturein)*2):
    sourceY = 0
    for targetY in range(0,getHeight(picturein)*2):
      srcpx = getPixel(picturein,int(sourceX),int(sourceY))    
      color = getColor(srcpx)
      setColor(getPixel(pictureout,targetX,targetY), color)
      sourceY = sourceY + 0.5
    sourceX = sourceX + 0.5
  
  