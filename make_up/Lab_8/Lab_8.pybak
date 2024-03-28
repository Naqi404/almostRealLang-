from SoundLib import *

def main():
  setMediaPath()
  sourceA = makeSound(getMediaPath("gettysburg.wav"))
  sourceB = makeSound(getMediaPath("preamble.wav"))
  #blockingPlay(sourceA)
  #blockingPlay(sourceB)
  woven = interweave(sourceA, sourceB) #wait a second is it interleave or interweave, I always thought it was interweave like with clothes and threads /irrelevant
  blockingPlay(woven)

def interweave(sourceA,sourceB):
  lenA = getLength(sourceA)
  lenB = getLength(sourceB)
  target = makeEmptySound(lenA+lenB,int(getSamplingRate(sourceA)))
  s = int(getSamplingRate(sourceA)*2)
  gs = int(lenA/s +1)
  twos = int(lenB/s +1)
  large = max(gs,twos)
  indexA = 0
  indexB = 0
  indexC = 0
  for i in range(large):
    if lenA > indexA:
      endindex = indexA+s
      clipend = min(endindex,lenA)
      x = clip(sourceA, indexA, clipend)
      copy(x,target,indexC)
      indexC = indexC+clipend-indexA
      indexA = clipend
    if lenB > indexB:
      endindex = indexB+s
      clipend = min(endindex,lenB)
      x = clip(sourceB, indexB, clipend)
      copy(x,target,indexC)
      indexC = indexC+clipend-indexB
      indexB = clipend
  return(target)

