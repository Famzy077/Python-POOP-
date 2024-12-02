class person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def more(self):
        if info.age <= 20:
            print(f'You\'re still a kid {info.age} years old')
        elif info.age > 40:
            print(f'You\'re an adult {info.age} years old')
        else:
            print(f'You\'re an young adult {info.age}')
        
info = person('Akinola Femi Odu Aremu', 24, 'Male')
info.age = int(info.age)
print(info.name, info.age, info.gender)
info.more()