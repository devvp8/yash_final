from openai import OpenAI
from dotenv import load_dotenv
import os
import re
load_dotenv()

def segerate(text):
    pattern = r"```([\s\S]+?)```"
    matches = re.findall(pattern, text)
    out = [block.split("\n", 1)[1] if "\n" in block else "" for block in matches]
    return out

def generate_openai(schema, language, database, prompt):
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )
    prompt= f"""for the following schema {schema} Give me a function based query in {language} to {prompt} for {database}"""
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo-16k-0613",
    messages=[
        {"role": "system", "content": "You are a function query code generator assistant where you have task to generate function code query"},
        {"role": "user", "content": prompt}
    ],
    stream=True
    )
    response = ""
    for chunk in completion:
        if chunk.choices[0].delta.content:
            response += chunk.choices[0].delta.content
            print(chunk.choices[0].delta.content,end="")
    print(response)
    return segerate(response)
    
    
    prompt = "Generate sample input data values in javascript for the previous response and the schema"
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo-16k-0613",
    messages=[
        {"role": "system", "content": "You are sample input value generator"},
        {"role": "user", "content": prompt}
    ],
    stream=True
    )
    response2 = ""
    for chunk in completion:
        if chunk.choices[0].delta.content:
            response2 += chunk.choices[0].delta.content
            print(chunk.choices[0].delta.content,end="")
    print(response2)
    return segerate(response)

    
# schema = """
# {
#   "tables": {
#     "students": {
#       "columns": {
#         "student_id": "integer",
#         "name": "string",
#         "age": "integer",
#         "department_id": "integer"
#       },
#       "foreign_keys": {
#         "department_id": {
#           "table": "departments",
#           "column": "department_id"
#         }
#       }
#     },
#     "departments": {
#       "columns": {
#         "department_id": "integer",
#         "name": "string"
#       }
#     },
#     "marks": {
#       "columns": {
#         "mark_id": "integer",
#         "student_id": "integer",
#         "subject": "string",
#         "score": "integer"
#       },
#       "foreign_keys": {
#         "student_id": {
#           "table": "students",
#           "column": "student_id"
#         }
#       }
#     }
#   }
# }
# """
# language = "javascript"
# prompt = "retrieve records of student name of computer department having marks greater than 100"
# db = "nosql"

# print(generate_openai(schema, language, db, prompt))