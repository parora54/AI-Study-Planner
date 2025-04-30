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
You must respond with ONLY valid JSON. 
No markdown, no bullet points, no code blocks, and no explanation. Just return the raw JSON object.

The user will give you a list of tasks, each with:
- a task name
- estimated number of hours required
- a priority level (1 = highest, 5 = lowest)

Your job is to:
- Prioritize tasks based on urgency and importance
- Distribute only the required total task hours across the available study days
- Never invent or increase study hours to fill time
- Leave any unused hours blank (do not assign extra work)

Respond in the following JSON format:
{
  "Day 1": [
    { "task_name": "Review Math Notes", "hours": 2, "priority": 1 },
    { "task_name": "Watch Chemistry Lecture", "hours": 1.5, "priority": 3 }
  ],
  "Day 2": []
}
"""
        ),
        ("user",
        "This is the work I have to do: {work}\n"
        "I have {time} hours per day and {day} total days.\n"
        "Please respond ONLY with a valid JSON object using the specified format."
        )
    ]
)
