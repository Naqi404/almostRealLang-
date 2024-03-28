def main():
  name = requestString("Type your name: ")
  counter = 1
  for i in range(len(name)):
    letter = i * counter
    