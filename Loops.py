"""                           LOOPS 
                        Loops are two types        """

                        # 1. While Loops
                        # 2. For While Loops


#While Loops:- wap to print "Hello" Five time.
"""i = 1
while i<=5:
    print("Hello")
    i +=1"""

  
"""Q). print numbers from 1 to 100.
i = 1
while i<=100:
    print(i)
    i +=1"""

"""Q). print numbers from 100 to 1.
i = 100
while i>=1:
    print(i)
    i -=1"""

"""Q). print the multiplication table of a number n.
n = 3
i = 1
while i<=10:
    print(n*i)
    i +=1"""

"""Q). print the element of the following list using a loop.
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
i = 0
while i <len(list):
    print(list[i])
    i+=1"""

"""Q). search for a number X in this tuple using loop.
tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
i = 0
X = int(input("enter you number: "))
while i < len(tuple):
    if( X ==tuple[i]):
     print( "number is find", i)
    else:
       print("not fund")
    
    i+=1"""


# Break 
"""tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
i = 0
X = int(input("enter you number: "))
while i < len(tuple):
    if( X ==tuple[i]):
     print( "number is find", i)
     break
    else:
       print("not fund")
    
    i+=1"""


#Continue 
"""i = 0
while i <=5:
    if (i==3):
        i+=1
        continue #skip
    print(i)
    i +=1 """



#Do-While Loops:- loops are used for sequential traversal. for traversing list, string, tuples etc.

"""Q1). print the elements of the following list using a loop.
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for el in list:
    print(el)"""

"""Q2). search for a number x in this tuple using loop.
tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = int (input("enter your number: "))
idx = 0
for number in tuple:

    if (x ==  number):

       print("number found at index:", idx)
    idx +=1"""

#Range()
"""for el in range(5): #stop
    print(el)"""

"""for el in range(1, 5): #start, stop
    print(el)"""

"""for el in range(1, 5, 2): #start, stop, step
    print(el)"""

"""Q1). print number from 1 to 100.
for el in range(1, 101):
    print(el)"""

"""Q2). print number from 100 to 1.
for el in range(100, 0, -1):
    print(el)"""

"""Q3). print the multiplication table of a number n.
n = int(input("enter your number: "))
for i in range(1, 11):
    print(n *i)
 """

# Let's Practice:-
"""Q1). WAP to find the sum of first n number.(using while).
n = int (input("enter your number: "))
sum = 0
i = 1
while (i <= n):
      sum +=i
      i +=1

print ("total sum:", sum)    """ 

"""Q2)> WAP to find the factorial of first n number. (using for)
n = int (input("enter your number: "))
fac = 1
for n in range(1, n+1):
      fac *=n
     

print(fac)"""
      