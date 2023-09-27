#Vector Storage
VectorStorage = []

#Create Vector Class, Constructor of [^i^, ^j^] and [^i^, ^j^, ^k^]
class Vector:
  def __init__(self, name, i = 0, j = 0, k = 0):
    self.name = name
    self.i = i
    self.j = j
    self.k = k

#Make Vector with 2 Values and a Name
def createVector2D(name, i, j):
  newVector2D = Vector(name, i, j, 0)
  return newVector2D

#Make Vector with 3 Values and a Name
def createVector3D(name, i, j, k):
  newVector3D = Vector(name, i, j, k)
  return newVector3D

#Print 10 blank lines to visually separate when you enter a new menu
def flushScreen():
  for i in range(10):
    print("")

#Main Menu
def mainMenu():
  while True:

    flushScreen()
    
    print("Welcome to Vector Maths App")
    userIn = input("Select an option: \n1: Create Vector\n2: View Vectors\n3: Add Vectors [WIP]\n4: Subtract Vectors [WIP]\n5: Dot Product Vector [WIP]\n6: Magnitude of Vector [WIP]\n7: Exit\n")
    
    if userIn == "1":
        createMenu()
    elif userIn == "2":
        viewMenu()
    elif userIn == "3":
        addMenu()
    elif userIn == "4":
        subtractMenu()
    elif userIn == "5":
        dotProductMenu()
    elif userIn == "6":
        magnitudeMenu()
    elif userIn == "7":
        print("Thanks for using the app, cya! Exiting the app.")
        break  # Exit the loop and end the program
    else:
        print("Invalid option. Please try again.")

#Create Vector Menu
def createMenu():
  flushScreen()

  userIn = input("Create 2D or 3D Vector:\n2: 2D\n3: 3D\n")

  flushScreen()

  if userIn == "2":
    name2D = input("Enter name of Vector: ")
    iVal2D = input("Enter i value: ")
    jVal2D = input("Enter j value: ")

    VectorStorage.append(createVector2D(name2D, iVal2D, jVal2D))

  if userIn == "3":
    name2D = input("Enter name of Vector: ")
    iVal2D = input("Enter i value: ")
    jVal2D = input("Enter j value: ")
    kVal2D = input("Enter k value: ")

    VectorStorage.append(createVector3D(name2D, iVal2D, jVal2D, kVal2D))
  
  pass

#Display Stored Vectors Menu
def viewMenu():
  flushScreen()

  displayTable = "Stored Vectors:\n"

  for index in range(len(VectorStorage)):
    vector_name = VectorStorage[index].name
    vector_i = str(VectorStorage[index].i)
    vector_j = str(VectorStorage[index].j)
    vector_k = str(VectorStorage[index].k)

    if vector_k == "0":
      displayTable += "[2D Vector: " + vector_name + "]: {" + vector_i + ", " + vector_j + "}\n"

    else:
      displayTable += "[3D Vector: " + vector_name + "]: {" + vector_i + ", " + vector_j + ", " + vector_k + "}\n"

  print(displayTable)
  
  pass

#Add Vectors together Menu
def addMenu():
  flushScreen()

  pass

#Subtract Vectors Menu
def subtractMenu():
  flushScreen()

  pass

def dotProductMenu():
  flushScreen()

  pass

def magnitudeMenu():
  flushScreen()

  pass

#Actual Program so far lol
mainMenu()

#Ignore this V
#Enter Vector Matrices as [i, j] or [i, j, k]:\nExamples: [5, 4] or [2, 4, 8]\n

#Select Create, Add, Subtract, Dot Product, or Distance
"""if (userIn == "1"):
  userIn = input("Create 2D or 3D Vector:\n2: 2D\n3: 3D\n")

  flushScreen()

  if userIn == "2":
    name2D = input("Enter name of Vector: ")
    iVal2D = input("Enter i value: ")
    jVal2D = input("Enter j value: ")

    VectorStorage.append(createVector2D(name2D, iVal2D, jVal2D))
    mainMenu()"""
