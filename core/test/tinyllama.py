import pickle
import torch
print(torch.__version__)
print(torch.version.cuda)
with open(
    "C:\\Users\\Acer\\Desktop\\kk_hackniche\\core\\test\\text_generation_pipeline.pkl",
    "rb",
) as f:
    loaded_pipe = pickle.load(f)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
loaded_pipe.model.to(device)
messages = [
    {
        "role": "user",
        "content": "write a function to check wheter string is pallindrome or not in python.",
    },
]
prompt = loaded_pipe.tokenizer.apply_chat_template(
    messages, tokenize=False, add_generation_prompt=True
)
outputs = loaded_pipe(
    prompt, max_new_tokens=555, do_sample=True, temperature=0.7, top_k=50, top_p=0.95
)
print(outputs[0]["generated_text"])
