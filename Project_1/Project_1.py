def main(n):  #n being the parameter determining how many pieces the images will splice into
            #first step: have the users select their image to be used for the program
  img1=pickAFile() 
  pic1 = makePicture(img1)
  show(pic1) #for the sake of showing the selection made by the user, however this does make it messy
  img2=pickAFile()
  pic2 = makePicture(img2)
  show(pic2)
            #get the dimensions from the images selected
  width1 = getWidth(pic1)
  height1 = getHeight(pic1)
  width2 = getWidth(pic2)
  height2 = getHeight(pic2)
            #Having an exit condition, to ensure that the height of the images is the same.
  if height1 != height2:
    print("Please provide images with the same height, the width can be different.")
  else:
            #Set up width and height for new canvas  
    newWidth = (width1+width2)-n  #I can't tell if it is a visual error, or of I'm missing something here. But the small excess space on the right has been annoying me and I dont know how to get rid of it.
    newHeight = height1
    newCanvas = makeEmptyPicture(newWidth, newHeight)      
            #caluclate the width of the each splice for pics 1 and 2
    slicePic1 = width1/n
    slicePic2 = width1/n      
            #the photos will be spliced here to make the accordion effect collage
    for h in range(newHeight):
      x=0
      sx1=0
      sx2=0     
      for i in range(n): #loop for the number of slices
            #Assemble these slices into a new collage in an alternating fashion.    
        for p in range(sx1, sx1+slicePic1-1):
          color = getColor(getPixel(pic1, p, h))
          setColor(getPixel(newCanvas, x, h), color)
          x+=1      
            #incrementing like this is pain
        for p in range(sx2, sx2+slicePic2-1):
          color = getColor(getPixel(pic2, p, h))
          setColor(getPixel(newCanvas, x, h), color)
          x+=1
            #I learned a painful truth here, if I use ctrl+z to undo a sizable number of lines I edited to fix, the code starts merging together for some reason.
        sx1=sx1+slicePic1
        sx2=sx2+slicePic2  
            #Display the resulting collage image on screen. 
    show(newCanvas)