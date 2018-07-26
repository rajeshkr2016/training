class Shark:
    def __init__(self, name):
        self.name = name

    def swim(self):
        print(self.name + " is swimming.")

    def be_awesome(self):
        print(self.name + " is being awesome.")

def main():
    Venkat = Shark("Venkat")
    Venkat.be_awesome()
    Venkat.swim()

    Srikanth = Shark("Srikanth")
    Srikanth.swim()

if __name__ == "__main__":
  main()

'''
Object-oriented programming is an important concept to understand because it makes code recycling more straightforward, as objects created for one program can be used in another. 
Object-oriented programs also make for better program design since complex programs are difficult to write and require careful planning, and this in turn makes it less work to maintain the program over time.
'''