#Magic8Ball.py
#Name:Luke Sheardown
#Date:9-1-2025
#Assignment:Lab 2

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  #Prompt the user for their question.
  print("What is my name")
answers = ["Luke 1", "Jeff 2", "Mike 3", "Taylor 4", "Gordon 5"]
  #Answer question randomly with one of the options from your earlier list.
r = random.random() * 5


r = int(r) #cut off any decimal values

print(r)
response = answers[r]
print(response)

if __name__ == '__main__':
  main()
