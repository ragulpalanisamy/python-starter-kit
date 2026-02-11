# 🏁 Introduction to PyTorch & Deep Learning

> **Welcome to the world of Deep Learning!** Before we dive into code, let's understand the landscape of neural networks and the frameworks we use to build them.

---

## 🖼️ Visual Architecture

![PyTorch ML Architecture](000_intro.png)

## 🧠 Neural Networks Recap

At its core, a **Neural Network** is a mathematical function that learns to map inputs to outputs by mimicking the human brain's structure.

### The Basic Components:

1.  **Neurons (Nodes):** The basic unit that receives input, processes it, and passes it on.
2.  **Weights & Biases:** The "knobs" the model turns to learn. Weights determine how much influence an input has, and biases shift the activation.
3.  **Layers:**
    - **Input Layer:** Receives the raw data.
    - **Hidden Layers:** Where the "magic" (math) happens.
    - **Output Layer:** Provides the final prediction.
4.  **Activation Functions:** Functions like **ReLU - (Rectified Linear Unit)** or **Sigmoid** that decide if a neuron should "fire."

---

## 🏗️ Deep Learning Frameworks

Building a neural network from scratch using just Python lists or NumPy is possible but extremely slow and complex for large models. Frameworks provide:

- **Optimized Math:** Fast matrix operations on CPU/GPU.
- **Autograd:** Automatically calculating gradients (no more manual calculus!).
- **Standard Layers:** Pre-built pieces like `Linear` or `Convolutional`.

---

## ⚔️ TensorFlow vs. PyTorch

There are two main giants in the AI world. Here is how they compare:

| Feature            | 🔥 PyTorch                    | ❄️ TensorFlow                 |
| :----------------- | :---------------------------- | :---------------------------- |
| **Philosopy**      | Imperative (Natural Python)   | Declarative (Static Graphs\*) |
| **Debugging**      | Easy (Standard Python tools)  | Harder (Specialized tools)    |
| **Popularity**     | Dominant in Research/Academia | Strong in Industry/Production |
| **Learning Curve** | Gentle (Feels like NumPy)     | Steeper (Can be verbose)      |
| **Dynamic?**       | ✅ Fully Dynamic              | ⚠️ Hybrid (Eager mode)        |

> **Why we use PyTorch here:** It is "Pythonic"—it feels like writing regular Python code. If you know how to use a `for` loop, you're halfway to understanding a PyTorch training loop!

---

## 🛤️ The Roadmap

We will follow this path to master PyTorch:

1.  **Tensors:** The fundamental data structure.
2.  **Manipulation:** Reshaping and squeezing data.
3.  **Math:** Matrix operations and broadcasting.
4.  **Autograd:** How PyTorch learns.
5.  **Building Models:** Putting it all together.

---

_Next Up: [Tensor Basics](./01_tensor_basics.md)_
