print("helloworld")
name='sami'
print(name.capitalize())
print(len(name))
print(name.isalpha())#let
print(name.isdigit())
print(name.isalnum()) # lettes +numbers
#cheks not captial letter
print(name.islower())
#cheks capital letter
print(name.isupper())




is_completed =True
print(type(is_completed))
print(type(name))
#premivtie data type

def Add(a,b):
    return a+b

sum= Add(5,6)
print("the sum is ", sum)

#pep python enchanement propsoal 

#datastructure
# list 
students=['hana','abebe','alex','sami','miki',7,9,True]


def check_password(pas):
    if len(pas) < 8:
        print("Password too short")
    if pas.islower(): 
        print("Password needs an uppercase ")
    if pas.isupper():
        print("Password needs alowercase ")
    if pas.isalpha():
        print("Password needs a number")
    else:
        print("Password is strong")

#pass 
   

#input acccptor
#password = input('Enter the password :  ')
#check_password(password)

#fizz bz
 

def check_fizz_bzz(a):
    if a%3==0 and a%5==0:
        print("FizzBuzz")
    elif(a%3==0):
        print("Fizz")
    elif(a%5==0):
        print("Buzz")
    else:print("none")



#number  = input('Enter the numberr :  ')
#number_int = int(number)
#check_fizz_bzz(number_int)


def cheker(num):
    if (num % 2 != 0):
        print("werid  and odd")
    elif(num%2 ==0 and 2<num and num<5):
        print("not werid  ")
    elif(num%2 ==0 and 6<num and num <20):
        print("werid 6 to 20")
    elif(num%2 ==0 and num> 20):
        print("not weid")
    

# number1  = input('Enter the numberr :  ')
# numch = int(number1)
# cheker(numch)

# def show(a,b):
#     print(a+b)
#     print(a-b)
#     print(a*b)

# show (9,10)


