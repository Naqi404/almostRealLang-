from SoundLib import *

def main():
  setMediaPath()
  sound = makeSound("mystery.wav")
  blockingPlay(sound)
  mysteryRev = reverse(sound)
  blockingPlay(mysteryRev)
  mirror = makeEmptySound(getLength(mysteryRev))
  copy(mysteryRev, mirror, 0)
  mirrorSound(mirror)
  blockingPlay(mirror)
  merge()

def merge():
  setMediaPath()
  guzdial = makeSound(getMediaPath("guzdial.wav"))
  isSound = makeSound(getMediaPath("is.wav"))
  aSound = makeSound(getMediaPath("a.wav"))
  carSound = makeSound(getMediaPath("car.wav"))
  target = makeSound(getMediaPath("sec3silence.wav"))
  index = 0
  for source in range(0, getLength(guzdial)):
    value = getSampleValueAt(guzdial, source)
    setSampleValueAt(target, index, value)
    index = index + 1
  for source in range(0, int(0.1*getSamplingRate(target))):
    setSampleValueAt(target, index, 0)
    index = index + 1
  for source in range(0, getLength(isSound)):
    value = getSampleValueAt(isSound, source)
    setSampleValueAt(target, index, value)
    index = index + 1
  for source in range(0, int(0.1*getSamplingRate(target))):
    setSampleValueAt(target, index, 0)
    index = index + 1
  for source in range(0, getLength(aSound)):
    value = getSampleValueAt(aSound, source)
    setSampleValueAt(target, index, value)
    index = index + 1
  for source in range(0, int(0.1*getSamplingRate(target))):
    setSampleValueAt(target, index, 0)
    index = index + 1
  for source in range(0, getLength(carSound)):
    value = getSampleValueAt(carSound, source)
    setSampleValueAt(target, index, value)
    index = index + 1
  play(target)
  return target