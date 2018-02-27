
# coding: utf-8

# In[4]:

#Part 1
#Write a Python Program to implement your own myreduce() function which works exactly like Python's built-in function reduce()
a = [1,2,3,4]
b = [5,6,7,8]
c = [9,10,11,12]
lst=[]
#print len(a)
#for index, elem in enumerate(a):
      #  print(index, elem)
    
for index in range(len(a)):
    num = a[index] + b[index] + c[index]
    lst.append(num)
    
print(lst)    


# In[9]:

#First let's make a function
def even_check(num):
    if num%2 ==0:
        return True
#Using filter method
lst =range(20)
print(lst)
print (list(filter(even_check,lst)))

#Write a Python program to implement your own myfilter() function which works exactly like Python's built-in function filter()
evenLst=[]
numlst=range(0,20)
print (numlst)
for i in numlst:
    if i%2 == 0:
        evenLst.append(i)
        
print(evenLst)        



# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



