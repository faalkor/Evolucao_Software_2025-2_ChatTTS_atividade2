# Análise de Code Smells

## 📋 Tutorial da Atividade

O tutorial completo com as instruções passo a passo para realizar esta atividade está disponível em PDF:

[📖 **Acessar Tutorial em PDF**](https://)

## 📰 Projeto
- [**ChatTTS**](https://github.com/2noise/ChatTTS)

## 🤖 Modelos

- [**X**](https://)
- [**Y**](https://)
- [**Z**](https://)

## Estrutura do Projeto

    .
    ├── README.md
    ├── requirements.txt
    └── src
        ├── main.py
        ├── models
        │   ├── X
        │   │   └── a
        │   ├── Y
        │   │   └── b
        │   └── Z
        │       └── c
        └── results
            ├── X.json
            ├── Y.json
            └── Z.json

## Pré-requisitos

Antes de rodar qualquer coisa, você vai precisar de:

- **Python 3.9+**
- **pip** (gerenciador de pacotes do Python)
- **Git** (para clonar o repositório)

## Fluxo resumido de execução
1. Clonar o repositório e instalar dependências.
2. Executar:
´´´bash
cd src
python main.py
´´´
3. Analisar os resultados em `"src/results/*.json."`


## 1. Instalação do Projeto

### 1.1. Clonar o repositório
```bash
    git clone https://github.com/faalkor/Evolucao_Software_2025-2_ChatTTS_atividade2.git
    cd Evolucao_Software_2025-2_ChatTTS_atividade2
```
### 1.2. Instalar dependências
```bash
    pip install -r requirements.txt
```

## 2. Como executar os modelos

### 2.1. Execução unificada via main.py
O script `"src/main.py"` executa os três modelos em sequência:
```python
from models.X
from models.Y
from models.Z
```
Para rodar a análise completa:

```bash
cd src
python main.py
# ou python3 main.py
```

Na primeira execução, a biblioteca `"transformers"` irá baixar os modelos do Hugging Face.
Isso pode levar alguns minutos, dependendo da conexão.

Ao final, serão criados/atualizados os arquivos:
```text
src/results/X.json
src/results/Y.json
src/results/Z.json
```
## 3. Formato dos arquivos de saída
Cada arquivo de resultados `"(*_results.json)"` contém uma lista de objetos
Cada objeto tem a estrutura:
```json
{
  "text": "conteúdo do código...",
  "label": "POSITIVE | NEUTRAL | NEGATIVE",
  "score": 0.987
}
```
- `"text"`: código analisado
- `"label"`: detecção ou não de defeito atribuído pelo modelo
- `"score"`: confiança do modelo na classificação (probabilidade aproximada)
