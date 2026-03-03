import os
import json
import traceback 
import pandas as pd
from dotenv import load_dotenv
from src.mcqgenerator.logger import logging
from src.mcqgenerator.utils import read_file,get_table_data

from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()
mykey=os.getenv("key")

llm=ChatOpenAI(model="gpt-3.5-turbo",temperature=0.9,openai_api_key=mykey)

template="""
    Text: {text}
    you are an expert MCQ maker. Given the above text, it is your job to \
    create a quiz of {number} multiple choice questions for {subject} students in {tone} tone.
    Make sure the questions are not repeated and check all the questions to be conforming the text as well.
    Make sure to format your response like RESPONSE_JSON below and use it as a guide. \
    Ensure to make {number} MCQs
    ### RESPONSE_JSON
    {response_json}

"""

quiz_generator_prompt=PromptTemplate(
    input_variables=["text","number","subject","tone","response_json"],
    template=template
)

quiz_chain=quiz_generator_prompt | llm | StrOutputParser()


template2="""
    You are an expert english grammarian and writer. Give a multiple choice quiz for {subject} students. \
    You need to evaluate the complexity of the question and give a complete analysis of the quiz. Only use at max 50 words for complexity analysis.
    if the quiz is not at per with the cognitive and analytical abilities of the students,
    update the quiz questions which needs to be changed and change the tone such that it perfectly fits the students abilities.
    Quiz_MCQs:
    {quiz}

    check from an expert English writer of the above quiz:
"""

quiz_evaluation_prompt=PromptTemplate(
    input_variables=["subject","quiz"],
    template=template2
)

review_chain= quiz_evaluation_prompt | llm | StrOutputParser()

generate_evaluate_chain = (
    RunnablePassthrough.assign(quiz=quiz_chain)
    | RunnablePassthrough.assign(review=review_chain)
)
