class animal:
    def __init__(self,name,age):
        self.name = name
        self.age =age 
    def __str__(self):
        return self.name+"" +str(self.age)    
class cat(animal):
    def speak(self):
        print("meow")

#oba = animal("meow", 5)
#print(oba) 
obc = cat()
print(obc)
