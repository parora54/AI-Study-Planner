import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate

os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)

template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an AI agent designed to assist users in organizing their coursework and generating personalized study plans."),
        ("user", "This is the work I have to do: {work}. This is the total amount of time I have to complete things per day: {time}. This is the total amount of days I have to complete the tasks: {day}. Write me a day by day study plan based on these parameters."),
    ]
)
