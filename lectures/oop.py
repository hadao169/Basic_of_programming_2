class student:
  def __init__(self,name,age):
    self.name = name
    self.age = age
    self.credits = 0
  
  def greet(self, greeting):
    print(f"{self.name}, {self.age} years old says: Hello!")
    print(f"{greeting}")
    
lisa = student("Lisa",10)
lisa.greet("Moi")
  