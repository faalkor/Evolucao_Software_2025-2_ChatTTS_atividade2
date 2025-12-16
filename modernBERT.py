from transformers import pipeline, AutoModelForSequenceClassification, AutoTokenizer

model_name = "mrm8488/ModernBERT-base-ft-code-defect-detection-4k"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)


model.config.id2label = {
    0: "DEFECT",
    1: "NO_DEFECT"
}

model.config.label2id = {
    "DEFECT": 0,
    "NO_DEFECT": 1
}

classifier = pipeline(
    "text-classification",
    model=model,
    tokenizer=tokenizer,
    max_length=4096,
    truncation=True,
)

# Não conseguiu identificar defeito sutil
good_code = "def add(a, b): return a + b"
bad_code = "def add(a, b): return a - b"


print(classifier(good_code))
print(classifier(bad_code))
