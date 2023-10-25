#!/usr/bin/env python
# coding: utf-8

# In[15]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# In[16]:


df=pd.read_csv('ratings.csv')
df.head()


# In[17]:


df.shape


# In[18]:


X = df[['userId', 'movieId']]
y = df['rating']


# In[19]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[20]:


from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X_train,y_train)


# In[21]:


y_pred=model.predict(X_test)


# In[22]:


from sklearn.metrics import mean_squared_error, r2_score
mse=mean_squared_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)


# In[23]:


print(f'mean square error is {mse} and r2 score is {r2}')

mse=20
# In[ ]:




