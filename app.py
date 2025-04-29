import streamlit as st
from agent import llm, template

st.title('Welcome to the APP')
work = st.text_area('Enter work that needs to be completed as well as its estimated time needed to complete')
time = st.slider(label='Enter total time available for studying per day (hours)', min_value=1.0, max_value=9.0, value=4.0, step=0.5)
day = st.slider('Enter total days available to study', min_value=1, max_value=100, value=7, step=1)

button = st.button('Generate Study Plan')

if button:
    if work and time and day:
        formatted_prompt = template.format_messages(work=work, time=time, day=day)
        result = llm.invoke(formatted_prompt)
        st.write(result.content)
    else:
        st.write('ERROR: COMPLETE ALL FIELDS')