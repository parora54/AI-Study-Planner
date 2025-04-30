import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)

template = ChatPromptTemplate.from_messages(
    [
        ("system", 
        """You are an intelligent study planning agent. You must respond with ONLY valid JSON, no commentary, no markdown, no formatting.
        The user will give you a list of tasks, each with an estimated duration and a priority level (1 to 5, where 1 is highest).
        Your job is to:
        - Prioritize tasks based on urgency and importance
        - Distribute the total available study time each day across the tasks
        - Make sure high-priority and time-sensitive tasks are allocated first
        - Balance the plan so it's realistic and evenly distributed
        - Return a day-by-day plan with what to do each day and for how long.
        ⚠️ Only assign the number of hours specified for each task — do not create extra study hours just because the user has more time available.
        Use clear headings and bullet points for each day."""
        ),
        ("user",
        "This is the work I have to do: {work}\nI have {time} hours per day and {day} total days.\nEach task includes a number of hours required and a priority.\n**Please return ONLY A JSON OBJECT** where each key is a day (e.g., 'Day 1'), and its value is a list of tasks. For example: \nEach task should include: task name, number of hours, and priority.\nDo NOT allocate more hours than required. If extra time exists, just leave it unused."
        ),
    ]
)
