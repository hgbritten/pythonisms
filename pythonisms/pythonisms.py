from ll import LinkedList
from functools import wraps
from time import sleep


def procrastinate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        sleep(3)
        return func(*args, **kwargs)

    return wrapper


@procrastinate
def say(txt, salutation="Dear Sir or Madam"):
    print(salutation + ", " + txt)


def sarcastic_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return f'Oh Sure, "{orig_val}" sounds like a "great" idea'

    return wrapper


@sarcastic_decorator
def propose_idea(idea):
    return f"How about {idea}?"


if __name__ == "__main__":
    result = propose_idea("gelato")
    print(result)
