import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
st.title("Let's Do Something Cool.")
st.subheader('Data Analysis Using Python and Streamlit')

#Uploading a dataset

upload = st.file_uploader("Upload a CSV to toy around")
if upload is not None:
    df = pd.read_csv(upload)
 
if upload is not None:
    with st.container():
        #Show dataset
        if st.checkbox("Take a peek at your data"):
            if st.button("Head"):
                st.write(df.head(15))
            if st.button("Tail"):
                st.write(df.tail(15))
        #Check datatype of each column
        if st.checkbox("Datatype of each column"):
            st.text('What kind of objects are we working with?')
            st.write(df.dtypes)

#Some overall statistics

#let's talk null values
if upload is not None:
    with st.container():
        st.subheader('Let\'s do some simple anaytics')
        st.write('Null value heatmap')
        fig, ax = plt.subplots()
        sns.heatmap(df.isnull(), ax = ax)
        st.pyplot(fig)

#Find some dup values
if upload is not None:
    test = df.duplicated().any()
    if test == True:
        st.warning('You have duplicate values in your data\n')
        dup = st.selectbox('Do you want to remove them?',('Select One', 'Yes', 'No'))
        if dup == 'Yes':
            df = df.drop_duplicates()
            st.text('Duplicate values have been removed')
        if dup == 'No':
            st.text('No problem!')
    else:
        st.write('There\'d normally be some duplicate values, but your data is good!')

#Some overall statistics about the data
if upload is not None:
    st.subheader('Some basic stats')
    st.write(df.describe())

#About slection

if st.button('About app'):
    st.text("built with Streamlit, Python, and some dependencies:\n"
            'If we are ')
