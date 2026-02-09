# 🧮 Tensor Math & Broadcasting

> Neural networks are just massive piles of linear algebra. PyTorch makes this math easy, readable, and incredibly fast.

---

## 🖼️ Visual Architecture

![PyTorch: Tensor Math & Broadcasting](003_tensor_math.png)

## ➕ Basic Arithmetic

Element-wise operations are straightforward.

```python
x = torch.tensor([10, 20, 30])
y = torch.tensor([1, 2, 3])

print(x + y) # [11, 22, 33]
print(x * y) # [10, 40, 90] (Element-wise multiplication)
print(x / 5) # [2, 4, 6]
```

---

## ✖️ Matrix Multiplication

In Deep Learning, we almost never use element-wise multiplication (`*`) for weight updates. We use **Matrix Multiplication**.

| Feature          | Operator | Symbol           | Rule                        |
| :--------------- | :------- | :--------------- | :-------------------------- |
| **Element-wise** | `*`      | `torch.mul()`    | Must have same shape        |
| **Matrix Mul**   | `@`      | `torch.matmul()` | Inner dimensions must match |

```python
A = torch.randn(3, 2)
B = torch.randn(2, 4)

# Matrix multiplication
C = A @ B # Result Shape: (3, 4)
```

---

## 📡 Tensor Broadcasting

Broadcasting is a powerful tool that allows PyTorch to perform operations on tensors of different shapes.

### The Rule:

Two dimensions are compatible when:

1.  They are equal, **OR**
2.  One of them is **1**.

### Example:

If you add a tensor of shape `(3, 1)` and `(1, 4)`, PyTorch "stretches" them to `(3, 4)` and adds them!

```python
x = torch.tensor([[10], [20], [30]]) # Shape: (3, 1)
y = torch.tensor([1, 2, 3, 4])       # Shape: (4)

# Result will be a (3, 4) matrix!
z = x + y
```

---

## 📉 Common Reductions

- `tensor.sum()`: Total of all elements.
- `tensor.mean()`: Average (requires float tensor).
- `tensor.max()` / `tensor.min()`.
- `tensor.argmax()`: Returns the **index** of the maximum value (extremely common in classification!).

---

_You've completed the Tensor journey! Next, explore how PyTorch uses these for [Neural Networks](../index.md)._
