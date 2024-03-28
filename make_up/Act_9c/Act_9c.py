def main():
  setMediaPath()
  s1 = makeSound(getMediaPath("car.wav"))
  delay = (getDuration(s1)*2)
  num = 16000
  echoes(s1, delay, num)
  

def echoes(s1, delay,num):
# Create a new snd, that echoes the input soundfile
# num number of echoes, each delay apart
  ends1 = getLength(s1)
  ends2 = int(ends1 + (delay * num))
  s2 = makeEmptySound(ends2)
  echoAmplitude = 1.0
  for echoCount in range(1,num):
  # 60% smaller each time
    echoAmplitude = echoAmplitude * 0.6
    for posns1 in range(0,ends1):
      posns2 = int(posns1+(delay*echoCount))
      values1 = getSampleValueAt(s1,posns1)*echoAmplitude
      values2 = getSampleValueAt(s2,posns2)
      setSampleValueAt(s2,posns2,values1+values2)
  play(s2)
  return s2