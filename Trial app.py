import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.title('My Streamlit Application')

x = st.slider('Select a value for x', 0, 10)
st.write('You selected', x)

df = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.line_chart(df)
