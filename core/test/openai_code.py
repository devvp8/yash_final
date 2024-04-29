from openai import OpenAI
from dotenv import load_dotenv
import os
import re
load_dotenv()

def extract_code(input_string):
    if "```" in input_string:
        start_index = input_string.find("```") + 3  
        end_index = input_string.find("```", start_index)
        code_block = input_string[start_index:end_index].strip()
        code_lines = code_block.split('\n', 1)
        if len(code_lines) > 1:
            code_block = code_lines[1]
        return code_block
    else:
        return input_string

def generate_code_openai(language, prompt):
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )
    prompt= f"""write a {language} program to do {prompt}"""
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo-16k-0613",
    messages=[
        {"role": "system", "content": "you are a function code generator which generates a code based on the user problem and test one hardcoded example for it in the code, also just give me the code not the tags and explanations "},
        {"role": "user", "content": prompt}
    ],
    stream=True
    )
    response = ""
    for chunk in completion:
        if chunk.choices[0].delta.content:
            response += chunk.choices[0].delta.content
            # print(chunk.choices[0].delta.content,end="")
    return extract_code(response)
