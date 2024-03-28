classData=[]

def record():
  ident=requestString("Enter student's identification: ")
  name=requestString("Enter student's name: ")
  major=requestString("Enter student's major: ")
  gpa=requestNumber("Enter student's GPA: ")
  score=requestInteger("Enter student's score: ")
  return [ident,name,major,gpa,score]

def display(record):
  printNow("ID: " + record[0])
  printNow("Name: "+record[1])
  printNow("Major: "+record[2])
  printNow("GPA: " + str(record[3]))
  printNow("Score: " + str(record[4]))

def main():
  number=int(input("Enter the number of records: "))
  for i in range(number):
    classData.append(record())
  classData.sort()
  for r in classData:
    display(r)