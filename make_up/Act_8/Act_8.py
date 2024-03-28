def main():
  setMediaPath()
  source = makeSound('c4.wav')
  parabolic(source)
  explore(source)
  

def parabolic(sound):
  length = getLength(sound)
  for index in range(0, int(length/3)):
    value = getSampleValueAt(sound, index)
    setSampleValueAt(sound, index, value)
  for sampleIndex in range(length/3, int((length*2)/3)):
    value = getSampleValueAt(sound, index)
    setSampleValueAt(sound, index, value*2)
  for index in range(int((length*2)/3), length):
    value = getSampleValueAt(sound, index)
    setSampleValueAt(sound, index, value)