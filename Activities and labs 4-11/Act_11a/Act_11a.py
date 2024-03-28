def readFile(wordOut, wordIn):
  inFile = open(getMediaPath('Gettysburg.txt'), 'rt')
  outFile = open(getMediaPath('Gettysburg.txt'), "wt")
  line = inFile.readline()
  while line <> ":
    newLine = line.replace(wordIn, wordOut)
    outFile.write(newLine)
    line = file.readline()
  counter = inFile.count("\n")
  print line
  print (counter)
  inFile.close()

def main():
  wordOut = '\n\n'
  wordIn = '\n'