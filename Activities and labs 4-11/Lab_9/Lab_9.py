from SoundLib import *

def main():
  blockingPlay(sineWave(500,12000,2))
  blockingPlay(squareWave(500,12000,2))
  source = makeSound(getMediaPath("airplane.wav"))
  airRepeat = copyNumberTimes(source,5)
  explore(echo(airRepeat,5000))

def echo(source,delay):
  target = duplicateSound(source)
  for index in range(delay,getLength(source)):
    echoSample = 0.6*getSampleValueAt(target, index - delay)
    comboSample = getSampleValueAt(source,index) + echoSample
    setSampleValueAt(target,index,comboSample)
  return(target)

def sineWave(freq,amp,sec):
  target = makeEmptySoundBySeconds(sec)
  sRate = getSamplingRate(target)
  interval = 1.0/freq
  sPerCycle = interval * sRate
  maxCycle = 2 * pi
  for pos in range(0,getLength(target)):
    rawSample = sin((pos/sPerCycle) * maxCycle)
    sampleValue = int(amp * rawSample)
    setSampleValueAt(target,pos,sampleValue)
  return(target)

def squareWave(freq,amp,sec):
  target = makeEmptySoundBySeconds(sec)
  sRate = getSamplingRate(target)
  interval = 1.0/freq
  sPerCycle = interval * sRate
  samplesPerHalfCycle = int(sPerCycle/2)
  sampleValue = amp
  s = 1
  i = 1
  for s in range(0,getLength(target)):
    if (i > samplesPerHalfCycle):
      sampleValue = sampleValue * -1
      i = 0
    setSampleValueAt(target,s,sampleValue)
    i = i + 1
  return(target)

def copyNumberTimes(source,number):
  target = makeEmptySound(getLength(source)*(number+1))
  for times in range(0,number+1):
    copy(source,target,times*getLength(source))
  return(target)