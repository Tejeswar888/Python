# generators
# (expr for var in collection/range)
'''a = (i for i in range(21))
print(a)
print(*a)
print(type(a))'''

#(expr for var in collection/range)
'''a=(i for i in range(21))
print(a)
print(*a)
print(type(a))'''

# (expr for var in collection/range)
'''a = (i for i in range(21))
print(a)
print(*a)
print(type(a))'''

# print(list(a))

# print(tuple(a))

#print(set(a))

'''a,b=(int(x) for x in input("enter the values")
    .split(","))
def check(a,b):
    while a<b:
        yield a
        a=a+1
        yield a
Print(*check(a,b))'''

'''a,b=(int(x) for x in input("enter the values")
    .split(","))
def check(a,b):
    while a<b:
        a=a+1
        return a
print(check(a,b))'''

'''#yield v/s return
def mygen():
    #return "vja"
    #return "hyd"
    #return "vzg"
    return "vja","hyd","vzg"
print(*mygen())'''

'''def mygen():
    yield "python"
    yield "java"
    yield "DSA

print(*mygen())'''

# next()
'''d = mygen()
print(next(d))
print(next(d))
print(next(d))
# print(next(d)) stop iteration'''

#Patterns

'''1)row = int(input("Enter the number of rows:"))

for i in range(row, 0, -1):
    for j in range(i):
        print("*", end="")
    print()
o/p:
Enter the number of rows:6
******
*****
****
***
**
*  '''

 #2.solid square pattern
'''N rows(outer loop), N cols(inner loop)

row col 1 2 3 4 5
    1   * * * * *
    2   * * * * *
    3   * * * * *
    4   * * * * *
    5   * * * * *

code:
N = int(input('N= '))

for row_num in range(1, N+1):
    for col_num in range(1, N+1):
        print("*",end=" ")
    # new row, new line
    print()'''

'''#3
n=int(input("enter the value:"))
for i in range(1,n+1):
    print(" "*(n-i)+"*"*(2*i-1))
o/p:
enter the value:6
     *
    ***
   *****
  *******
 *********
***********'''

'''#4
a=int(input("enter the rows"))
for i in range(1,a+1):
    print(" "* (a-i),end="")
    print("* "*i)
    o/p:
    enter the rows 6
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
* * * * * * '''
