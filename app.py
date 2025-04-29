import streamlit as st
from agent import model, template

st.title('Welcome to the APP')
prompt = st.text_input('Enter prompt here')

if prompt:
    formatted_prompt = template.format_messages(input=prompt)
    result = model.invoke(formatted_prompt)
    st.write(result.content)