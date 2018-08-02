from abc import ABCMeta, abstractmethod

"""
Animal parent class
"""
class Animal:
    __metaclass__ = ABCMeta

    @abstractmethod
    def say_something(self):
        return "I'm an animal!"

"""
Cat child class
"""
class Cat(Animal):
    def __init__(self):
        pass

    def say_something(self):
        s = super(Cat, self).say_something()
        return "%s - %s" % (s, "Miauuu")
