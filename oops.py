# CLASS IS A BLUEPRINTE FOR CREATING OBJECT.

class student:
    name="suryajeet"
s1=student()
print(s1.name)

class car:
    color="blue","yellow"
    brand="mercedes"
car1=car()
print(car1.color)
print(car1.brand)

# __init__function!!
# SELF PARAMETER IS REFERENCE TO THE CLASS AND USED TO ACCESS VARIABLES OF THE CLASS.

class student:
    def __init__(self,fullname):
        self.name=fullname
        print("adding new student in database.")
s1=student("karan")
print(s1.name)
s2=student("surya")
print(s2.name)

class student:
    def __init__(self,name):
        self.name=name
s1=student("surya")
s2=student("mansi")
s3=student("sms")
print(s1.name)
print(s2.name)
print(s3.name)

class student:
    college_name="csvtu"
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def welcome(self):
        print("welcome student",self.name)
    def get_marks(self):
        
        return self.marks
s1=student("MANSI",99)
s1.welcome()
print(s1.get_marks())

class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hi",self.name,"your avg marks is :",sum/3)
s1=student("MANSI",[99,100,98])
s1.get_avg()

s2=student("SURYAJEET",[100,98,96])
s1.name="SURYA"
s2.marks=[100,100,100]
s1.get_avg()

class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,"age is",self.age)

s1=dog("tommy",5)
s1.show()
s2=dog("jerry",6)
s2.show()


class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

s1=rectangle(20,20)
s1.area()
print("area of rec:",s1.area())


class book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
        print("book created:",self.title)
    def an(self):
        return self.title ,self.author
s1=book("wings of fire","APJ ABDUL KALAM")
title,author=s1.an()
print("book named",title,"by",author)