import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy

# First some MPG Data Exploration
@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    return df
# read data from file

inet_df_raw = load_data(path="share-of-individuals-using-the-internet.csv")
inet_df = deepcopy(inet_df_raw)

income_df_raw=load_data(path='gdp-per-capita-worldbank.csv')
income_df= deepcopy(income_df_raw)
income_df.sort_values(by=['Year'], inplace=True)
#print(income_df)
# Add title and header
st.title("My first Streamlit App")
st.header("Global internet Access")

# Setting up columns
left_column, right_column = st.columns( [1, 1])
# Widgets: checkbox (you can replace st.xx with st.sidebar.xx)
plot_types = ["Internet access", "GDP per capita"]
plot_type = right_column.radio("Choose Plot Type", plot_types)

if plot_type == 'Internet access':
     d = inet_df
elif plot_type == 'GDP per capita':
     d = income_df
 
if left_column.checkbox("Show Dataframe"):
    st.subheader("This is my dataset:")
    st.dataframe(data= d)


# data for GDP per capita
#dfi = pd.read_csv('share-of-individuals-using-the-internet.csv')
dfi=inet_df
#print(dfi)
#plot Internet access
plot1 = px.choropleth(dfi,    
                           locations=dfi.Entity,
                           locationmode='country names',
                           color=dfi['Individuals using the Internet (% of population)'],
                           animation_frame=dfi.Year,
                            color_continuous_scale="Inferno",
                           center={"lat": 0, "lon": 0},
                            title = "Internet access worldwide",
                            width=1000,
                            height=800
                         
                    )
                   
#fig_i.show()

#st.plotly_chart(fig1)
dfw= income_df
plot2 = px.choropleth(dfw
                    ,    
                           locations=dfw.Entity,
                           locationmode='country names',
                           color=dfw['GDP per capita, PPP (constant 2017 international $)'],
                           animation_frame=dfw.Year,
                            color_continuous_scale="Plasma",
                           center={"lat": 0, "lon": 0},
                            title = "Gross domestic product per capita",
                             width=1000,
                            height=800
                    
                   )
#fig_w.show()
if plot_type == "Internet access":
   st.plotly_chart(plot1)

elif plot_type == "GDP per capita": 
    st.plotly_chart(plot2)







