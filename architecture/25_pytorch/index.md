# 🔥 PyTorch Machine Learning

> **Deep Learning with PyTorch** - From tensors to neural networks

---

## 📖 What is PyTorch?

**PyTorch** is an open-source machine learning framework developed by Facebook's AI Research lab. It's widely used for deep learning and neural networks.

```
┌─────────────────────────────────────────────────────────────┐
│                    Why PyTorch?                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  🐍 Pythonic: Feels natural to Python developers            │
│  ⚡ Dynamic: Build models on-the-fly                        │
│  🎓 Research: Preferred in academia and research            │
│  🚀 Production: Easy deployment with TorchScript            │
│  📊 GPU: Seamless GPU acceleration                          │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## 🏗️ PyTorch Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                    Your Python Code                          │
│                                                              │
│  • Define model architecture                                │
│  • Load data                                                │
│  • Train model                                              │
└───────────────────────┬──────────────────────────────────────┘
                        │
                        ▼
┌──────────────────────────────────────────────────────────────┐
│                  PyTorch Framework                           │
│                                                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Tensors    │  │  Autograd    │  │  nn.Module   │      │
│  │  (Data)      │  │  (Gradients) │  │  (Models)    │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└───────────────────────┬──────────────────────────────────────┘
                        │
        ┌───────────────┴───────────────┐
        ▼                               ▼
┌──────────────┐              ┌──────────────┐
│     CPU      │              │     GPU      │
│  (Slower)    │              │  (Faster!)   │
└──────────────┘              └──────────────┘
```

---

## 🎯 Core Concepts

### 1. Tensors

Multi-dimensional arrays (like NumPy, but with GPU support).

```python
import torch

# Create tensors
x = torch.tensor([1, 2, 3])
y = torch.zeros(3, 4)  # 3x4 matrix of zeros
z = torch.randn(2, 3)  # Random normal distribution

# Move to GPU (if available)
if torch.cuda.is_available():
    x = x.cuda()
```

---

### 2. Autograd (Automatic Differentiation)

PyTorch automatically computes gradients for backpropagation.

```python
# Enable gradient tracking
x = torch.tensor([2.0], requires_grad=True)

# Forward pass
y = x ** 2  # y = x²

# Backward pass (compute gradients)
y.backward()

# Gradient: dy/dx = 2x = 2*2 = 4
print(x.grad)  # tensor([4.])
```

---

### 3. Neural Networks (nn.Module)

Build models by subclassing `nn.Module`.

```python
import torch.nn as nn

class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(10, 5)  # Input: 10, Output: 5
        self.fc2 = nn.Linear(5, 1)   # Input: 5, Output: 1

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

model = SimpleNet()
```

---

### 4. Training Loop

Standard pattern for training neural networks.

```python
# 1. Forward pass
outputs = model(inputs)

# 2. Compute loss
loss = criterion(outputs, targets)

# 3. Backward pass
optimizer.zero_grad()  # Clear gradients
loss.backward()        # Compute gradients

# 4. Update weights
optimizer.step()
```

---

## 🤖 Use Cases

### Text Classification (Sentiment Analysis)

```
Input: "This movie is amazing!"
         ↓
    Tokenization
         ↓
    Word Embeddings
         ↓
    Neural Network
         ↓
Output: Positive (0.95 confidence)
```

### Image Classification

```
Input: Image of a cat
         ↓
    Convolutional Layers
         ↓
    Feature Extraction
         ↓
    Fully Connected Layers
         ↓
Output: Cat (0.98 confidence)
```

---

## 📊 PyTorch Workflow

```
1. Prepare Data
   ↓
   Load dataset, create DataLoader

2. Define Model
   ↓
   Create nn.Module subclass

3. Set Loss & Optimizer
   ↓
   Choose loss function and optimizer

4. Training Loop
   ↓
   Forward → Loss → Backward → Update

5. Evaluation
   ↓
   Test on validation data

6. Inference
   ↓
   Make predictions on new data
```

---

## 🔧 Key Components

### Layers

```python
# Fully connected (dense) layer
nn.Linear(in_features, out_features)

# Convolutional layer (for images)
nn.Conv2d(in_channels, out_channels, kernel_size)

# Recurrent layer (for sequences)
nn.LSTM(input_size, hidden_size)

# Dropout (regularization)
nn.Dropout(p=0.5)
```

### Activation Functions

```python
# ReLU (most common)
nn.ReLU()

# Sigmoid (for binary classification)
nn.Sigmoid()

# Softmax (for multi-class classification)
nn.Softmax(dim=1)

# Tanh
nn.Tanh()
```

### Loss Functions

```python
# Mean Squared Error (regression)
nn.MSELoss()

# Cross Entropy (classification)
nn.CrossEntropyLoss()

# Binary Cross Entropy
nn.BCELoss()
```

### Optimizers

```python
# Stochastic Gradient Descent
torch.optim.SGD(model.parameters(), lr=0.01)

# Adam (adaptive learning rate)
torch.optim.Adam(model.parameters(), lr=0.001)

# AdamW (Adam with weight decay)
torch.optim.AdamW(model.parameters(), lr=0.001)
```

---

## 🎓 Learning Path

| Step | Topic                       | Documentation                                      | Code Examples (run with `uv run`)                                         |
| :--- | :-------------------------- | :------------------------------------------------- | :------------------------------------------------------------------------ |
| 0    | **Intro & Background**      | [View Guide](./learning/00_introduction.md)        | -                                                                         |
| 1    | **Tensor Basics**           | [View Guide](./learning/01_tensor_basics.md)       | [Explore Code](../../starter_kit/15_pytorch_ml/01_tensor_basics.py)       |
| 2    | **Tensor Manipulation**     | [View Guide](./learning/02_tensor_manipulation.md) | [Explore Code](../../starter_kit/15_pytorch_ml/02_tensor_manipulation.py) |
| 3    | **Tensor Math & Broadcast** | [View Guide](./learning/03_tensor_math.md)         | [Explore Code](../../starter_kit/15_pytorch_ml/03_tensor_math.py)         |
| 4    | **Training Loops**          | [View Guide](./learning/04_training.md)            | -                                                                         |
| 5    | **Full Project: Sentiment** | [View Guide](./learning/06_sentiment_analysis.md)  | -                                                                         |

---

## 🚀 Quick Start

If you have **uv** installed, you can run the examples without manually installing anything:

```bash
uv run --with torch --with numpy starter_kit/15_pytorch_ml/01_tensor_basics.py
```

### Manual Example

```python
import torch
import torch.nn as nn
import torch.optim as optim

# 1. Create simple dataset
X = torch.randn(100, 10)  # 100 samples, 10 features
y = torch.randn(100, 1)   # 100 targets

# 2. Define model
model = nn.Sequential(
    nn.Linear(10, 5),
    nn.ReLU(),
    nn.Linear(5, 1)
)

# 3. Loss and optimizer
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.01)

# 4. Training loop
for epoch in range(100):
    # Forward
    outputs = model(X)
    loss = criterion(outputs, y)

    # Backward
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch + 1) % 10 == 0:
        print(f'Epoch [{epoch+1}/100], Loss: {loss.item():.4f}')

# 5. Make prediction
with torch.no_grad():
    test_input = torch.randn(1, 10)
    prediction = model(test_input)
    print(f'Prediction: {prediction.item():.4f}')
```

---

## 💡 PyTorch vs TensorFlow

| Aspect             | PyTorch                | TensorFlow         |
| ------------------ | ---------------------- | ------------------ |
| **Style**          | Pythonic, dynamic      | More verbose       |
| **Debugging**      | Easy (Python debugger) | Harder             |
| **Research**       | Preferred              | Less common        |
| **Production**     | TorchScript            | TensorFlow Serving |
| **Learning Curve** | Easier                 | Steeper            |
| **Community**      | Growing fast           | Larger             |

---

## 🔗 Resources

- [Official PyTorch Documentation](https://pytorch.org/docs/)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/)
- [PyTorch Examples](https://github.com/pytorch/examples)

---

## 🎯 Quick Reference

### Essential Operations

| Operation         | Code                      | Description      |
| ----------------- | ------------------------- | ---------------- |
| **Create tensor** | `torch.tensor([1, 2, 3])` | Create from list |
| **Random tensor** | `torch.randn(3, 4)`       | Random normal    |
| **Zeros**         | `torch.zeros(3, 4)`       | All zeros        |
| **To GPU**        | `tensor.cuda()`           | Move to GPU      |
| **To CPU**        | `tensor.cpu()`            | Move to CPU      |
| **Shape**         | `tensor.shape`            | Get dimensions   |
| **Reshape**       | `tensor.view(2, -1)`      | Change shape     |

---

_Updated: Feb 2026_
