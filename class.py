class Person:

    def __init__(self, name):
        self.name = name


class Emplyer(Person):

    def __init__(self, name, salary,position):
        self.name = name
        self.salary = salary
        self.position = position

    def data(self):
       print('Name: {}. Salary: {}. Position: {}'.format(self.name, self.salary, self.position))



emp1 = Emplyer("Tom",3000,"CEO")
emp2 = Emplyer("Peter", 2000,"Programmer")
emp1.data()
emp2.data()


class Driver(Person):

    def __init__(self, name, experience, drivers_class):
        self.name = name
        self.experience = experience
        self.drivers_class = drivers_class

    def data(self):
        print('Name: {}. Experience: {}. Drivers Class: {}'.format(self.name, self.experience, self.drivers_class))

driver1 = Driver("Jack", 12,"D")
driver1.data()





        


