import os
import torch
import torch_directml
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_ID = "mistralai/Mistral-7B-Instruct-v0.3"
MODEL_NAME = "Mistral"

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
    try:
        device = torch_directml.device()
        print("🚀 GPU AMD detectada via DirectML")
        return device, torch.float16
    except Exception:
        print("🧠 Usando CPU")
        torch.set_num_threads(8)
        torch.set_grad_enabled(False)
        return torch.device("cpu"), torch.float32


def analisar_codigo(caminho_arquivo):
    device, dtype = get_device_and_dtype()

    tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        torch_dtype=dtype,
        low_cpu_mem_usage=True,
    ).eval()

    model.to(device)

    MAX_CHARS = 3000

    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        codigo = f.read()

    codigo = codigo[:MAX_CHARS]

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

    input_ids = encoded.to(device)
    attention_mask = input_ids.ne(tokenizer.pad_token_id)

    print("🧠 Analisando código...")

    with torch.no_grad():
        output = model.generate(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_new_tokens=250,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id
        )

    print("✅ Análise concluída")

    resposta = tokenizer.decode(
        output[0][input_ids.shape[1]:],
        skip_special_tokens=True
    )

    return resposta


if __name__ == "__main__":

    pasta_releases = "src/releases"

    for arquivo in os.listdir(pasta_releases):
        if arquivo.endswith(".py"):
            caminho_completo = os.path.join(pasta_releases, arquivo)

            print(f"\n📂 Analisando arquivo: {arquivo}\n")

            resultado = analisar_codigo(caminho_completo)

            print("\n--- RELATÓRIO DO ESPECIALISTA ---\n")
            print(resultado)

            nome_saida = f"resultado_{arquivo.replace('.py', '')}.txt"

            pasta_modelo = os.path.join("src", "results", MODEL_NAME)
            os.makedirs(pasta_modelo, exist_ok=True)

            with open(
                os.path.join(pasta_modelo, nome_saida),
                "w",
                encoding="utf-8"
            ) as f:
                f.write(resultado)
