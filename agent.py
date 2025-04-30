import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)

template = ChatPromptTemplate.from_messages(
    [
        ("system", 
        """You are an intelligent study planning agent.
        The user will give you a list of tasks, each with an estimated duration and a priority level (1 to 5, where 1 is highest).
        Your job is to:
        - Prioritize tasks based on urgency and importance
        - Distribute the total available study time each day across the tasks
        - Make sure high-priority and time-sensitive tasks are allocated first
        - Balance the plan so it's realistic and evenly distributed
        - Return a day-by-day plan with what to do each day and for how long.
        Use clear headings and bullet points for each day."""
        ),
        ("user", "This is the work I have to do: {work}. This is the total amount of time I have to complete things per day: {time}. This is the total amount of days I have to complete the tasks: {day}. Write me a day by day study plan based on these parameters."),
    ]
)
