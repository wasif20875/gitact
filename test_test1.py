#!/usr/bin/env python
# coding: utf-8

# In[4]:


from slr import *


# In[7]:


mse


# In[6]:


import pytest


# In[8]:

def test_min_score():
    assert r2<=0.0018222242743777262 and mse<=1.098036313363161

if __name__=="main":
    test_min_score()
