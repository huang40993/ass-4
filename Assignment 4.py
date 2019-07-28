#!/usr/bin/env python
# coding: utf-8

# In[43]:


# Name: Baicheng Huang
# Class: Mac281.7828
# Date: 07/28/2019

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node('catherine', Location = (5, 5))
G.add_node('Angela', Location = (4, 6))
G.add_node('Fiona ', Location = (4, 4))
G.add_node('Denny', Location = (3, 5))
G.add_node('Beverly', Location = (2, 6))
G.add_node('Gray', Location = (2, 4))
G.add_node('Emma', Location = (1, 5))
G.add_node('Henley', Location = (3, 3))
G.add_node('Ivan', Location = (3, 2))
G.add_node('Jenny', Location = (3, 1))
G.add_edges_from([  ('catherine', 'Angela'), ('catherine', 'Fiona '), ('catherine', 'Emma'),
                    ('Angela', 'Fiona '), ('Angela', 'Denny'), ('Angela', 'Beverly'),
                    ('Beverly', 'Denny'), ('Beverly', 'Gray'), ('Beverly', 'Emma'),
                    ('Fiona ', 'Denny'), ('Fiona ', 'Henley'), ('Fiona ', 'Gray'),
                    ('Gray', 'Denny'), ('Gray', 'Henley'), ('Gray', 'Emma'),
                    ('Emma', 'Denny'), ('Ivan', 'Henley'), ('Ivan', 'Jenny')
                ])
pos = nx.get_node_attributes(G, 'Location')

nx.draw(G, pos, with_labels = True)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




