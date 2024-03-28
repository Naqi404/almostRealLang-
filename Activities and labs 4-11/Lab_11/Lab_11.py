def checkVowel(character):
   string = character
   vowel = 'aeiou'
   if string[0].lower() in vowel:
      printNow(string,'starts with vowel',string[0])
      return true
   else:
      printNow(string,'starts with consonant',string[0])
      return false

def pig_latin(word):
  word = word.strip().lower()
  pig_latin =''
  vowel = ['a','e','i','o','u']
  for i in range(len(word)):
    if word[i] in vowel:
      if i==0:
        word+="w"
        pig_latin+=word[i:]+word[0:i]+"ay"
        break
  return pig_latin
  
def readText():
  inFile = open(pickAFile(), 'rt')
  text = inFile.read()
  inFile.close()
  return text
  
def pickAndReadText():
  data = readText()
  data = data.splitlines()
  word = data.lower()  #I don't know why this is giving me an error? I'm asking for a string 'data' to be in lower
  outLine = pig_latin(data)
  print outLine