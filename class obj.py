class person:
    name="hitarth"
    occupation="employee"
    def info(self):
        print(f"{self.name} is an {self.occupation}")
    
a=person()
b=person()
b.name="kalp"
b.occupation="hr"
a.info()
b.info()