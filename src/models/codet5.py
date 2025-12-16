from transformers import AutoTokenizer, T5ForConditionalGeneration

# Resume a funcionalidade do código fornecido
model_name = "Danda245/CodeT5-base_code-refinement-defects4j"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

code_snippet = """
Defect: 
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
"""

inputs = tokenizer(
    code_snippet,
    return_tensors="pt",
    truncation=True,
    max_length=512
)

outputs = model.generate(
    input_ids=inputs.input_ids,
    attention_mask=inputs.attention_mask,
    max_length=64,
    num_beams=5,
    early_stopping=True
)

summary = tokenizer.decode(outputs[0], skip_special_tokens=True)
print("Resumo:", summary)
