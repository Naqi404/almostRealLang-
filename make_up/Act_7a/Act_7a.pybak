def main():
  setMediaPath()
  sound = makeSound(getMediaPath("paganini.wav"))
  explore(sound)
  blockingPlay(sound)
  soundInfo(sound)  
  decreaseVolume(sound)
  increaseVolume(sound)
  blockingPlay(sound)
  explore(sound)
  soundInfo(sound)
  maxSamples(sound)
  
  
def decreaseVolume(sound):
  samples= getSamples(sound)
  for index in range(0, getLength(sound)/2):
    value = getSampleValue(samples[index])
    value = value* 0.25
    setSampleValue(samples[index], value)
    
def increaseVolume(sound):
  samples= getSamples(sound)
  for index in range(getLength(sound)/2, getLength(sound)):
    value = getSampleValue(samples[index])
    value = value*4
    setSampleValue(samples[index], value)
    
def maxSamples(sound):
  for sample in getSamples(sound):
    if sample >= 0:
      setSampleValue(sample, 32767)
    else:
      setSampleValue(sample, -32768)
  

def soundInfo(sound):
  length = getLength(sound)
  rate = getSamplingRate(sound)
  duration = getDuration(sound)
  maxValue = 0
  minValue = 0
  for s in getSamples(sound):
    value = getSampleValue(s)
    if value > maxValue:
      maxValue = value
    if value < minValue:
      minValue = value
  print "number of samples:" , length
  print "sample rate:", rate
  print "duration is:", duration
  print "max amplitude is:" , maxValue
  print "max aplitude is:" , minValue
  
  
  