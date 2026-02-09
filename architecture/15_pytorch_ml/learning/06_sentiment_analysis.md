# PyTorch Sentiment Analysis

> **Text classification with PyTorch** - Build a sentiment analyzer from scratch

---

## 🖼️ Visual Architecture

![PyTorch: Sentiment Analysis](006_sentiment_analysis.png)

![PyTorch: Sentiment Analysis](006_sentiment_analysis_2.png)

## 🎯 Project Overview

Build a sentiment analysis model that classifies text as **positive** or **negative**.

```
Input: "This movie is amazing!"
         ↓
    Preprocessing
         ↓
    Tokenization
         ↓
    Model (Neural Network)
         ↓
Output: Positive (95% confidence)
```

---

## 📊 Dataset

We'll use a simple movie review dataset (no API key needed).

```python
# Sample data
reviews = [
    ("This movie is great!", 1),  # 1 = positive
    ("I loved it so much", 1),
    ("Terrible waste of time", 0),  # 0 = negative
    ("Worst movie ever", 0),
    ("Amazing acting and plot", 1),
    ("Boring and predictable", 0)
]
```

---

## 🔧 Step 1: Data Preparation

```python
import torch
import torch.nn as nn
from collections import Counter
import re

# Sample dataset
train_data = [
    ("This movie is great", 1),
    ("I loved it", 1),
    ("Terrible waste of time", 0),
    ("Worst movie ever", 0),
    ("Amazing acting", 1),
    ("Boring and predictable", 0),
    ("Fantastic film", 1),
    ("Not worth watching", 0)
]

# Preprocessing function
def preprocess(text):
    """Lowercase and remove special characters"""
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text.split()

# Build vocabulary
all_words = []
for text, _ in train_data:
    all_words.extend(preprocess(text))

vocab = {word: idx + 1 for idx, word in enumerate(set(all_words))}
vocab['<PAD>'] = 0  # Padding token
vocab_size = len(vocab)

print(f"Vocabulary size: {vocab_size}")
print(f"Sample vocab: {list(vocab.items())[:5]}")
```

---

## 🔢 Step 2: Text to Numbers

```python
def text_to_indices(text, vocab, max_len=10):
    """Convert text to list of indices"""
    words = preprocess(text)
    indices = [vocab.get(word, 0) for word in words]

    # Pad or truncate to max_len
    if len(indices) < max_len:
        indices += [0] * (max_len - len(indices))
    else:
        indices = indices[:max_len]

    return indices

# Convert all data
X_train = []
y_train = []

for text, label in train_data:
    X_train.append(text_to_indices(text, vocab))
    y_train.append(label)

# Convert to tensors
X_train = torch.tensor(X_train)
y_train = torch.tensor(y_train, dtype=torch.float32)

print(f"X_train shape: {X_train.shape}")  # (8, 10)
print(f"y_train shape: {y_train.shape}")  # (8,)
```

---

## 🧠 Step 3: Define Model

```python
class SentimentModel(nn.Module):
    def __init__(self, vocab_size, embedding_dim, hidden_dim):
        super().__init__()

        # Embedding layer: converts word indices to vectors
        self.embedding = nn.Embedding(vocab_size, embedding_dim)

        # LSTM layer: processes sequence
        self.lstm = nn.LSTM(embedding_dim, hidden_dim, batch_first=True)

        # Fully connected layer: outputs prediction
        self.fc = nn.Linear(hidden_dim, 1)

        # Sigmoid: converts to probability
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        # x shape: (batch_size, seq_len)

        # Embedding: (batch_size, seq_len, embedding_dim)
        embedded = self.embedding(x)

        # LSTM: (batch_size, seq_len, hidden_dim)
        lstm_out, (hidden, cell) = self.lstm(embedded)

        # Use last hidden state
        # hidden shape: (1, batch_size, hidden_dim)
        hidden = hidden.squeeze(0)  # (batch_size, hidden_dim)

        # Fully connected
        output = self.fc(hidden)  # (batch_size, 1)

        # Sigmoid
        output = self.sigmoid(output)  # (batch_size, 1)

        return output.squeeze()  # (batch_size,)

# Create model
model = SentimentModel(
    vocab_size=vocab_size,
    embedding_dim=16,
    hidden_dim=32
)

print(model)
```

---

## 🎓 Step 4: Training

```python
import torch.optim as optim

# Loss and optimizer
criterion = nn.BCELoss()  # Binary Cross Entropy
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Training loop
epochs = 100
for epoch in range(epochs):
    # Forward pass
    outputs = model(X_train)
    loss = criterion(outputs, y_train)

    # Backward pass
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # Print progress
    if (epoch + 1) % 10 == 0:
        # Calculate accuracy
        predictions = (outputs > 0.5).float()
        accuracy = (predictions == y_train).float().mean()
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}, Accuracy: {accuracy.item():.4f}')
```

---

## 🔮 Step 5: Inference

```python
def predict_sentiment(text, model, vocab, max_len=10):
    """Predict sentiment of new text"""
    model.eval()  # Set to evaluation mode

    with torch.no_grad():
        # Preprocess
        indices = text_to_indices(text, vocab, max_len)
        x = torch.tensor([indices])  # Add batch dimension

        # Predict
        output = model(x)
        probability = output.item()

        # Interpret
        sentiment = "Positive" if probability > 0.5 else "Negative"
        confidence = probability if probability > 0.5 else 1 - probability

        return sentiment, confidence

# Test predictions
test_texts = [
    "This is amazing",
    "I hate this",
    "Great movie",
    "Terrible acting"
]

for text in test_texts:
    sentiment, confidence = predict_sentiment(text, model, vocab)
    print(f"Text: '{text}'")
    print(f"Sentiment: {sentiment} ({confidence:.2%} confidence)\n")
```

---

## 🚀 Using Pre-trained Models (Easier!)

For production, use pre-trained models from Hugging Face:

```python
from transformers import pipeline

# Load pre-trained sentiment analyzer (no API key!)
classifier = pipeline("sentiment-analysis")

# Predict
result = classifier("This movie is amazing!")
print(result)
# [{'label': 'POSITIVE', 'score': 0.9998}]

# Batch predictions
texts = [
    "I love this!",
    "This is terrible",
    "Not bad"
]

results = classifier(texts)
for text, result in zip(texts, results):
    print(f"{text}: {result['label']} ({result['score']:.2%})")
```

---

## 📊 Complete Example with Real Data

```python
# Using a small subset of IMDB reviews
from torch.utils.data import Dataset, DataLoader

class SentimentDataset(Dataset):
    def __init__(self, texts, labels, vocab, max_len=50):
        self.texts = texts
        self.labels = labels
        self.vocab = vocab
        self.max_len = max_len

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = self.texts[idx]
        label = self.labels[idx]

        # Convert to indices
        indices = text_to_indices(text, self.vocab, self.max_len)

        return torch.tensor(indices), torch.tensor(label, dtype=torch.float32)

# Create dataset and dataloader
dataset = SentimentDataset(
    texts=[text for text, _ in train_data],
    labels=[label for _, label in train_data],
    vocab=vocab,
    max_len=10
)

dataloader = DataLoader(dataset, batch_size=4, shuffle=True)

# Training with DataLoader
for epoch in range(50):
    total_loss = 0
    for batch_x, batch_y in dataloader:
        # Forward
        outputs = model(batch_x)
        loss = criterion(outputs, batch_y)

        # Backward
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    if (epoch + 1) % 10 == 0:
        avg_loss = total_loss / len(dataloader)
        print(f'Epoch [{epoch+1}/50], Avg Loss: {avg_loss:.4f}')
```

---

## 💡 Key Concepts

### Embedding Layer

Converts word indices to dense vectors:

```
Word: "movie" → Index: 5 → Vector: [0.2, -0.5, 0.8, ...]
```

### LSTM (Long Short-Term Memory)

Processes sequences and remembers context:

```
"This movie is great" → LSTM → Context-aware representation
```

### Binary Classification

Two classes (positive/negative):

```
Output > 0.5 → Positive
Output < 0.5 → Negative
```

---

## 🎯 Improvements

1. **Larger Dataset**: Use IMDB or other datasets
2. **Better Preprocessing**: Remove stopwords, stemming
3. **Pre-trained Embeddings**: Use GloVe or Word2Vec
4. **Deeper Model**: Add more LSTM layers
5. **Attention Mechanism**: Focus on important words
6. **Transfer Learning**: Use BERT or RoBERTa

---

## 📝 Quick Reference

| Component           | Purpose                    |
| ------------------- | -------------------------- |
| **Embedding**       | Convert words to vectors   |
| **LSTM**            | Process sequences          |
| **Fully Connected** | Make final prediction      |
| **Sigmoid**         | Convert to probability     |
| **BCE Loss**        | Binary classification loss |
| **Adam**            | Optimizer                  |

---

_Previous: [← Pre-trained Models](./05_models.md) | Next: [Complete Examples →](./07_examples.md)_
