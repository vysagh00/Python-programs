"""
# n=int(input("No: "))
# d={}
# l=[]
# for i in range(n):
#   w=str(input("str: "))
#   l.append(w)
#   if w in d:
#      d[w] += 1
#   else:
#      d[w] = 1 
# print(len(d))
# print(''.join([str(d[w])for w in d]))
"""


# n = int(input("no: "))
# if n%2==0:
#     if (n>2 and n<5):
#        print("Not Weird")
#     elif (n>6 and n<=20):
#         print("Weird")
#     elif (n>20):
#         print("Not Weird")    
# else:
#     print("Weird")



"""
# import math
# import os
# import random
# import re
# import sys

# def solve(meal_cost, tip_percent, tax_percent):
#     total_cost =  meal_cost + meal_cost * tip_percent/100 + meal_cost * tax_percent/100
#     print(round(total_cost))
    
# if __name__ == '__main__':
#     meal_cost = float(input().strip())
#     tip_percent = int(input().strip())
#     tax_percent = int(input().strip())
#     solve(meal_cost, tip_percent, tax_percent)
"""



# x = int(input("enter "))
# y = int(input("enter "))
# z = int(input("enter "))
# n = int(input("enter "))

# output=[]
# for i in range(x+1):
#     for j in range(y+1):
#         for k in range(z+1):
#             if i+j+k==n:
#                 continue
#             else:
#                 output.append([i,j,k])
    
# print(output)


"""
# import random
# k = random.randint(1,10)

# from random import randint
# l = ["ans","and","are","app"]
# len = len(l)
# k = randint(0,len-1)
# s = " "
# for i in l[k]:
#    if i=="a" or i==" ":
#       s += i
#       s += " "
#       continue
#    s += "_ "
# print(s)
"""


# class Person:
#    age = 0
#    def __init__(self,initialAge):
       
#       if initialAge < 0:
#          print ("Age is not valid, setting age to 0.")
#       else:
#          self.age = initialAge

#    def amIOld(self):
        
#       if self.age < 13:
#          print ("You are young.")
#       elif self.age >= 13 and self.age < 18:
#          print ("You are a teenager.")
#       else:
#          print ("You are old.")

#    def yearPasses(self):
#       self.age += 1
       
# t = int(input())
# for i in range(0, t):
#    age = int(input())         
#    p = Person(age)  
#    p.amIOld()
#    for j in range(0, 3):
#       p.yearPasses()       
#    p.amIOld()
#    print("")



"""
# import math
# import os
# import random
# import re
# import sys


# # if __name__ == '__main__':
# #     n = int(input().strip())
# #     for i in range(1, 11):
# #        print(n,'x',i,'=',n*i)
# """



# T = int(input())

# for i in range(0,T):
#     S = input()
#     print(S[0::2]+" "+S[1::2])


"""
# import math
# import os
# import random
# import re
# import sys


# if __name__ == '__main__':
#     n = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))
    
#     m = map (str,arr[::-1])
#     print (" ".join(m))

"""


# phonebook = {}
# entries = int(input())

# for n in range(entries):
#     name, num = input().strip().split(' ')
#     name, num = [str(name), int(num)]
#     phonebook[name] = num

# while True:
#     try:  
#         search = str(input())

#         if search in phonebook:
#             output = ''.join('%s=%r' % (search, phonebook[search]))
#             print(output)
#         else:
#             print ("Not found")
#     except EOFError:
#         break


"""
# import math
# import os
# import random
# import re
# import sys

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         n = n * factorial(n-1)
#     return n

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#     n = int(input())
#     result = factorial(n)
#     fptr.write(str(result) + '\n')
#     fptr.close()
"""