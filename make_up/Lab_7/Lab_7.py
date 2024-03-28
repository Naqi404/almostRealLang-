def main():
  setMediaPath()
  sound = makeSound("yesterday.wav")  
  adjustmentFactor = 2
  soundLow = makeEmptySound(getLength(sound)*adjustmentFactor)
  soundHigh = makeEmptySound(getLength(soundLow)/adjustmentFactor)
  explore(sound)
  pitch(0.5, sound, soundLow)
  explore(soundLow)
  pitch(1.75, soundLow, soundHigh)
  explore(soundHigh)
  normalize(soundHigh)
  explore(soundHigh)
  
def pitch(adjuster, soundIn, soundOut):
  soundIndex = 0
  for i in range(0, getLength(soundOut)):
    value = getSampleValueAt(soundIn, int(soundIndex))
    setSampleValueAt(soundOut, i, value)
    soundIndex = soundIndex + adjuster
  return soundOut

def normalize(sound):
  largest = 0
  for s in getSamples(sound):
    largest = max(largest,abs(getSampleValue(s)))
    multiplier = 32767.0 / largest
  for s in getSamples(sound):
    louder = multiplier * getSampleValue(s)
    setSampleValue(s,louder)
    