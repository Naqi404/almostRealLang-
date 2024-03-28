from media import *

# This file has definitions for the following functions:
#	clip(source, start, end)
#	copy(source, target, start)
#	reverse(source)
#	mirrorSound(sound)


def clip(source, start, end):
  # Written by: Guzdial & Ericson E4 - program # 105
  target = makeEmptySound(end - start,int(getSamplingRate(source)))
  targetIndex = 0
  for sourceIndex in range(start, end):
    sourceValue = getSampleValueAt(source, sourceIndex)
    setSampleValueAt(target, targetIndex, sourceValue)
    targetIndex = targetIndex + 1
  return target


def copy(source, target, start):
  #Written by: Guzdial & Ericson E4 - program # 106
  targetIndex = start
  for sourceIndex in range(0, getLength(source)):
    sourceValue = getSampleValueAt(source, sourceIndex)
    setSampleValueAt(target, targetIndex, sourceValue)
    targetIndex = targetIndex + 1


def reverse(source):
  #Written by Guzdial & Ericson E4 - program # 108
  target = makeEmptySound(getLength(source) - 1,int(getSamplingRate(source)))
  sourceIndex = getLength(source) - 1
  for targetIndex in range(0, getLength(target)):
    sourceValue = getSampleValueAt(source, sourceIndex)
    setSampleValueAt(target, targetIndex, sourceValue)
    sourceIndex = sourceIndex - 1
  return target


def mirrorSound(sound):
  #Written by: Guzdial & Ericson E4 - program # 109
  len = getLength(sound)
  mirrorpoint = len / 2
  for index in range(0, mirrorpoint):
    left = getSampleObjectAt(sound, index)
    right = getSampleObjectAt(sound, len - index - 1)
    value = getSampleValue(left)
    setSampleValue(right, value)
