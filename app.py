import streamlit as st
import pandas as pd
from agent import llm, template
from formatting_helpers import convert_df_to_text, study_plan_to_txt
import datetime as dt
import json

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

# Generate Study Plan
button = st.button('Generate Study Plan')
if button:
    if not work.empty:
        formatted_prompt = template.format_messages(work=convert_df_to_text(work), time=time, day=day)
        with st.spinner("Crafting your ultimate study plan..."):
            chain = formatted_prompt | llm
            
            result = chain.invoke()

        st.subheader("🗓️ Your Study Plan")

        # Parse GPT response as JSON
        try:
            content = json.loads(result.content)
        except json.JSONDecodeError:
            st.error("GPT did not return valid JSON. Please try again.")
            st.text(result.content)
            st.stop()

        # Download Output for users
        txt_str = study_plan_to_txt(content)

        st.download_button(
            label="Download Study Plan (. txt)",
            data=txt_str,
            file_name=f"study_plan_{dt.date.today().strftime('%m%d%Y')}.txt",
            mime="text/plain"
        )

        # Display output into expander cards
        for day, tasks in content.items():
            with st.expander(f"📅 {day}", expanded=True):
                if tasks:
                    for task in tasks:
                        st.markdown(
                            f"- **{task['task_name']}** – {task['hours']} hours (Priority {task['priority']})"
                        )
                else:
                    st.markdown("_No tasks assigned. ✅ Enjoy your free time!_")
            
    else:
        st.write('ERROR: COMPLETE ALL FIELDS')