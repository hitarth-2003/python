class person:
    def __init__(self,n,o):
     self.name=n
     self.occupation=o
    def info(self):
        print(f"{self.name} is an {self.occupation}:")
a=person("hitarth","develpoer")
b=person("kalp","hr")
a.info()
b.info()
