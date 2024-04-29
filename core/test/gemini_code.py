import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
load_dotenv()
import re

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

def generate_code_gemini(language, prompt):
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
        f"you are a function code generator and generate a function where {prompt} in {language} program also test one hard coded example ",
        stream=True,
    )
    response = ""
    for chunk in res:
        response += chunk.text
    # print(response)
    # q_code = segerate(response)
    # print(output, "output hai ")
    return extract_code(response)