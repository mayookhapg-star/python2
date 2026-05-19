class Outer:
  def __init__(self):
     self.name = "Outer class"

  class Inner:
     def __init__(self):
        self.name = "Inner class"

     def display(self):
      print("this is the inner class")

outer = Outer()
print(outer.name)

inner = outer.Inner()
print(inner.name)
    