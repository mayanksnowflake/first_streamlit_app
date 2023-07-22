import streamlit as st
import pandas as pd

st.title('My Parents New Healthy Diner!')
st.title('Healthy Everyday Menu_italics_ :blue[colors] and emojis :sunglasses:')

st.header ('🍞 Breakfast Menu')
st.text('🥣 Omega 3 & Bluberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard Boiked Free Range Eggs')


st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')



# Display the table on the page.

my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
st.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
st.multiselect("Pick some fruits:", list(my_fruit_list.index))
