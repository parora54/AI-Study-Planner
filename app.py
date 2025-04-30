import streamlit as st
import pandas as pd
from agent import llm, template

st.markdown('# PLAN YOUR STUDY SCHEDULE')

# Configuration of time adjustment for study plan
time = st.slider(label='Enter total time available for studying per day (hours)', min_value=1.0, max_value=9.0, value=4.0, step=0.5)
day = st.slider(label='Enter total days available to study', min_value=1, max_value=100, value=7, step=1)

# Area for user to enter their work
df = pd.DataFrame(columns=['Work','Priority',"Number of Hours Required"])
st.write('Enter work that needs to be completed as well as its estimated time needed to complete')
work = st.data_editor(
    df, 
    column_config={
        "Priority": st.column_config.NumberColumn("Priority Level (1-5)", min_value=1, max_value=5, step=1),
        "Number of Hours Required": st.column_config.NumberColumn("Number of Hours Required", min_value=0.5, max_value=100, step=0.5)
    }, 
    hide_index=True,
    num_rows="dynamic"
)

def convert_df_to_text(df):
    '''
    Takes dataframe and turns it into neat formatted string for llm
    '''
    lines = []
    for _, row in df.iterrows():
        lines.append(
            f"Task: {row['Work']}\nPriority: {row['Priority']}\nHours Required: {row['Number of Hours Required']}\n"
        )
    return "\n---\n".join(lines)


# Generate Study Plan
button = st.button('Generate Study Plan')
if button:
    if not work.empty and time and day:
        formatted_prompt = template.format_messages(work=convert_df_to_text(work), time=time, day=day)
        with st.spinner("Crafting your ultimate study plan..."):
            result = llm.invoke(formatted_prompt)
        st.write(result.content)
    else:
        st.write('ERROR: COMPLETE ALL FIELDS')