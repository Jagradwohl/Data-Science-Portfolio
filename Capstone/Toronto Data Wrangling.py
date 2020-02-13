#!/usr/bin/env python
# coding: utf-8

# In[22]:


#import libraries and using beautiful soup to scrape the wikipedia page
import pandas as pd
import numpy as np 
import csv
import requests
from bs4 import BeautifulSoup
get_ipython().system('conda install beautifulsoup4')


# In[47]:


#you have to set the column width before you read into the file to get the complete column
pd.set_option('max_colwidth', 800) 


# In[48]:


#Bring the webpage in
Page = requests.get('https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M').text 
soup = BeautifulSoup(source, 'lxml')


# In[49]:


# We are creating a CSV file out of the webpage with the command csv_writer 
csv_file = open('toronto_postal_codes.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Postcode', 'Borough', 'Neighbourhood'])


# In[50]:


#Scrap the page to set up and initialize your table. 
#This is the core of manipulating the data once we've brought it in as a csv
#soup.find brings our table in from wikipedia. 
table = soup.find('table', class_ = 'wikitable sortable')  
rows = table.find_all('tr') 

postcodes = [] 
boroughs = [] 
neighbourhoods = [] 
#We need a for/if statement that helps us remove the rows where the borough name is not assigned
for row in rows:    
    columns = row.find_all('td')
    try :
        if columns[1].text != 'Not assigned':  
            
            postcode = columns[0].text
            postcodes.append(postcode)
            borough = columns[1].text
            boroughs.append(borough)
            neighbourhood = columns[2].text.split('\n')[0]     
            
            if neighbourhood == 'Not assigned': 
                neighbourhood = borough            
                neighbourhoods.append(neighbourhood)
             
    except Exception as e : 
        pass 
postcode_explored = [] 
# we need another for / if loop to help combine the neighborhood names into the same postcode (index)
for index_i, postcode_i in enumerate(postcodes) :   
    if postcode_i not in postcode_explored :
        nbds = neighbourhoods[index_i]
        for index_f, postcode_f in enumerate(postcodes) :
            if postcode_i == postcode_f and index_i != index_f:
                nbds = nbds + ', ' + neighbourhoods[index_f]
        csv_writer.writerow([postcode_i, boroughs[index_i], nbds]) 
        postcode_explored.append(postcode_i)


# In[51]:


csv_file.close()


# In[55]:



df_tot.head()


# In[54]:


df_tot=pd.read_csv('toronto_postal_codes.csv')
df_tot.shape

