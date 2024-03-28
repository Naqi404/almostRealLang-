def getQuarters():
  source = makePicture(pickAFile())
  canvas = makeEmptyPicture(getWidth(source),getHeight(source)) 
  w = getWidth(source)
  h = getHeight(source)
  #segment 1
  sX1 = 0  
  for tarX in range(0, 234):
    sY1 = 155  
    for tarY in range(0, 155):
      color = getColor(getPixel(source, sX1, sY1))
      setColor(getPixel(canvas, tarX, tarY), color)
      sY1 = sY1 + 1
    sX1 = sX1 + 1
    
  #Segment 2
  sX2 = 0
  for tarX in range(234, 468):
    sY2 = 0
    for tarY in range(0, 155):
      color = getColor(getPixel(source, sX2, sY2))
      setColor(getPixel(canvas, tarX, tarY), color)
      sY2 = sY2 + 1
    sX2 = sX2 + 1
    
  #Segment 3
  sX3 = 234
  for tarX in range(0, 234):
    sY3 = 155
    for tarY in range(155, 310):
      color = getColor(getPixel(source, sX3, sY3))
      setColor(getPixel(canvas, tarX, tarY), color)
      sY3 = sY3 + 1
    sX3 = sY3 + 1
    
  #Segment 4
  sX4 = 234
  for tarX in range(234, 468):
    sY4 = 0
    for tarY in range(155, 310):
      color = getColor(getPixel(source, sX4, sY4))
      setColor(getPixel(canvas, tarX, tarY), color)
      sY4 = sY4 + 1
    sX4 = sY4 + 1
  repaint(canvas)