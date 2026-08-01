#Exception Handling
#1.try
#2.except
#3.else
#4.finally

#try
'''Insructions from which we are expecting the exceptions.'''
#except
'''Exceptions are raised in try block it will handle by this block.'''
#else
'''optional(No Exceptions)'''
#finally
'''Always it will display.'''

'''while True:
    try:
        a=int(input("a value"))
        b=int(input("b value"))
        c=a//b
        print(c)
    except:
        print("exception is raised")
    else:
        print("no exceptions")
    finally:
        print("program ends")

#exception expressions(regex)'''

#regular expressions(regex)
'''a="codegnan is in vja"
print(a)'''

'''a="codegnan\nis\tin\nvja"
print(a)'''

#rstring
'''a=r"codegnan\nis\tin\nvja"
print(a)'''

#compile(),search(),findall(),split(),sub()

#sequence characters
'''\w->it matches alphanumeric
\W->it matches non-alphanumeric
\d->it matches any digit
\D->it matches non-digit
\s->it reprsents white spaces
\S->it represents non-white spaces'''

#compile()
import re
a="mat map cap cup money cash cat dog mug donkey maths"
'''b=re.compile(r"m\w\w\w\w")
print(b)

#search()
c=b.search(a)
print(c)'''

'''c=re.search(r"m\w+",a)
print(c)'''

#findall()
'''d=re.findall(r"m\w+",a)
print(*d) '''

#split()
'''e=re.split(r"m",a)
print(e)

f=re.split(r"\s",a)
print(f) '''

#sub()
'''g=re.sub(r"m","a",a)
print(g)'''

'''c="year 2026 month 7 date 30"
d=re.findall(r"\d",c)
print(d)

c="year 2026 month 7 date 30"
d=re.findall(r"\d+",c)
print(d)
c="year 2026 month 7 date 30"
d=re.findall(r"\D+",c)
print(d)'''
