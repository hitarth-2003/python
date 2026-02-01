#print first 10 natural number
# "for i in range (10):
#     print("i+1)

# row=5
# for i in range(1,row+1,1):
#     for j in range(1,i+1):
#      print(j,end='*')
#     print("*")

#print multiplication table:
# a=int(input("enter the number here:"))
# for i in range(10):
#     i= i+1
#     print(a," * ",i, "=",a*i)

# display number from -10 to -1
# 
# print elements present at odd index
# a=[1,2,3,4,5,6,7,8,9,10]
# for i in a[1::2]:
#   print(i)

# factorial
a=int(input("enter the numbetr here:"))
factorial=1
if a<0:
    print("number not exist:")
elif a==0:
    print("factorial of 0 is 1:")
else:
    for i in range(1,a+1):
     factorial = factorial * i
    print(factorial)