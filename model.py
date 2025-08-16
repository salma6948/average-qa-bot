from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.distributed import DistributedConfig
import torch

from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Use GPT-2 Medium
model_path = "gpt2-medium"

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_path)
tokenizer.padding_side = "left"

# Load model 
model = AutoModelForCausalLM.from_pretrained(model_path)

# Response function 
def generate_response(prompt: str, max_new_tokens: int = 150) -> str:
    inputs = tokenizer(prompt, return_tensors="pt").to("cpu")
    outputs = model.generate(
        **inputs,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
        repetition_penalty=1.2,  # reduces repeated phrases
        pad_token_id=tokenizer.eos_token_id
    )
    return tokenizer.decode(outputs[0], skip_special_tokens=True)
