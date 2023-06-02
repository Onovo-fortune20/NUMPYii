#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
data = {'County': ['Montgomery', 'Prince George', 'Baltimore', 'Anne Arundel', 'Baltimore City','Howard', 
                   'Frederick',  'Hartford', 'Carroll', 'Charles', 'Washington', 'St. Mary', 'Wicomico', 'Ceil'],
'2022 Pop': [1080, 988, 864, 598, 579, 341, 279, 264, 174, 170, 156, 116, 105, 104],
'2021 Pop': [1054, 955, 849, 590, 576, 335, 280, 263, 174, 169, 155, 114, 104, 104]}
MD_POP = pd.DataFrame(data)

frame


# In[6]:


MD_POP.iloc[[0, 1, 2, 3, 4]]


# In[ ]:


MD_POP['Pop increase'] = df.apply(lambda x: x['2022 Pop'] - x['2021 Pop'], axis=1)
df


# In[ ]:


MD_POP.sort_values(by = ['Pop increase'], ascending = False)


# In[ ]:




