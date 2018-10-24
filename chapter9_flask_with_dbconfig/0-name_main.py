def func1():
    print("this is printed from func1")

def func2():
    print("this is printed from func2")



#__name__ = "new name"

if __name__ == "__main__":
    func1()
else:
    func2()


'''
built in variable : __name__ 
default assignement : __name__ = "__main__"
'''