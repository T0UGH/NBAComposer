class Dog:
    def __init__(self):
        self.eye = 2
        self.leg = 4


if __name__ == '__main__':
    dog = Dog()
    print(getattr(dog, 'eye'))

