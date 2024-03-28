def main():
  setMediaPath()
  source1 = makeSound(getMediaPath("preamble10.wav"))
  source2 = makeSound(getMediaPath("c4.wav"))
  smpl = getSamples(source2)
  for i in range(0,getLength(source2)):
    x = getSampleValue(smpl[i])
    newSampleValue = x * 0.25
    setSampleValue(smpl[i],newSampleValue)
  #blockingPlay(source1)
  #blockingPlay(source2)
  explore(merge(source1,source2))

def merge(source1,source2):
  len1 = getLength(source1)
  len2 = getLength(source2)
  maxLength = max(len1,len2)
  minLength = min(len1,len2)
  targ = makeEmptySound(maxLength)
  i1 = 0
  for i in range(0,maxLength):
    i1 = i1 +1
    if i1 >= minLength:
      i1 = i1 - minLength
    s1Sample = getSampleValueAt(source1,i)
    s2Sample = getSampleValueAt(source2,i1)
    setSampleValueAt(targ,i,s1Sample+s2Sample)
  return(targ)