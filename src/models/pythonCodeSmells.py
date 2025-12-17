import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_ID = "jonaskoenig/Llama-3-8b-instruct-ML-Python-code-smells"

SYSTEM_PROMPT = """
Atue como um Engenheiro de Software Sênior especialista em Python/ML.
Analise o código procurando por Code Smells (Long Method, Magic Numbers, Cognitive Complexity).
Para cada smell, forneça:
- Localização
- Evidência
- Justificativa Técnica
- Sugestão de Refatoração
"""

def get_device_and_dtype():
    if torch.cuda.is_available():
        print("🚀 NVIDIA CUDA detectada")
        return "cuda", torch.float16
    else:
        print("🧠 Usando CPU")
        return "cpu", torch.float32


def analisar_codigo(caminho_arquivo):
    device, dtype = get_device_and_dtype()

    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        device_map="auto" if device == "cuda" else None,
        dtype=dtype,
        low_cpu_mem_usage=True,
    ).eval()

    if device == "cpu":
        model.to("cpu")

    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        codigo = f.read()

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": f"Analise este código:\n\n{codigo}"}
    ]

    encoded = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        return_tensors="pt",
    )

    input_ids = encoded
    attention_mask = input_ids.ne(tokenizer.pad_token_id)

    print("🧠 Analisando código...")

    with torch.no_grad():
        output = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_new_tokens=800,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id
        )

    resposta = tokenizer.decode(
        output[0][input_ids.shape[1]:],
        skip_special_tokens=True
    )

    return resposta


if __name__ == "__main__":
    resultado = analisar_codigo(
        "src/releases/ChatTTS-0.1.1/ChatTTS/core.py"
    )

    print("\n--- RELATÓRIO DO ESPECIALISTA ---\n")
    print(resultado)

    # Salva o resultado em um arquivo texto
    with open(os.path.join("src","results","resultado_pythonCodeSmells.txt"), "w", encoding="utf-8") as f:
        f.write(resultado)
