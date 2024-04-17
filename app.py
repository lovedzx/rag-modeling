import sys
from langchain import PromptTemplate 
from langchain_community.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI

from langchain.chains import LLMChain 

from model.constants import (
       OPEN_AI_KEY
        )

llm = ChatOpenAI(openai_api_key=OPEN_AI_KEY)

print(llm.invoke("how can langsmith help with testing?"))
