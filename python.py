# print(98+905)
# print()

# c = 'a'
# print("The ASCII value of '" + c + "' is", ord(c))
# print("anti"<"abcd")\\\\
 
# num1 = int(input ("enter number1:"))
# num2 = int(input ("enter number2:"))
# num3 = int(input ("enter number3:"))
# num4 = int(input ("enter number4:"))
# num5 = int(input ("enter number5:"))

# lis = [num1, num2, num3, num4,num5]
# print(lis)
  
# student_details  = ["mohit",24,"bhopal",[23,56,78]]
# print(student_details)
# student_details [1] = 23
# print("city:",student_details[-2])
# print("name:",student_details[0])
# print("age:",student_details[1])
# print("num:",student_details[3])
# print(type(student_details))
# student_details[3][1]=50
# print(student_details[3][1]+ student_details[3][2])
# lis = []
# lis1 =lis()  #list()
# print(lis,type(lis))
# print(lis1,type(lis1))

# fruit = []

# fruit.append("apple")
# print(fruit)
# fruit.append("bsnsnns")
# print(fruit)

# fruit.append("papeta")
# print(fruit)


# 09/10/2024


# lis=['mohit','jai','jpo']
# lis1=[23,34,56,23,23,23,23,23]
# #list.count(element)----> Return number of occurence(frequency)

# c = lis1.count(23)
# print(c)

# #max(), min(),len(),sum()
# print(lis1)
# print("maximum" ,max(lis1))
# print("minimun" ,min(lis1))
# print("length" ,len(lis1))
# # print("sum" ,sum(lis1))
# # DOt operator are uesd 


# lis = []
# r= lis.append(89)
# print(lis)
# print(r)
# extend
#  insert
# # ---------------Index------------>
# lis = [2,3,5,4,5,67,8,8,2,4,4,5,6,4,3,4]
# # r= lis.index(4)
# # print(r)
# # r1= lis.index(4)
# # print(r1)
# r= lis.index(4,0)
# # index (element start ,end )--> end exclusive (just earlier)
# print(r)
# r1= lis.index(4,r+1)
# print(r1)
# r2= lis.index(4,r1+1)
# print(r2)
# r3= lis.index(4,r2+1)
# print(r3)
# Note-> Exception handling , To run a loop number of accurance time.

#  Count function...............
# num = lis.count(4)
# print(num)

# #  sort () Function..........

# lis.sort()
# print(lis)


# lis.sort(reverse=True)
# print(lis)
# #  In place function
# lis.reverse()
# print(lis)

#  element remove 
#pop()----> deleted last  element return 
# pop(index)-----> deleted index element return ..

# d= lis.pop()
# print(d)

#  element instead of index ----> Remove ()(non-return )
# lis = [2,3,44,5,6,7]
# print(lis)
# lis.remove(44)
# print(lis)

#  clear() function 
# lis = [2,3,44,5,6,7]
# print(lis)
# lis.clear()
# print(lis)

#  delete statement........
# lis = [2,3,44,5,6,7]
# print(lis)
# del lis
# print(lis)

# #  lis can be conatenated 

# lis = [2,3,4,5,6,7] + [45,67]   # strong typing
# print(lis)

#  *Slizing 
    #    0  1 2  3   4        5  6 7   8   9    10 11
# lis = [23,4,5,67,"sourabh",333,4,8.8,7,"arun",5,66]
#     #  lis[start:end:jump]
#     #  end (excluded)(just stop before end)
#     # jump (may be +ive or -ive) default = 1
# a = lis[4:10:1]
# print(a)
# a = lis[4:10:2]
# print(a)
# a = lis[4:10:3]
# print(a)
# a = lis[4:10:-3]

# print(a)
# a = lis[9:3:-1]
# print(a)
# a = lis[4:10:-2]
# print(a)

# st = "mohit jannhai hai yaha issliye"
# print(st[5:24])


#  16-10-2024

# tuple

# i) immutable 
# ii) sequence(ordered data type)
#  iii) container (more than one value)
# iv) faster than list
# v) object once created never going to mutate.
# vi) representation 
# (comma seperated element)
# vii) single element representation 
# viii) empty tuple..

# t = (3,4,5,6)
# print(type(t))
# t1 = 3,4,5,6  # multiplr return in function.
# print(type(t1))

# t3 = (3,)
# print(type(t3))


# t4 = (23,34,45,66)
# print(t4)
# print(t4[1])
# # t[1] =90 error (immutable)


# a = 23
# t = (23,44,5,67)
# t = (23,44,5,57)
# print(t)
# print(id(a))
# print(id(t[0]))

#  isupper(),islower(),isalpha,isdigit(),--- return boolean

# s = "ertdgdhjdvdhdbdhdbgd"
# a = s.isalpha()
# print(a)
# lis = ['we','are', 'here', 'to', 'learn','a','python']
# lis1 = ["apple","banana"]
 


#  19/10/2024

# Dictionary. data type.......
# It is mapping data type  in  which each element is represented as key value pair.  dictionary is mutable data type and also it is a ordered data type.(no indexing)

#  Representation of Dictionary-> 
# 


# "features of key and  value"====>  
# 1) key should be unique , if key is repeated then new key value pair override  old key value pair.
# No change in order
# 2) key must be consist of immutable data type ,, value may be duplicated and consist  of any object.
# record = {
#     404050606060 : "aadhar details",
#     ("abcd@gmail.com", "cybrom@123"): "access granted",
# }
# print(record[404050606060])
# userid=input("enter userid:")
# passd=input("enter passd:")
# print(record[userid,passd])

# d = {1:"mon", 2:"tue"}
# d[3] = "web"
# d.update({3:"jaiho"})
# d[4] = "thr"
# d[5] = "fri"
# d[1] = "jai"
# print(d,len(d))


# d = { 101:["ajay",22,"bhopal",4767288726],
# 102:["atul", 23,"malthgone",636723563]}

# # print(d[101])
# # print([101][2])
# d[102][3]=83884664
# print(d[102])
# d[102][0]="mohit"
# print(d[102])


# d1 = { 101:{"name":"ajay", "age":22,"city":"bhopal"},
# 102:{"name":"atul", "age":23,"city":"malthgone"}}

# d1[102]["city"]="jaipur"

# d1[102].update({"city":"indore"})
# print(d1)
# d1[102].update({"pincode":101010})
# print(d1)
# # method of dictionary

# d2 = {"name":"ajay", "age":22,"city":"bhopal"}
# # d.keys()---> return keys.
# k = d2.keys()
# print(k)
# # d.values()---> return values.
# v =d2.values()
# print(v)
# i=d2.items()
# print(i)

# sorted_key= sorted(d2.keys())
# print(sorted_key)


# # Zip function
# names =["mohit", "jain"]
# age = [23,45]

# data = dict(zip(names,age))
# print(data)


# # 22/10/2024

# # get(key)--> return value...

# data = {1:"mon",2:"tue",3:"wed"}
# # r = data[23]
# r = data.get(23)
# print(r) 

# # setdefault()-----> value return
# #  1) key exist---> no changes, return associate value
# #  1) key not exists--> dict update (key value pair add)
#                     #    return new associate value.
# data1 =    {1:"mon",2:"tue",3:"wed"}  
# print(data1)
# r1= data1.setdefault(11,"jain")
# print(data1)
# print(r1)               

# # pop(key)----> return deleted value
# #  popitem() --->return deleted item

# data = {1:"mon",2:"tue",3:"wed"}
# print(data)
# r=data.pop(2)
# print(data)
# print(r)


# data = {1:"mon",2:"tue",3:"wed"}
# print(data)
# r=data.popitem()
# print(data)
# print(r)

# lis = ["jai","ajay","jainho"]
# school = "kvs"
# data = {  }
# data = data.fromkeys(lis,school)
# print(data)

# data = { '1':2345,'2':3746,'3':2386,'4':{'11':2345,'22':2344,'44':9876}}
# print(data)
# r = data['4'].pop('22')
# print(data)
# print(r)

# 23/10/2024

# Set =>  set is  a container in which we conatin multiple data,(homogeneous or heterogeneous)
#  but duplicate is not allowed  , and it is an unordered data type
# 2) where our main concern is data , but not any order related to it, then we use set. 


# s = set()
# print(type(s))
# print(s)

# soap = {"dettol ka dhule no. one brand","dettol", "lifeboy","wildstone","lux"}
# print(type(soap))
# print(soap)

# soap.add("lifeboy is best")
# print(soap)
# soap.add(("jaihoo","dettol"))
# print(soap)

# soap.update({"1",2,3,4})
# print(soap)

# s1 = {1,2,3,4,5,6}
# s2 = {1,3,6,0,87,4,5,6}
# s3 = {1,5,6}

# # s4= s1.union(s2,s3)
# s4 = s1|s2|s3
# print(s4)

# # s5= s1.intersection(s2,s3)
# s4 = s1&s2&s3
# print(s5)



#  Condition Statement ==> Basically divided into three part.
# 1) if-else 2) Ladder 3) Nesting
''' if Condition:
 body_of_if_statement
'''  

# if False:
#     print("jai ho")
#     print("jai ho")
#     print("jai ho")
# else:
#     print("kaise ho")
#     print("kaise ho")
#     print("kaise ho")

#  Q->  WAP to determine whether a person  eligible to cast code or not on the basis of age....................
# age = int(input("enter number"))
# if age>=18:
#     print("ur eligible")
# else :
#         print("ur not")



# # percentage
# a = int(input("enter number"))

# if (a>=75):
#     print("ur eligible")
# else : 
#     print("not")


# unit =int(input("enter totalunit"))
# total =unit*100
# if total>1000 :
#     print("eligible")
#     dis = total *(10/100)
#     print("discount",dis)
#     print("total pay:",total-dis)

# else :
#     print("no")
#     print("total pay:",total)

# wap to determine whether a charcter is a vowel or not
# char = input("enter char:")
# v="AEIOUaeiou"
# if char[0] in v: 
# # if char ==  'A' or char=='E' or char=='I' or char=='O' or char=='U':

#      print("vowels")
# else:
#     print("not")

# # synatax of Ladder
# ''' if condition1
    # body
    # elif cond2
    # body
    # else optinal
    # body
    # '''
# Q-6-->>
# cp = int(input("enter number"))

# if  cp<=100 and cp>0:
#     dis = 0
# elif cp>=101 and cp<=500:
#     dis =cp*(10/100)

# elif cp>=501 and cp<=1000:
#     dis =cp*(20/100)

# elif cp>1000 :
#     dis =cp*(30/100)

# print("discount:",dis)
# print("total:",cp-dis)

# #  05/11/2024
# new sir........

# mystr = "Neeraj"
# print(mystr[:: -1])

# print(mystr[-6:-2:-1])
# print(mystr[1:4:-1])
# s = 'follow'
# print(s[3:8:1])
# s1 = 'medium'
# print(s1[-4:4])
# s3 = 'coder'
# print(s3[1:4:0])  #value error.
# s4 = "neeraj"
# print(s4[-6:-6:1])

#  06/11/2024

# x = range(1,11,1)
# print(list(x))

# x1 = range(-1,-11,-1)
# print(list(x1))

# x2 = range(2,11,2)
# print(list(x2))

# x3 = range(1,11,2)
# print(list(x3))

# x4 = range(19,67,5)
# print(list(x4))

# x5 = range(-5,1,1)
# print(list(x5))

# x6 = range(-3,4)
# print(list(x6))

# x7 = range(-2,3,2)
# print(list(x7))

# x8 = range(-3,4,3)
# print(list(x8))


# x9 = range(3,-4,-3)
# print(list(x9))


# x10 = range(2,-3,-2)
# print(list(x10))


# x11 = range(3,-4,-1)
# print(list(x11))


# x12 = range(3,-1,-1)
# print(tuple(x12))


# slice is inbuilt function 


# 07/11/2024


# control flow

# x  = int(input("enter your number"))
# y  = int(input("enter your number"))

# print("1 add/n  2 sub/n 3.multi/n 4.divide/n")

# n= int(input("please enter your choice"))

# if n==1:
#     print(x+y)
# elif n==2:
#     print(x-y)
# elif n==3:
#     print(x*y)
# elif n==4:
#     print(x/y)
# else:
#     print("you enter wrong number")    

# 08/11/2024

#  WAP to  print natural number upto n.
# n = int(input("enter your number"))
# i=1
# while i<=n:
#     if i<n:
#         print(i,end=",")
#     else:
#         print(i)
#     i = i+1

# even
# n = int(input("enter your number"))
# i=2
# while i<=n:
#     if n%2==0:
#         if i%2==0:
# 02
# n = int(input("enter your number"))
# i=2
# while i<=n:
#     if i%2==0:
#         print(i,end=',')
#     else:
#         print(i)
#     i=i+2

# 03
# n = int(input("enter your number"))
# i=2
# while i<=n*2:
#     if i%2==0:
#         print(i,end=',')
#     else:
#         print(i)
#     i=i+2



# question 1 t0 20 sum
# n=int(input("enter your number"))
# sum=i=2
# while i<=n*2:
#     if i%2==0:
#         print(i,end='+')
#     else:
#         print(i,end="=")
#     sum=sum+i
#     i=i+2
# print(sum)

# # question 1 t0 10 sum
# n = int(input("enter your number"))
# sum=i=2
# while i<=n:
#     if i%2==0:
#         print(i,end='+')
#     else:
#         print(i,end='=')
#     sum=sum+i
#     i=i+2
# print(sum)





# n =  int(input("enter your number"))
# sum=i=0
# while i<=n:
#     if i<n:
#         print(i,end='+')
#     else:
#         print(i,end='=')
#     sum=sum+i 
#     i=i+1
# print(sum)    
#


# n = int(input("enter your number"))
# i=1
# while i<=n:
#     if i<n:
#         print(2*i,end=',')
#     else:
#         print(2*i)
#     i=i+1

# #  for loop((1)print natural number using for loop)
# n=int(input("enter number"))
# for i in range(1,n+1):
#    if i<=(n-1):
#         print(i,end=',')
#    else:
#         print(i)


# sum of natural number

# n=int(input("enter number"))
# sum=0
# for i in range(1,n+1):
#    sum=sum+i
#    if i<=(n-1):
#         print(i,end='+')
#    else:
#         print(i,end='=')
# print(sum)


# # python tutor for print a code line by line

# n= int(input("Enter Your number "))
# sum=0




#13/11/2024 python class

# n = int(input("enter your number"))
# i=0
# while i<n:
#      print(" "*i+"*"*(n-i))
#      i=i+1


# # 

# n = int(input("enter your number"))
# i=0
# while i<=n:
#      print("*"*i)
#      i=i+1

# # 
# n = int(input("enter your number"))
# i=0
# while i<=n:
#      print("*"*(n-i)+" "*i)
#      i=i+1


# # 
# n = int(input("enter your number"))
# i=0
# while i<=n:
#      print(" "*(n-i)+"*"*i)
#      i=i+1

# # 
n = int(input("enter your number"))
i=0
while i<=n:
     print(" "*(n-i)+"* "*i)
     i=i+1
         


# 
# n = int(input("enter your number"))
# i=0
# while i<=n:
#      print(' '*i+"* "*(n-i))
#      i=i+1


# 
# n = 5

# print("Pattern 1")

# for a1 in range (0,n):
#     for a2 in range (a1):
#         print("*", end=" ")
#     print()

# for a1 in range (n,0,-1):
#     for a2 in range (a1):
#         print("*", end=" ")
#     print()


#
# n  = int(input("enter numbre"))
# i=1
# while i<=n:
#      print('*'*i)
#      i=i+1
# # print(i)
# while i>0:
#      print('*'*i +" "*(n-i)) 
#      i=i-1



# # 
# n = int(input("enter your number beta"))
# i=0
# while i<n:
#      print((n-i)*' *')
#      i=i+1
# i=i-2
# while i>=0:
#      print((n-i)*' *')
#      i=i-1

# 
# n = int(input("enter your input beta"))
# i=1
# for i  in  range(i,n+i):
#      print('*'*i)
     

# 
# n = int(input("enter your input beta"))
# i=1
# for i  in  range(i,n+i,2):
#      print('*'*i)

# # 
# n = int(input("enter your input beta"))
# # i=1
# for i  in  range(n,0,-1):
#      print('*'*i)

# for i  in  range(2,n+1):
#      print('*'*i)   
         

#  ascii value  



#  Transfer Statement 
#  continue,break and pass   

# while True:
#      print("1.ADD\n 2.SUB\n 3.MULTI\n 4.DIV\n 10.OFF")
#      n=int(input("enter y0ur choice"))
#      x=[1,2,3,4]
#      if n in x:
#           y=int(input("enteryour 1st number"))
#           z=int(input("enter your number"))
#           if n==1:
#                print("ADD=",y+z)
#           elif n==2:
#                print("sub=",y-z)
#           elif n==3:
#                print("multi=",y*z)
#           elif n==4:
#                print("div=",y/z)
#      elif n==10:
#           break
#      else:
#           print("please enter right choice~ number")

#  18/11/2024

# bitwise operatpor 
# left shift ang rightshift and and operator and or operator 
# that are padhna hai hai ye youtube se  dyan se padhna hai hai yaad rakhna


# n = int(input("Enter the number of terms: "))
# a=0
# b=1
# print("Fibonacci Series:")
    
  
# for _ in range(n):
#         print(a, end=" ")
#         print(b, end=" ")
#         b=a+b
#         a=b
# print(n)
        

# n =int(input("enter the number of"))
# n=n*n
# n=n**10

# print(n)

#  function

# function questions
# def add(x,y):
#     # print(x+y)// they can print none with values
#     return x+y # they can print only the values.
# p=int(input("enter the number"))
# q=int(input("enter the number"))
# num=add(p,q)
# print(num)

# types of argumrnt 
# 1 positional argument
# 2 default arguments

#  20/11/2024
# 3 keyword arguments
#  4 variable length arguments
# def squar (x,y,z):
#     x=x**2
#     y=y**2
#     z=z**2
#     return x,y,z
# p=int(input("enter "))
# q=int(input("enter "))
# r=int(input("enter "))
# a,b,c=squar(z=q,x=r,y=p)

# print(a,b,c)


# def add(*args):
#     print(args)
#     print(type(args))
#     sum=0
#     for x in args:
#         sum=sum+x
#     return sum
# num = add(10,2,22,2,45,67,89)
# print(num)


# #  eval()
# x=eval(input("enter"))
# print(type(x))

# 
# def add(*n):
#     sum=0
#     for i in n:
#         for x in i: 
#             sum=sum+x
#     return sum
# x=eval(input("enter"))
# num = add(x)
# print(num)


#  keyword variables length arguments ->
                                 # *args -> positional arguments
                                     # **kwargs -> keyword arguments
                                    
# y=10
# def show(**n):
#     print(n)
#     x=20
#     for i,j in n.items():
#         print(i,j)
#     print(x,y)
# show(name="mohit",age=23,quality="m.tech")
# print(x,y)


#  Scope
# x=10
# def show():
#     global y
#     y=90
#     print(x)
#     print(y)
# print(x)
# # print(y)
# show()
# print(y)


#  
# x=10
# def show():
#     x=20
#     print(x)
# print(x)


# a = 25
# b = 25
# print(a is b)
# print(id(a))
# print(id(b))


# # 
# my_list = [1,2,3,4,5,6,7,8]
# def square(x):
#     return x**2
# x=map(square,my_list)
# print(x)
# print(tuple(x))


# # 
# my_list = [ 1, 2, 3, 4, 5, 6,8,9]
# def maxdigit(x):
#     if x>=6:
#         return x
# x=filter(maxdigit, my_list)
# print(list(x))


# # 
# import functools
# my_list = [ 1, 2, 3, 4, 5,8,9,10,77,98]
# def max_digit(x,y):
#     if x>y:
#         return x
#     else:
#         return y
# var = functools.reduce(max_digit,my_list)
# print (var)


# import functools
# from functools import reduce
# my_list = [ 1, 2, 3, 4, 5,8,9,10,77,98]
# def min_digit(x,y):
#     if x<y:
#         return x
#     else:
#         return y
# # var = functools.reduce(min_digit,my_list)
# var=reduce(min_digit,my_list)
# print (var)





