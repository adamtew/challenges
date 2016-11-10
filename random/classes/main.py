class Person:
    """ Member variables """

    def __init__(self, name):
        self.name = name
        self.name = ''
        self.age = 0
        self.gender = None

    def get_age(self):
        return self.age

""" Inheritance """


class Male(Person):
    def __init__(self, name):
        Person.__init__(self, name)
        self.gener = 0


print 'class'
