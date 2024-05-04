class Person:
    """
    this is class Person 
    """
    
    def __init__(self, name: str, age: int, yearbrith: int) -> None:
        self.name = name
        self.age = age
        self.year = yearbrith
    
    def greeting(self):
        """
        greeting person!
        """
        
        print(f'Hello {self.name}!')
        return
    
    def getInfor(self):
        person = dict({
            'name': self.name,
            'age': self.age,
            'year_of_brith': self.year
        })
        return person
    
    
myPerson = Person('adam', 25, 1998)

myPerson.greeting()