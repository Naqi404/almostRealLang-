#Program created by Naqi Nadeem
from SoundLib import *
def soundCollage():
  sound = makeSound("paganini.wav") #This is Paganini Caprice Op. 1: number 24 in A minor. This in particular is the opening sequence
  #explore (sound)                   #The sound was available as a royalty free download from the University of Leicester website
  slice1 = clip(sound, 0, 170000)
  slice2 = clip(sound, 170000, 340000)
  slice3 = clip(sound, 340000, 510000) #This sounds like it stops and then starts back up after someone hit rewind on the tape 
  slice4 = clip(sound,510000, 680000) #adding the reverb/vibrato to 4 and 5 was very nice, I can feel the vibration
  slice5 = clip(sound,680000, 851744) 
  reverse(slice2)
  mirrorSound(slice3)
  vibrato(slice4)
  vibrato(slice5)
  decreaseVolume(slice5)
  newSound = splice(slice1,slice2,slice3,slice4,slice5)
  normalize(newSound)
  explore(newSound)
  print (str(getDuration(newSound))+' seconds')

def splice(slice1,slice2,slice3,slice4,slice5):
  len = getLength(slice1) + getLength(slice2) + getLength(slice3) + getLength(slice4) + getLength(slice5)
  newSound = makeEmptySound(len)      
  copy(slice1, newSound, 0)
  copy(slice2, newSound, getLength(slice1))
  copy(slice3, newSound, getLength(slice1) + getLength(slice2))
  copy(slice4, newSound, getLength(slice1) + getLength(slice2) + getLength(slice3))
  copy(slice5, newSound, getLength(slice1) + getLength(slice2) + getLength(slice3) + getLength(slice4))
  return newSound

def reverse(source):
  target = makeEmptySound(getLength(source))
  sourceIndex = getLength(source) - 1 # start at end
  for targetIndex in range(0, getLength(target)):
    value = getSampleValueAt(source, sourceIndex)
    setSampleValueAt(target, targetIndex, value)
    sourceIndex = sourceIndex - 1 # moving backwards
  return target

def mirrorSound(sound):
  len = getLength(sound)
  mirrorpoint = len/2
  for index in range(0, mirrorpoint):
    left = getSampleObjectAt(sound, index)
    right = getSampleObjectAt(sound, len-index-1)
    value = getSampleValue(left)
    setSampleValue(right, value)
  return sound
  
def normalize(sound):
  largest = 0
  for s in getSamples(sound):
    largest = max(largest,abs(getSampleValue(s)))
    multiplier = 32767.0 / largest
  for s in getSamples(sound):
    louder = multiplier * getSampleValue(s)
    setSampleValue(s,louder)

def vibrato(source):
  delay = 800 #Nicola Paganini was known for his vibrato, the intention was to add some synthetic vibrato, but it sounds more like a reverb which is actually an unexpected positive
  s2 = duplicateSound(source)
  for index in range(delay, getLength(source)):
    echoSample = 0.6*getSampleValueAt(s2, index-delay)
    comboSample = getSampleValueAt(source,index) + echoSample
    setSampleValueAt(source, index,comboSample)
  return source

def decreaseVolume(sound):
  samples = getSamples(sound)
  length = getLength(sound)
  for index in range(length/2, length):
    value = getSampleValue(samples[index])
    value = value* 0.69
    setSampleValue(samples[index], value)