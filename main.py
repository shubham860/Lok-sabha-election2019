import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go 
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

init_notebook_mode(connected=True) 

dataset = pd.read_csv('UP_2019.csv')

data = dict(type = 'choropleth',
            locations = dataset['District'],
            locationmode = 'USA-states',
            colorscale= 'Portland',
            text= ['text1','text2','text3'],
            z=[1.0,2.0,3.0],
            colorbar = {'title':'Uttar pradesh Lok sabha election 2019'})

layout = dict(title='Lok sabha election 2019',geo = {'scope':'usa'})

choromap = go.Figure(data = [data],layout = layout)

iplot(choromap)