'''

Class — A blueprint created by a programmer for an object.
This defines a set of attributes that will characterize any object that is instantiated from this class.

Object — An instance of a class. This is the realized version of the class, where the class is manifested in the program.

'''

# defining a class
class Shark:
    def swim(self):
        print("The shark is swimming.")

    def be_awesome(self):
        print("The shark is being awesome.")

'''
The argument to these functions is the word self, which is a reference to objects that are made based on this class. To reference instances (or objects) of the class, self will always be the first parameter, but it need not be the only one.
'''
# An object is an instance of a class

def main():
    sammy = Shark()
    sammy.swim()
    sammy.be_awesome()

if __name__ == "__main__":
    main()

