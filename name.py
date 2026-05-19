class person:
    def __init__(self, name):
        self.name = name

    def greet(self):
      print("hello,my name is " + self.name)

p1 = person("Emil")
p1.greet()