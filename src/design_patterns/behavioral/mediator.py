"""
https://www.djangospin.com/design-patterns-python/mediator/

Objects in a system communicate through a Mediator instead of directly with each other.
This reduces the dependencies between communicating objects, thereby reducing coupling.

*TL;DR
Encapsulates how a set of objects interact.
"""


class ChatRoom(object):
    """Mediator class"""
    @staticmethod
    def display_message(user, message):
        return "[{} says]: {}".format(user, message)


class User(object):
    """A class whose instances want to interact with each other"""

    def __init__(self, name):
        self.name = name

    def say(self, message):
        ChatRoom.display_message(self, message)

    def __str__(self):
        return self.name


"""
>>> molly = User('Molly')
>>> mark = User('Mark')
>>> ethan = User('Ethan')

>>> molly.say("Hi Team! Meeting at 3 PM today.")
[Molly says]: Hi Team! Meeting at 3 PM today.
>>> mark.say("Roger that!")
[Mark says]: Roger that!
>>> ethan.say("Alright.")
[Ethan says]: Alright.
"""
