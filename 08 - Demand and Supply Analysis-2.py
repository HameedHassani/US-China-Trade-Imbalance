#!/usr/bin/env python
# coding: utf-8

# In[1]:


# I would like to analyze U.S.'s' oil supply and demand

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import statsmodels.api as sm
pio.templates.default = 'plotly_white'


# In[2]:


data = pd.read_csv('/Users/hhassani/Downloads/Supply_Demand_Oil.csv')


# In[3]:


pd.set_option('display.max_columns', None)
data.head()


# In[4]:


# First, I want to look at the relation between U.S. oil supply and demand

us_oil_demand = data['U.S. (50 States) Total Demand']
us_oil_supply = data['U.S. (50 States) Total Supply']

figure = px.scatter(data, x = us_oil_demand, y = us_oil_supply, trendline ='ols')
figure.update_layout(
    xaxis_title ='U.S. Oil Demand',
    yaxis_title ='U.S. Oil Supply',
    title = {'text':'U.S. Oil Supply and Demand 1994 - 2019 (million barrels per day)',
            'x' : 0.5,
            'y' : 0.95})

figure.show()


# In[5]:


# Now, I want to assess if there is any relationship between U.S. oil supply 
# and total world demand for oil
    
world_oil_demand = data['Total World Demand']
world_oil_demand = sm.add_constant(world_oil_demand)

model = sm.OLS(us_oil_supply, world_oil_demand).fit()
model.summary()


# In[6]:


# The model is indicative of a relationship between U.S. oil supply and world oil demand
# U.S. oil supply doubles as world demand increase by 20% and it is statistically significant
# Figure below visualizes this relationship

fig = px.scatter(data, x =  'Total World Demand', y = 'U.S. (50 States) Total Supply', title = 'World Oil Demand and U.S. Oil Supply', trendline = 'ols')
fig.update_layout(title_x=0.5, title_y=0.9)
fig.show()


# In[7]:


# World oil demand and U.S. oil demand relationship

fig = px.scatter(data, x =  'Total World Demand', y = 'U.S. (50 States) Total Demand', title = 'World Oil Demand and U.S. Oil Demand', trendline = 'ols')
fig.update_layout(title_x=0.5, title_y=0.9)
fig.show()


# In[8]:


# U.S. oil demand in light of world supply & demand

fig = px.scatter(data, x =  'Total World Demand', y = 'U.S. (50 States) Total Demand',color = 'Total World Supply', title = 'World Oil Demand and U.S. Oil Demand/Supply', trendline = 'ols')
fig.update_layout(title_x=0.5, title_y=0.9)
fig.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




