# Análise de Sentimentos em Evolução de Software

Este repositório apresenta uma **pipeline de análise de sentimentos aplicada à Evolução de Software**, utilizando comentários de *Pull Requests* do projeto **ChatTTS** como base de dados.
A atividade compara diferentes **modelos de linguagem** executados **diretamente no Google Colab**, garantindo reprodutibilidade, facilidade de uso e padronização do ambiente.

---

## 📋 Tutorial da Atividade

O tutorial oficial da atividade, com instruções passo a passo e critérios de avaliação, está disponível em PDF:

[📖 **Acessar Tutorial em PDF**](https://docs.google.com/document/d/1p-8Ncw8_xaF_mdi4iRVpKwUrpNi_9oD37J9TUgNvhFI/edit?usp=sharing)

---

## 📰 Projeto
- [**ChatTTS**](https://github.com/2noise/ChatTTS)

Os comentários de *Pull Requests* deste repositório são utilizados como entrada para os modelos de análise de sentimentos.

---

## 🤖 Modelos Utilizados

Os modelos são executados em **notebooks do Google Colab**, evitando dependências locais complexas e permitindo uso de GPU quando disponível.

### 🔹 Modelos LLM (Execução via Colab)

* **Mistral**
  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/faalkor/Evolucao_Software_2025-2_ChatTTS_atividade2/blob/main/src/models/Mistral.ipynb)

* **Qwen**
  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/faalkor/Evolucao_Software_2025-2_ChatTTS_atividade2/blob/main/src/models/Qwen.ipynb)

* **Phi‑3**
  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/faalkor/Evolucao_Software_2025-2_ChatTTS_atividade2/blob/main/src/models/Phi_3.ipynb)

> 💡 Cada notebook é autocontido e pode ser executado individualmente no Colab.

---

## 🗂 Estrutura do Projeto

```
.
├── README.md
├── requirements.txt
└── src
    ├── main.py
    ├── PRs_comments
    │   └── extract_pr_comments.py
    ├── models
    │   ├── Mistral.ipynb
    │   ├── Phi_3.ipynb
    │   └── Qwen.ipynb
    └── results
        ├── Mistral
        │   ├── resultado_core-0.1.1.txt
        │   ├── resultado_core-0.2.2.txt
        │   └── resultado_core-0.2.4.txt
        ├── Phi_3
        │   ├── resultado_core-0.1.1.txt
        │   ├── resultado_core-0.2.2.txt
        │   └── resultado_core-0.2.4.txt
        └── Qwen
            ├── resultado_core-0.1.1.txt
            ├── resultado_core-0.2.2.txt
            └── resultado_core-0.2.4.txt
```

---

## ⚙️ Pré‑requisitos (Execução Local)

Caso deseje executar a versão local (modelos clássicos):

* **Python 3.9+**
* **pip**
* **Git**

Instalação das dependências:

```bash
pip install -r requirements.txt
```

---

## 🚀 Fluxo Resumido de Execução

1. Clonar o repositório.
2. Instalar as dependências.
3. GExecução via Google Colab.

---

## 1. Instalação do Projeto

### 1.1 Clonar o repositório

```bash
git clone https://github.com/faalkor/Evolucao_Software_2025-2_ChatTTS_atividade2.git
cd Evolucao_Software_2025-2_ChatTTS_atividade2
```

### 1.2 Instalar dependências

```bash
pip install -r requirements.txt
```

---

## 2. Execução via Google Colab

Para os modelos **Mistral**, **Qwen** e **Phi‑3**, utilize diretamente os notebooks no Google Colab:

1. Clique no badge **Open in Colab** do modelo desejado.
2. Execute as células sequencialmente.
3. Os resultados serão exibidos no próprio notebook ou exportados em formato `.json`.

Essa abordagem evita configurações locais e permite uso de GPU.

---

## 3. Formato dos Arquivos de Saída

Cada arquivo de resultados contém uma lista de objetos no formato:

```json
{
  "pr_number": 123,
  "user": "login_do_usuario",
  "text": "conteúdo do comentário",
  "label": "POSITIVE | NEUTRAL | NEGATIVE",
  "score": 0.987
}
```

* **pr_number**: número do Pull Request
* **user**: autor do comentário
* **text**: texto analisado
* **label**: sentimento atribuído
* **score**: confiança do modelo

---

## 📌 Observações Metodológicas

* Os modelos clássicos garantem **baseline comparável**.
* Os LLMs (Mistral, Qwen, Phi‑3) permitem análise mais contextual.
* A execução via Colab garante **reprodutibilidade e padronização**.
* Os resultados podem ser comparados quantitativamente (labels e scores) e qualitativamente.

---

## 👨‍💻 Disciplina

**Evolução de Software – 2025/2**
Atividade prática de análise de sentimentos aplicada a repositórios open‑source.
