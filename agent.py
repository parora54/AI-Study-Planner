import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate

import getpass

if "OPENAI_API_KEY" not in os.environ:
    os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter your OpenAI API key: ")

model = ChatOpenAI(model="gpt-4o-mini", temperature=0.0)

template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Your name is Bob"),
        ("user", "{input}"),
    ]
)
