# Assignment 1: Design Your Own Class! 🏗️

class Book:
  def __init__(self, title, author):
    self.title = title
    self.author = author

  def __str__(self):
    return f"{self.title} was written by {self.author}"   
  
  def read(self):
    print ("You are reading the book " + self.title) 

bk1 = Book("THE FOUR-WAY PATH", "Hector Garcia")
bk2 = Book("IKIGAI", "Hector Garcia")

print(bk1)
print(bk2)
bk1.read()
bk2.read()

# Activity 2: Polymorphism Challenge! 🎭

class Car:
  def move(self):
    return "Driving"
    
class Plane:
  def move(self):
    return "Flying"

class Person:
  def move(self):
    return "Walking"

for motion in [Car(), Plane(), Person()]:
  print(motion.move())