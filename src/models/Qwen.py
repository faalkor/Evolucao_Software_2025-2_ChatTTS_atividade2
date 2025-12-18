import os
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_ID = "Qwen/Qwen2.5-Coder-7B-Instruct"
MODEL_NAME = "Qwen-2.5-Coder"

SYSTEM_PROMPT = """
Atue como um Engenheiro de Software Sênior especialista em Python e Engenharia de Software.
Analise o código procurando por Code Smells conforme o catálogo do Refactoring Guru,
com foco em: Long Method, Magic Numbers e Cognitive Complexity.

Para cada code smell identificado, apresente:
- Localização (função ou trecho do código)
- Evidência concreta no código
- Justificativa técnica
- Sugestão de refatoração
"""

def get_device_and_dtype():
    if torch.cuda.is_available():
        print("🚀 NVIDIA CUDA detectada")
        return "cuda", torch.float16
    else:
        print("🧠 Usando CPU")
        torch.set_num_threads(8)
        torch.set_grad_enabled(False)
        return "cpu", torch.float32


def analisar_codigo(caminho_arquivo):
    device, dtype = get_device_and_dtype()

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_ID,
        trust_remote_code=True
    )
    tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        device_map="auto" if device == "cuda" else None,
        torch_dtype=dtype,
        trust_remote_code=True,
        low_cpu_mem_usage=True
    ).eval()

    if device == "cpu":
        model.to("cpu")

    MAX_CHARS = 2000  # ajustado para CPU

    with open(caminho_arquivo, "r", encoding="utf-8") as f:
        codigo = f.read()

    if len(codigo) > MAX_CHARS:
        codigo = codigo[:MAX_CHARS]

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {
            "role": "user",
            "content": f"Analise o código a seguir e identifique code smells:\n\n{codigo}"
        }
    ]

    encoded = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        return_tensors="pt"
    )

    input_ids = encoded
    attention_mask = input_ids.ne(tokenizer.pad_token_id)

    print("🧠 Analisando código com Qwen...")

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
    pasta_saida = os.path.join("src", "results", MODEL_NAME)
    os.makedirs(pasta_saida, exist_ok=True)

    for arquivo in os.listdir(pasta_releases):
        if arquivo.endswith(".py"):
            caminho_completo = os.path.join(pasta_releases, arquivo)

            print(f"\n📂 Analisando arquivo: {arquivo}\n")

            resultado = analisar_codigo(caminho_completo)

            print("\n--- RELATÓRIO DO ESPECIALISTA (QWEN) ---\n")
            print(resultado)

            nome_saida = f"resultado_{arquivo.replace('.py', '')}.txt"

            with open(
                os.path.join(pasta_saida, nome_saida),
                "w",
                encoding="utf-8"
            ) as f:
                f.write(resultado)
