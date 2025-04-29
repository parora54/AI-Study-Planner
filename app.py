import streamlit as st
from agent import llm, template

st.title('Welcome to the APP')
work = st.text_area('Enter work that needs to be completed as well as its estimated time needed to complete')
time = st.text_input('Enter total time available for studying per day')
day = st.text_input('Enter total days available to study')

button = st.button('Generate Study Plan')

if button:
    if work and time and day:
        formatted_prompt = template.format_messages(work=work, time=time, day=day)
        result = llm.invoke(formatted_prompt)
        st.write(result.content)
    else:
        st.write('ERROR: COMPLETE ALL FIELDS')