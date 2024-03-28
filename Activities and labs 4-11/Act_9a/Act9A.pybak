from SoundLib import *

def cScale():
  setMediaPath()
  source = makeSound(getMediaPath("a440.wav"))
  lenSource = getLength(source)
  #Create all notes
  c = note(261.626)
  d = note(293.665)
  e = note(329.628)
  f = note(349.228)
  g = note(391.995)
  a = note(440.000)
  b = note(493.164)
  c1 = note(523.251)
  #Copy notes into empty sound to create scale
  adjust = makeEmptySound(getLength(source)*9)
  copy(c,adjust,0)
  copy(d,adjust,lenSource)
  copy(e,adjust,lenSource1)
  copy(f,adjust,lenSource2)
  copy(g,adjust,lenSource3)
  copy(a,adjust,lenSource4)
  copy(b,adjust,lenSource5)
  copy(c1,adjust,lenSource6)
  #Create a chord and copy into sound
  chord = createChord(c,e,g)
  copy(chord,adjust,lenSource7)
  #Explore the scale and chord
  explore(adjust)


def note(freq):
  #Accepts a frequency and returns a sound for it by applying
  #  a factor to shift up or down from A440.
  a = makeSound(getMediaPath("a440.wav"))
  freq = freq/440.0
  b = shiftPitch(a,freq)
  return(b)
  

def shiftPitch(source, factor):
  #Written by: DL Largent based on Guzial & Ericson E4 Program 119
  #Date written: 10/16/13
  #Accepts a sound and a factor and returns a new sound
  #  shifted by the factor from the original sound.
  #  factor > 0 and < 1 will decrease pitch
  #  factor > 1 will increase pitch
  target = makeEmptySound(getLength(source))
  source_index = 0
  
  for target_index in range(0, getLength(target)):
    source_value = getSampleValueAt(source, int(source_index))
    setSampleValueAt(target, target_index, source_value)
    source_index = source_index + factor
    if (source_index >= getLength(source)):
      #Start over to allow new sound to be same length as original.
      source_index = 0
  return target


def createChord(note1, note2, note3):
  #Accepts three sound files that are "notes" and returns a 
  #  combined sound that forms a chord.
  c = makeSound(getMediaPath("a440.wav"))
  e = makeSound(getMediaPath("a440.wav"))
  g = makeSound(getMediaPath("a440.wav"))
  chord = makeEmptySound(getLength(note1))
  for index in range(0,getLength(c)):
    cValue = getSampleValueAt(c,index)
    eValue = getSampleValueAt(e,index)
    gValue = getSampleValueAt(g,index)
    total = cValue + eValue + gValue
    setSampleValueAt(chord,index,total*0.2)
  return chord
  