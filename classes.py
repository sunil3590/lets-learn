class Student:
    def main(self):

    def __init__(self, name=None, age=None, qualification=None):
        print('inside init function')
        self.__name = name
        self.__age = age
        self.__qualification = qualification

    def print_details(self):
        print(self.__name)
        print(self.__age)
        print(self.__qualification)
        print('*' * 50)

    def grow_up(self):
        self._increase_age_by_one()

    def _increase_age_by_one(self):
        self._age = self._age + 1


# vishwa = Student('Vishwa', 22, 'BE')
# vishwa.print_details()
#
# # after 1 year
# vishwa.grow_up()
# vishwa.print_details()
#
# # try accessing private variable and function
# vishwa._increase_age_by_one()
# vishwa.print_details()

one = Student()
two = Student('two', 22, 'BE')
three = Student('three')
four = Student(age=20)

one.print_details()
two.print_details()
three.print_details()
four.print_details()

