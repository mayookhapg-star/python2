class tv:
    def on(self):
        print("tv is on")

d1=tv()  # object
d1.on()

class fan:
    def on(self):
        print("turn on fan")

d1=fan()
d1.on()



class person:
 def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = person("Emil", 36)

print(p1.name)
print(p1.age)