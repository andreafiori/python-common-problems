from abc import ABCMeta, abstractmethod

class Animal(object):
    __metaclass__ = ABCMeta

    def __init__(self):
        pass

    @abstractmethod
    def say_something(self):
        return "I'm an animal!"

class Cat(Animal):
    def __init__(self):
        pass

    def say_something(self):
        s = super(Cat, self).say_something()
        return "%s - %s" % (s, "Miauuu")
