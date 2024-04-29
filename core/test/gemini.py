import google.generativeai as genai
from dotenv import load_dotenv
import os
import json

load_dotenv()

import re

# def segerate(input_string):
#     pattern = r"```(\w+)\n([\s\S]+?)```"
#     match = re.search(pattern, input_string)
#     if match:
#         program_name = match.group(1)
#         program_code = match.group(2)
#         return program_name,program_code
#     else:
#         return "no","any"


def segerate(text):
    pattern = r"```([\s\S]+?)```"
    matches = re.findall(pattern, text)
    return [block.split("\n", 1)[1] if "\n" in block else "" for block in matches]


def generate_gemini(schema, language, database, prompt):
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    generation_config = {
        "temperature": 0.9,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 5000,
    }
    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
    ]
    model = genai.GenerativeModel(
        model_name="gemini-1.0-pro",
        generation_config=generation_config,
        safety_settings=safety_settings,
    )
    convo = model.start_chat(history=[])
    res = convo.send_message(
        f"""for the following schema {schema} Give me a function based query in {language} to {prompt} for {database}.""",
        stream=True,
    )
    response = ""
    for chunk in res:
        response += chunk.text
    q_code = segerate(response)
    result = {"code": q_code}
    json_result1 = json.dumps(result, indent=2)

    res = convo.send_message(
        "give me just sample input data values for the previous code you provided in javascript",
        stream=True,
    )
    response2 = ""
    for chunk in res:
        response2 += chunk.text
    q_code = segerate(response2)
    result = {"input_data": q_code}
    json_result2 = json.dumps(result, indent=2)

    res = convo.send_message(
        "give me sample output data values for the previous code you provided",
        stream=True,
    )
    response3 = ""
    for chunk in res:
        response3 += chunk.text
    # print(response3)
    o_code = segerate(response3)
    result = {"output_data": o_code}
    json_result3 = json.dumps(result, indent=2)
    # print(json_result3)

    output = {
      json_result1, json_result2,json_result3,
    }
    print(output, "output hai ")
    return output


# schema = """
# {
#     "tables": [
#         {
#             "name": "Student",
#             "attributes": [
#                 {
#                     "name": "id",
#                     "keyType": "primary",
#                     "dataType": "number",
#                     "referenceTable": ""
#                 },
#                 {
#                     "name": "name",
#                     "keyType": "",
#                     "dataType": "string",
#                     "referenceTable": ""
#                 }
#             ]
#         },
#         {
#             "name": "Marks",
#             "attributes": [
#                 {
#                     "name": "sid",
#                     "keyType": "foreign",
#                     "dataType": "number",
#                     "referenceTable": "Student"
#                 },
#                 {
#                     "name": "marks",
#                     "keyType": "",
#                     "dataType": "number",
#                     "referenceTable": ""
#                 }
#             ]
#         }
#     ]
# }
# """
# language = "javascript"
# database = "nosql"
# prompt = "retrieve records of student name of computer department having marks greater than 100"
# generate_code(schema, language, database, prompt)
