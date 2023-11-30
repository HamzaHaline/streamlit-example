import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns
from fonction_project import *
import warnings




#%% Debut Page 

# TITRE : 
st.title("Data Analyse for the drug data ")
st.markdown("Project made by \n Yahya BOUAYAD,\n Hamza HALINE\n et Joshua BORNET")

if st.checkbox("Show raw data"):
    st.subheader('Drug Raw data used')
    st.write(data)
    st.markdown(
        """
        The dataset here is made up of 31 columns, the first represents some global characteristics about the person such as his age, education and others. Then comes some psychological aspects of the person, and the last part of the dataset is about what kind of addiction the person has, from chocolate to cocaine.
We have 1800 individuals, which gives us a good data set to study.

        """
        )
st.markdown("We read the documentation and thus, we were able to rename the columns and modify them to make their content readable by everybody.")



