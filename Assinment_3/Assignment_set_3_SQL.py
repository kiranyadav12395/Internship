#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Connecting with database.
# if there is no database exist, it will create one. 

import sqlite3
db = sqlite3.connect("Modelcars_database.db")


# In[2]:


cursor = db.cursor()


# In[3]:


# Ans no:-1

cursor.execute("create table customers_db(customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, addressline2, city, state, postalCode, country, salesRepEmployeeNumber, creditLimit)")


# In[4]:


# Ans no:-2

cursor.execute("create table Orders_db(orderNumber, orderDate, requiredDate, shippedDate, status, comments, customerNumber)")


# In[5]:


with open ('Orders_data.csv', 'r') as file:
    no_records = 0
    for row in file:
        cursor.execute("insert into Orders_db values (?, ?, ?, ?, ?, ?, ?)", row.split(","))
        db.commit()
        no_records+=1
print(no_records, 'records inserted')  


# In[6]:


# Ans No:- 3

results = cursor.execute("select * from Orders_db")
for row in results:
    print(row)


# In[7]:


# Ans No:- 4

comments = cursor.execute("select comments from Orders_db")
for row in comments:
    print(row)


# In[8]:


# Ans No:- 5

order_table = cursor.execute("select orderNumber, orderDate from Orders_db")
for row in order_table:
    print(row)


# In[9]:


cursor.execute("create table employees_db(employeeNumber, lastName, firstName, extension, email, officeCode, reportsTo, jobTitle)")


# In[10]:


with open ('Employee_data.csv', 'r') as file:
    no_records = 0
    for row in file:
        cursor.execute("insert into employees_db values (?, ?, ?, ?, ?, ?, ?, ?)", row.split(","))
        db.commit()
        no_records+=1
print(no_records, 'records inserted')        


# In[11]:


# Ans No:- 6

comments = cursor.execute("select employeeNumber, lastName, firstName from employees_db")
for row in comments:
    print(row)


# In[12]:


with open ('Customers_data.csv', 'r') as file:
    no_records = 0
    for row in file:
        cursor.execute("insert into customers_db values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", row.split(","))
        db.commit()
        no_records+=1
print(no_records, 'records inserted')        


# In[13]:


# Ans no:- 8

results = cursor.execute("select customerName, salesRepEmployeeNumber from customers_db")
for row in results:
    print(row)


# In[14]:


cursor.execute('create table payments_db(customerNumber, checkNumber, paymentDate, amount)')


# In[16]:


with open ('Payments_data.csv', 'r') as file:
    no_records = 0
    for row in file:
        cursor.execute("insert into payments_db values (?, ?, ?, ?)", row.split(","))
        db.commit()
        no_records+=1
print(no_records, 'records inserted')     


# In[17]:


# Ans no:- 9

results = cursor.execute("select paymentDate, amount from payments_db")
for row in results:
    print(row)


# In[18]:


cursor.execute("create table products_db(productCode, productName, productLine, productScale, productVendor, productDescription, quantityInStock, buyPrice, MSRP)")


# In[19]:


with open ('Products_data.csv', 'r') as file:
    no_records = 0
    for row in file:
        cursor.execute("insert into products_db values (?, ?, ?, ?, ?, ?, ?, ?, ?)", row.split(","))
        db.commit()
        no_records+=1
print(no_records, 'records inserted')  


# In[20]:


# Ans no:- 10

results = cursor.execute("select productName, MSRP, productDescription from products_db")
for row in results:
    print(row)


# In[21]:


# Ans no:- 14

comments = cursor.execute("select employeeNumber, lastName, firstName from employees_db")
for row in comments:
    print(row)


# In[ ]:




