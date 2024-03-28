def blendSounds():
  bass = makeSound("c4.wav")
  aah = makeSound("g4.wav")
  length = getLength(bass)
  halfLength = length/2
  canvas = makeEmptySound(halfLength+length)
  for i in range(0,halfLength):
    aahSample = getSampleValueAt(aah, i+halfLength)
    bassSample = getSampleValueAt(bass, i)
    newSample = 0.5*aahSample + 0.5*bassSample
    setSampleValueAt(canvas, i+halfLength, newSample)
  for i in range(0, halfLength):
    aahSample = getSampleValueAt(aah,i+halfLength)
    bassSample=getSampleValueAt(bass,i)
    newSample = 0.5*aahSample + 0.5*bassSample
    setSampleValueAt(canvas,i+halfLength,newSample)
  for i in range(halfLength,length):
    bassSample = getSampleValueAt(bass,i)
    setSampleValueAt(canvas,i+halfLength,bassSample)
  play(canvas)
  return canvas