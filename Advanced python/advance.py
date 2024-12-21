# x=int(input("enter nummber first"))
# y=int(input("enter nummber second"))
# z=int(input("enter num LAST"))

# max_digit =lambda x,y,z:x if(x>y and x>z) else  y  if(y>z)  else z

# print("maximum digit is",max_digit(x,y,z))
# decrator 
# def fun1(x):
#     def fun2(p,q):
#         p=p+5
#         q=q+10
#         data =x(p,q)
#         return data
#     return fun2
# @fun1
# def main_function(x,y):
#     return x+y
# x=main_function(5,10)
# print(x)
# 09/12/2024
# Generator
# def fibonacci(x):
#     a,b=0,1
#     while b<x:
#         yield b
#         a,b=b,a+b
# data=fibonacci(5)
# # print(data)
# print(next(data))
# print(next(data))
# print(next(data))
# print(next(data))

# def even_no(n):
#     i=2
#     while i<=n:
#         yield i
#         i+=2
# n=int(input("enter the number"))
# x=even_no(n)
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))


# class student:
#     x=2
#     y=7
  
#     def add(p,q):
#         return p+q
#     def __init__(self):
#         print("constructor called")
#         print(id(self))
   
# obj=student()
# print(id(obj))
# obj.__init__()
# obj.__init__()
# obj.__init__()
# obj.__init__()
# obj.__init__()
# obj.__init__()
# obj2=student()
# print(id(obj2))
# print(dir(student))
# print(dir(obj))

# 13/12.24
# class school:
#     def __init__(self,name,city):
#         self.name=name
#         self.city=city
#         print(id(self))
# obj1=school('model','malthone')
# print(id(obj1))
# obj2=school('model hai','sagar')
# print(id(obj2))
# print(obj1.name)
# print(obj1.city)
# print(obj2.name)

# # Instance variable
# # object dependent
# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         print(self.name)
#         print(self.age)
        

#     def add(self,school):
#         self.school = school #declare
#         print(self.name)
#         print(self.age)
    
#     def show_details(self):
#         print(self.name)
#         print(self.age)
#         print(self.marks)
#         print(self.school)
        

# obj=student('neeraj',56)
# obj.marks=[1,2,3,4]  #outside of the class
# print(obj.name)
# print(obj.age)
# obj.add("jaiho")
# obj.show_details()


# static and class variable

# class student1:
#     school='Model University'
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         student1.school_city='bhopal'
#         print(student1.school)
        

#     def add(self):
#         self.school_code = 1008 #declare
#         print(student1.school_city)
# obj1=student1('mohit',23)
# student1.school_principal="indore"
# print(student1.school_city)


# local variable
# x=50
# class student3:
#     x=10
#     def new():
       
#         print(x)
        
#     def new1():
#         global x
#         print(x)
#         x=60
#         print(x)
# obj3 = student3
# print(x)
# obj3.new()
# obj3.new1()
# print(x)



# class A:
#     def __init__(var):
#         print("constructor")
#     def __init__(self):
#         print("constructor 2")
# obj4=A()
# obj4.__init__()
# print(dir(obj4))


# # # METHODS
# # 1.Instance method
#     #    Example
# class B:
#     def new(self):
#         print("Hello method")
#     def new1(self):
#         self.new()
# obj5=B()
# obj5.new()
# obj5.new1()







# Class method
class Book:
    price =230
    def __init__(self,author,year):
        self.x=author
        self.y=year
    def show_details(self):
        print(self.x)
        print(Book.price)
        print(self.y)
    @classmethod
    def update_price(cls,price):
        cls.price=price
obj=Book('mohit',2024)
obj.show_details()
obj.update_price(4067)
obj.show_details()