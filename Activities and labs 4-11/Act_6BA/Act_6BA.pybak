def main():
  source = makePicture(pickAFile())
  target = makePicture(pickAFile())
  merger(source, target)
  show(target)
  
def merger(source, target):
  for startP in range(2):
    for x in range(startP, getWidth(source), 2):
      for y in range(startP, getHeight(source), 2):
        sourcePix= getPixel(source, x, y)
        targetPix = getPixel(target, x, y)
        setColor(targetPix, getColor(sourcePix))
