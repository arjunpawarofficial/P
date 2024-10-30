"""  Strings and Conditional Statements

        Escape sequence Characters, Basic Operations, Indexing and Slicing.  """


#Next line

str1 = "This is my first Strings.\nThis is the python language."
print(str1)

#Tab

str2 = "This is my first Strings.\tThis is the python language."
print(str2)



"""Basic Operation"""

#Concatenation:- Add of two strings

str3 = "Arjun"
str4 = "Pawar"
print(str3+ " " +str4)

#Length of str 

str3 = "Arjun"
len3 = len(str3)
print(len3)

str4 = "Pawar"
len4 = len(str4)
print(len4)


#Indexing

str5 = "Arjun Pawar"
ch = str5[0]
print(ch)

#Slicing

str6 = "Arjun Pawar"
ch = str6[1:4]
print(ch)

# Negaive index Slicing

str7 = "arjun Pawar"
ch = str7[-7:-1]
print(ch)

#Ends With (checker)
print(str7.endswith("ar"))

#Cpitalize
print(str7.capitalize())