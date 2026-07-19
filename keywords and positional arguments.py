# keyword and positional arguments
'''def Details(id, name, mailid):
    id = 10
    name = "pooja"
    mailid = "pooja@codegnan.com"
    print(id, name, mailid)


Details(id="id", name="name", mailid="mailid")'''

'''def Details(id, name, mailid):
    print(id, name, mailid)

Details(id="id", name="name", mailid="mailid")
Details(id=20, name="bhanu", mailid="b@gmail.com")
Details(id=30, name="nayana", mailid="n@gmail.com")
Details(40, "chethana", "c@gmail.com")
Details("h@gmail.com", 50, "harika")
Details(mailid="k@gmail.com", id=60, name="kavya")'''

#default arguments
'''def Grocery(item,price):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("rice",1500)'''

'''def Grocery(item="sugar",price=100):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery() '''

'''def Grocery(item,price=200):
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery("dhal")'''

'''def Grocery(item="ghee",price):
    #non def arg follows def arg
    print("item is %s" %item)
    print("price is %.2f" %price)
Grocery(500)'''

#cake_name,price,qty

# * arguments(* is used to unpack the elements)
'''a=[10,20,30,40,50]
print(a)
print(*a)'''

'''b=(5,6,7,8,9,10)
print(b)
print(*b)'''

'''c={6,7,8,9,10}
print(c)
print(*c)'''

'''d={"name":"pooja","year":2026,"month":7}
print(d)
print(*d)'''

'''a = "codegnan"
print(a)
print(*a)'''

'''a, b, c = 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
print(a)
print(b)
print(c)  # error'''

'''a, b, c = 3, 4, 5
print(a)
print(b)
print(c)'''

'''a,*b,c=2,3,4,5,6,7,8,9,10,11
print(a)
print(*b)
print(c)'''

'''a,b,*c=2,3,4,5,6,7,8,9,10,11
print(a)
print(b)
print(*c)'''

'''a,b,c="codegnan"
print(a)
print(b)
print(c)'''  #error

'''a,b,c="cod"
print(a)
print(b)
print(c)'''

'''a,b,*c="codegnan"
print(a)
print(b)
print(*c)'''
