class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getPersonInfo (self):
        return self.name, self.age
    
    def setAge (self, age):
        self.age = age


person =  Person("John","55")
print (person.getPersonInfo())

person.setAge(44)
print (person.getPersonInfo())

print (person.age)

