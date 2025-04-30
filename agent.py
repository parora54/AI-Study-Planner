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
        "This is the work I have to do:\n{work}\n\n"
        "I have {time} hours per day and {day} total days to study.\n"
        "Each task includes the number of hours required and a priority (1 = highest).\n"
        "ONLY return a JSON object. Example:\n"
        "{\n  \"Day 1\": [\n    {\"task\": \"Task A\", \"hours\": 2, \"priority\": 1}\n  ],\n  \"Day 2\": [...]\n}\n"
        "No explanation. No markdown. No code blocks. Just the raw JSON."
        )
    ]
)
