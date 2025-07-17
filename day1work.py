#!/usr/bin/env python
# coding: utf-8

# In[40]:


a=3
print(type(a))


# In[41]:


a=3.5
print(type(a))


# In[42]:


a=True
print(type(a))


# In[43]:


a=3
print(str(a))


# In[44]:


a=3
b=str(a)
print(type(b))


# In[ ]:


#arithmetic operator 


# In[ ]:


+,-,*,/,%,//,**


# In[45]:


a=int(input("enter the no"))
b=int(input("enter the no 2"))
c= a + b
print(c)


# In[1]:


a=int(input("enter the no"))
b=4
c= a + b
print(c)


# In[2]:


a=3
b=4
print(a+b)


# In[46]:


a=3
b=4
print(a+b)


# In[3]:


a=int(input("enter the no"))
b=int(input("enter the no 2"))
c= a + b
print(c)


# In[4]:


#comparison operator 


# In[ ]:


<,>,<=,>=,==


# In[6]:


a=10
b=12
print(a>b)


# In[7]:


a=int(input("enter a no"))
b=int(input("enter a no"))
print(a>b)


# In[8]:


a=float(input("enter a no"))
b=float(input("enter a no"))
print(a>b)


# In[10]:


a=int(input("enter a no"))
b=int(input("enter a no"))
print(a==b)


# In[11]:


a=int(input("enter a no"))
b=int(input("enter a no"))
print(a>=b)


# In[15]:


x=int(input("enter a no :"))
y=int(input("enter another no :"))
z=int(input("enter another no :"))
sum=x+y+z
print(sum)
avg=sum/3
print(avg)
print(avg>50)
print(sum/5)


# In[18]:


#logical operators


# In[ ]:


and,or,not


# In[20]:


print(a>b and a==b)


# In[26]:


print(a>b or a==a)


# In[25]:


a=3
b=4
print(not a>b)


# In[27]:


a=3
b=3
print(not a==b)


# In[ ]:


#membership operator


# In[ ]:


in,not in


# In[32]:


a=[2,4,3,5]
for x in a:
    print(x)


# In[33]:


a="python is imp"
print("is" in a)


# In[34]:


a="python is imp"
print("is" not in a)


# In[39]:


a=2
b=10
print(a is not b)


# In[36]:


num1=int(input("enter a no"))
num2=int(input("enter another no"))
sum=num1+num2
mul=num1*num2
print(sum)
print(mul)
print(num1==num2)
print(num1>num2)
a=[10,20,30,40,50]
print(num1 in a)
print(num2 in a)
for x in a:
    print(x)


# In[37]:


a=2
b=2
print(a is b)


# In[47]:


#bitwise operator


# In[ ]:


&,~,|

