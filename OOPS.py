# class car:
#     pass
# audi = car()
# bmw = car()
# print(type(audi))

# class Dog:

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def bark(self):
#         print(f"{self.name} says Oh Yeah!")    
# dog1 = Dog("Joy",2)
# print(dog1)
# print(dog1.name
# print(dog1.ag
# dog1.bark()
# class Car:
#     def __init__(Self,Windows,Doors,Enginetype):
#       Self.Windows = Windows
#       Self.Doors = Doors
#       Self.Enginetype = Enginetype
#     def drive(Self):
#        print(f"The person will drive a {Self.Enginetype} car")
# Car1=Car(4,5,"EV")
# Car1.drive()

# class Tesla(Car):
#    def __init__(Self,Windows,Doors,Enginetype,is_selfdriving):
#       super().__init__(Windows,Doors,Enginetype)
#       Self.is_selfdriving = is_selfdriving
#    def driving(Self):
#       print(f"Tesla Supports self driving? : {Self.is_selfdriving}")

# Tesla1 = Tesla(2,2,"EV","Yes")
# Tesla1.driving()
# class Person:
#    def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender 

# def get_name(person):
#    return person.name

# person = Person("Krish",34,"Male")
# get_name(person) 

# Getter and Setter method for age 
class Person:
    def __init__(self,name,age):
        
      self.__name = name 
      self.__age = age
    def get_name(self):
        return self.__name
    def set_name(self,name):
       self.__name=name 
    def get_age(self):
       return self.__age
    def set_age(self,age):
       if (age>0):
          self.__age = age
       else:
          print("Age cannot be negative")
person  = Person("Rakshit", 36)

print(person.get_age())
person.set_age(35)
print(person.get_age())
person.set_age(-10)

    
      
