class pyTest(object):
    def __init__(self,name,age):
        self.name = name
        self.age = int(age)
        if self.name == '':
            self.name = 'wangxu'
        if self.age <= 0:
            self.age = 32
    def printInfo(self):
        print (self.name)
        print (self.age)

if __name__ == '__main__':

    myName = input('input name:')
    try:
        myAge = int(input('input age:'))
    except ValueError as identifier:
        myAge = 33
    print ('****************************')
    pt = pyTest(myName,myAge)
    pt.printInfo()