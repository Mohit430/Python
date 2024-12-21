# Single level inheritance

# class A:
#     x=10
#     y=90
#     def p_name(self,name):
#         self.x = name
#         print(self.x)
# class B(A):
#     def c_name(self, name):
#         self.y = name
        

# obj2=B()
# print(obj2.x)
# print(obj2.y)
# print(obj2.p_name("jail house"))

# # multilevel inheritance   
# # Multiple inheritance

# class Father:
#     def property(self, f_name,f_bank):
#         self.f_name = f_name
#         self.f_bank = f_bank
     
# class Mother:
#         def property1(self, m_name, m_bank):
#             self.m_name = m_name
#             self.m_bank = m_bank
# class Child(Father,Mother):
#         def own_property(self,city):
#             self.city = city
#             print(self.f_name)
#             print(self.f_bank)
#             print(self.m_name)
#             print(self.m_bank)
#             print(self.city)
# obj=Child()
# # obj.own_property("malthone")
# obj.property("mohit","punjab")
# obj.property1("atul","mumbai")
# obj.own_property("sagar")
# print(dir(Child))

# hybrid inheritance

# class Grandfather:
#     def grand_property(self, gf_name, gf_bank):
#         self.gf_name = gf_name
#         self.gf_bank = gf_bank
# class father:
#     def property(self, f_name,f_bank):
#         self.f_name = f_name
#         self.f_bank = f_bank
# class Ladka:
#     def property1(self, l_name, l_bank):
#         self.l_name= l_name
#         self.l_name = l_bank
# class Ladkekaladka(Grandfather,Father,Ladka):
#     def own_property(self,city):
#         self.city = city
#         print(self.gf_name)
#         print(self.gf_bank)
#         print(self.f_name)
#         print(self.f_bank)
#         print(self.l_name)
#         print(self.l_bank)
#         print(self.city)

# obj=Ladkekaladka()

# # obj.own_property("malthone")

# obj.grand_property("rahul","punjab")
# obj.property("mohit","punjab")
# obj.property1("atul","mumbai")
# obj.own_property("sagar")
# print(dir(Ladkekaladka))

# Polymorphisms
# single function  having many forms
# same function name with different   
# class A:
#     def Add(self,*n):
#         sum=0
#         for i in n:
#             sum=sum+1
#         print(sum)
# obj=A()
# obj.Add(10,50)
# obj.Add(1,2)


# method overriding
class A:
    def add(self,x,y):
        self.x=x
        self.y=y
        print( self.x+self.y)
class B(A):
    def add(self,x,y,z):
        
        self.p=x
        self.q=y
        self.r=z
        super().add(x,y)
        print( self.p+self.q+self.r)
obj= B()
# print(dir(B))
obj.add(10,20,90)

# Encapsulation
# multiple attributes wrap up into a single unit
class A:
    x=90
    y=89
    def add(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def new1(cls,p):
        cls.p=p
    @staticmethod
    def great():
        print("Great")
print(dir(A))


# Access specifier
class A:
    _x=10
    _y=89
    def _show (self):
        print("class A")
class B(A):
    pass
class C:
    pass
print(dir(C))
# print(dir(B))
obj=B()
print(obj._x)
print(obj._y)
obj._show()


# Abstraction
# hiding internal process


# Extra
# exception handling 
# file handling
# conpinancor



    

