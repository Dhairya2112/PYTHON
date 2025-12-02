#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a=30
b=10
c=30
d="hello"
if (a==b):
    print("-"*60)
    print("operations")
    print(a or b)
    print(0 or a) 
    print(a and b)
    print(d or 0)
    print("-"*60)
elif (a==c):
    print("he" in d)
    print(a is c)
else:
    print("bye")


# In[ ]:


x=int(input("Enter no. f days to convert:"))
print(f"for {x} days will be {x//360} year {(x%360)//30} month {(x%30)%30} days")


# In[ ]:


a=int(input("Enter number to sum:"))#123
z=a//10   #12
x=a%10    #3
w=z//10   #1           
y=z%10    #2
print(f"for {y} number sum will be {y+x+w}")


# In[ ]:


x=int(input("Enter number:"))
z=x%10
if(z==0):
    print("zero")
elif (z==1):
    print("one")
elif (z==2):
    print("two")
elif (z==3):
    print("three")
else:
    print("number is not =0,1,2,3")


# In[ ]:


x=int(input("Enter number of amount:"))
a=x//50
b=x%50
c=b//20
d=b%20
e=d//10
print(f"50={a},20={c},10={e}")


# In[ ]:


x1=int(input("Enter IN hour:"))
x2=int(input("Enter IN min:"))
x3=int(input("Enter IN sec:"))
x4=int(input("Enter out hour:"))
x5=int(input("Enter out min:"))
x6=int(input("Enter out sec:"))

if(x1==x4 and x2==x5 and x3==x6):
    print("entry and exit cannot be same")
else:
    a=x1*60
    b=x4*60
    c=x3//60
    c1=c%60
    d=x6//60
    d1=d%60
    print("total mins for in time=",(a+x2+c))
    print(f"total sec of in time={c1}")
    print("total mins for out time=",(b+x5+d))
    print(f"total sec of in time={d1}")


# In[ ]:


for i in range(1,11):
    if (i%2==0):
        print("even=",i)
    else:
        print("odd=",i)


# In[ ]:


x1=int(input("Enter number to multiply:"))
print(f"table for {x1}")
for i in range(1,11):
    if (x1>=0):
        print(f"{x1}*{i}=",x1*i)
    else:
        print("enter valid name")


# In[ ]:


x1=int(input("Enter number to multiply:"))
print(f"table for {x1}")
for i in range(10,0,-1):
    if (x1>=0):
        print(f"{x1}*{i}=",x1*i)
    else:
        print("enter valid name")


# In[ ]:


for i in range(1,11):
    if (i==3 or i==6):
        continue
    else:
        print(i)


# In[ ]:


x1=int(input("Enter number:"))
sum=0
while x1>0:
    digit=x1%10
    sum=(sum*10)+digit
    x1=x1//10
print(f"reversed number=",sum)


# In[ ]:


x1=int(input("Enter number:"))
sum=0
while x1>0:
    digit=x1%10
    sum=sum+digit
    x1=x1//10
print(f"sum of number=",sum)


# In[ ]:


x1=int(input("Enter number:"))
sum=0
while x1>0:
    digit=x1%10
    sum=sum+(digit**3)
    x1=x1//10
print(f"sum of cube of number=",sum)


# In[ ]:


x1=int(input("Enter number:"))
sum=0
temp=x1
while x1>0:
    digit=x1%10
    sum=sum+(digit**3)
    x1=x1//10
    
print(sum)
if(sum==temp):
    print(f"yes it is an armstrong number")
else:
    print("no it is not")


# In[ ]:


x1=int(input("Enter number:"))
sum=0
temp=x1
last=x1%10
first=0
middle=0
c=0
while x1>0:
    c=c+1
    digit=x1%10
    first=digit
    x1=x1//10
    middle=(temp%10**(c-1))//10
    swap=((last*10**(c-1))+(middle*10)+first)
print(f"first=",first)
print(f"last=",last)
print("middle=",middle)
print("swap of first and last number="swap)


# In[ ]:


x1=int(input("Enter number:"))
temp=x1
c=0
while x1>0:
    c=c+1
    x1=x1//10
    second=(temp//10**(c-2))
print("first 2 number is",second)


# In[ ]:


x1=int(input("Enter number:"))
sum=0
temp=x1
c=0
while x1>0:
    x1=x1//10
    c=c+1
while temp>0:
    digit=temp%10
    sum=sum+(digit**c)
    temp=temp//10
print(f"sum of cube of number in base of count=",sum)


# In[ ]:


s=0
c=0
while True:
    n=input("Enter number or press q for exit=")
    if n=='q'or n=='Q':
        break
    else:
        n=int(n)
        s=s+n
        c=c+1
print(f"sum of numbers is {s} and count is {c} so the avg is {s/c}")


# In[ ]:


s1=0
s2=0
c1=0
c2=0
while True:
    n=input("Enter number or press q for exit=")
    if n=='q'or n=='Q':
        break
    else:
        n=int(n)
        if n%2==0:  
            s1=s1+n
            c1=c1+1
        else:
            s2=s2+n
            c2=c2+1
print(f"sum of numbers of even={s1} odd={s2} and count of even={c1} odd={c2} so the avg of even={s1/c1} odd={s2/c2}")


# In[ ]:


max1=0
min1=1000000000001
while True:
    n=input("Enter number or press q for exit=")
    if n=='q'or n=='Q':
        break
    else:
        n=int(n)
        if n>max1: 
            max2=max1
            max1=n
        elif n>max2 and n!=max1:
            max2=n
        if n<min1:
            min2=min1
            min1=n
        elif n<min2 and n!=min1:
            min2=n
print(f"max number is {max1} and min number is {min1}")
print("  ")
print(f"2nd max number is {max2} and 2nd min number is {min2}")


# In[ ]:


max1=0
min1=1000000000001
while True:
    n=input("Enter number or press q for exit=")
    if n=='q'or n=='Q':
        break
    else:
        n=int(n)
        if n%2==0:
            if n>max1: 
            max2=max1
            max1=n
        elif n>max2 and n!=max1:
            max2=n
        if n<min1:
            min2=min1
            min1=n
        elif n<min2 and n!=min1:
            min2=n
        else:
            if n>max1: 
                max2=max1
                max1=n
            elif n>max2 and n!=max1:
                max2=n
            if n<min1:
                min2=min1
                min1=n
            elif n<min2 and n!=min1:
                min2=n
print(f"max number is {max1} and min number is {min1}")
print("  ")
print(f"2nd max number is {max2} and 2nd min number is {min2}")


# In[ ]:


d=int(input("Enter day="))
m=int(input("Enter month="))
y=int(input("Enter year="))
print(f"your input {d}/{m}/{y}")
if m==12 and d==31:
    d=1
    m=1
    y=y+1
elif (d==31 and ((m==1)or(m==3)or(m==5)or(m==7)or(m==8)or(m==10)or(m==12))):
    m=m+1
    d=1
elif (d==30 and ((m==2)or(m==4)or(m==6)or(m==9)or(m==11))):
    d=1
    m=m+1
elif (m==2 and (d==28 or d==29)):
    if ((y%400==0)or(y%100==0) and (y%4==0)):
        if d==28:
            d=d+1
        else:
            d=1
            m=m+1
    else:
        d=1
        m=m+1
else:
    d=d+1
print(f"next predicted date is {d}/{m}/{y}")


# In[ ]:


def demo(a=10,b=20):
    print(a+b)
    return a,b
demo()


# In[ ]:


x=int(input("Enter your number="))
def check_even(a):
    if(a%2==0):
        return "even number"
    else:
        return "odd number"
c=check_even(x)
print(c)


# In[ ]:


def multi(a):
    while(a>0):
        sum1=1
        digit=a%10
        sum1=sum1*digit
        a=a//10
    return sum1
x=int(input("Enter your number="))
c=multi(x)
print(c)


# In[2]:


def multi(a,*b):
        sum1=0
        a=10
        print(a)
        for i in b:
            s=a+i
        print(s)
        
multi(1,2,3,4)


# In[49]:


n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()


# In[20]:


n=4
for i in range(1,n+1):
    for j in range(i,n+1):
        print("*",end=" ")
    print()


# In[29]:


n=4
for i in range(1,n+1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()


# In[33]:


n=4
for i in range(n,0,-1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()


# In[34]:


n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end=" ")
    print()


# In[35]:


n=4
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()


# In[36]:


n=4
for i in range(1,n+1):
    for j in range(i,n+1):
        print(j,end=" ")
    print()  


# In[42]:


n=4
for i in range(1,n+1):
    for j in range(i):
        if i%2==0:
            print("*",end=" ")
        else:
            print("#",end=" ")
    print()


# In[ ]:




