class Student:

    #student_fields = ['first_name', 'last_name', 'email', 'age', 'address', 'gender', 'point']

    STUDENTS = []

    #TEST_STUDENTS = [
    #    ['Mary', 'D', 'mail@mail.com', '19', 'Huston', 'F'],
    #    ['John', 'S', 'new_mail@mail.com', '21', 'London', 'M'],
    #    ['Andy', 'H', 'more_mail@mail.com', 'sexteen', 'Brighton', 'M']
    #]

    def __init__(self, first_name, last_name, email, age, address, gender, point=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.address = address
        self.gender = gender
        self.point = point
        Student.STUDENTS.append({self.first_name: self})





    def __lt__(self, other):
        if hasattr(other, 'age'):
            return self.age < other.age
        else:
            return False

    def __le__(self, other):
        if hasattr(other, 'age'):
            return self.age <= other.age
        else:
            return False

    def __gt__(self, other):
        if hasattr(other, 'age'):
            return self.age > other.age
        else:
            return False

    def __ge__(self, other):
        if hasattr(other, 'age'):
            return self.age >= other.age
        else:
            return False

    @classmethod
    def print_total_student(cls):
        print(cls.STUDENTS)

    @classmethod
    def add_student_dict(cls, dict_student):
        obj = cls(first_name='', last_name='', email='', age=0, address='', gender='', point=0)
        for key in dict_student:
            setattr(obj, key, dict_student[key])
        return obj

    def student_email(self, email):
        if '@' in email and email[0] != '@' and email[-1] != '@'  :
            self.student_email = email
        else:
            raise AttributeError('Your email is wrong!!!!')


class Group:

    def __init__(self, first_name, last_name, email, age, address, gender, point=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.address = address
        self.gender = gender
        self.point = point
        self.STUDENTS = []

    def __iter__(self):
        self.index_student = 0
        return self

    def __next__(self):
        if self.index_student < len(self.STUDENTS):
            _index = self.index_student
            self.index_student += 1
            return self.STUDENTS[_index]
        else:
            raise StopIteration


    def add_student_to_group(self, *args):
        for student in args:
            self.STUDENTS.append(student)






group = Group('001')

if __name__ == '__main__':

    student = Student()

    group.add_student_to_group(student.STUDENTS)

    iter_group = iter(group)
    for student in iter_group:
        print(student)