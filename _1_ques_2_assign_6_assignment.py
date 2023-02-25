class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print("Name of Dog: ",self.name)
        print("Age of Dog: ", self.age)

    def get_info(self):
        return self.coat_color
    
class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        Dog.__init__(self, name, age, coat_color)

    def details(self):
        print("Name: {}".format(self.name))
        print("Age: {} years".format(self.age))
        print("Coat Color: {}".format(self.coat_color))



class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        Dog.__init__(self, name, age, coat_color)
    
    def details(self):
        print("Name: {}".format(self.name))
        print("Age: {} years".format(self.age))
        print("Coat Color: {}".format(self.coat_color))


print("\nPlease Enter Details of Jack Russel Terrier Dog.")
name1 = input("Enter name: ")
age1 = int(input('Enter age: '))
coat_color1 = input("Enter Coat Color: ")
print("\n===================")
print("Congratulations! Details of Jack Russel Terrier has been saved.")
jack_russell_terrier = JackRussellTerrier(name1,age1,coat_color1)
jack_russell_terrier.details()


print("\n======================")
print("Please Enter Details of Bull Dog.")
name2 = input("Enter name: ")
age2 = int(input('Enter age: '))
coat_color2 = input("Enter Coat Color: ")
print("\n===================")
print("Congratulations! Details of Bull Dog has been saved.")
bull_dog = Bulldog(name2, age2, coat_color2)
bull_dog.details()


