#  even and odd.
# for i in range(21):
#  while i %2==0:
#      print(i)
#      i=i+1

# for i in range(21):
#  while i %2==1:
#      print(i)
#      i=i+1

# first 10 integers with their square.
# num=1
# print("integer\t\t square")
# while num<=10:
#     print(num,"\t\t",num**2)
#     num=num+1
# i=1
# num=int(input("enter the number here:"))
# while i<=10:
#     print(num,"*",i,"=",num*i)
#     i=i+1

# print number in increment series
# a=0
# while(a >=10):
#     print(a,"\n")
#     a=a+1
# # print number in increment series
# a=10
# while(a >=0):
#     print("\n",a)
#     a=a-1

# number to name program:
# num=(input("enter the number here:"))
# l1=list(num)
# l=len(l1)
# i=0
# n={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten"}
# while(i<l):
#     print(n[int(l1[i])],end="")
#     i=i+1
# factorial
# num=int(input("enter the number here:"))
# i=1
# f=1
# while(i<=num):
#     f=f*i
#     i=i+1
#     print("the factorial of number is",f)
#     if(i!=1):
#      print("factorial of 0 is 1:")    
    
# sum of numbers user entered.
a='Y'
sum=0
while a.upper()=='Y':
 num=int(input("enter the number here:"))
 sum=sum+num
 a=input("you want to continue (Y/N)?:")
print(sum)