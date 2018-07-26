'''
The Constructor Method
The constructor method is used to initialize data.
It is run as soon as an object of a class is instantiated.
Also known as the __init__ method, it will be the first definition of a class and looks like this:

'''

class Shark:
    def __init__(self):
        print("This is the constructor method.")

    def swim(self):
        print("The shark is swimming.")

    def be_awesome(self):
        print("The shark is being awesome.")



def main():
    sammy = Shark()
    sammy.swim()
    sammy.be_awesome()

if __name__ == "__main__":
    main()
