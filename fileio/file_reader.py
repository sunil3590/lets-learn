class File:
    def __init__(self, name):
        self.__name = name
        self.__f = open(name, 'r')

    def get_name(self):
        return self.__name

    def get_all_lines(self):
        lines = self.__f.readlines()
        self.__f.seek(0)
        return lines

    def print_all_lines(self):
        lines = self.get_all_lines()
        for line in lines:
            print(line)


def some_func():
    print('sdfasdf')
