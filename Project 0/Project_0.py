def main():
  encoded = requestString('Please enter the encrypted message: ').upper()   
  alphabet = '.,!? ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  cipher(encoded,alphabet)  

def cipher(encoded,alphabet):        
  for shift in range(len(alphabet)):
    decoded = ('') 
    for i in encoded:
      findIndex=alphabet.find(i)
      alphabetIndex=(findIndex-shift)
      decodedLetter=alphabet[alphabetIndex]
      decoded=decoded+decodedLetter
    print decoded
  
main()