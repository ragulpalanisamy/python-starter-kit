import torch

def run_math():
    print("=== 1. Matrix Multiplication ===")
    mat_a = torch.tensor([[1, 2], [3, 4]])
    mat_b = torch.tensor([[10, 20], [30, 40]])
    
    # Standard multiplication (Element-wise)
    print(f"Element-wise (mat_a * mat_b):\n{mat_a * mat_b}")
    
    # Matrix Multiplication (@ or matmul)
    print(f"Matrix Mul (mat_a @ mat_b):\n{mat_a @ mat_b}")

    print("\n=== 2. Broadcasting ===")
    table = torch.zeros(3, 3) 
    row = torch.tensor([1, 2, 3]) # shape (3)
    
    # Row is "stretched" to (3,3) automatically
    result = table + row
    print(f"Broadcasting row into zeros table:\n{result}")

    print("\n=== 3. Argmax (Essential for AI) ===")
    probs = torch.tensor([0.1, 0.7, 0.2])
    prediction = torch.argmax(probs)
    print(f"Probabilities: {probs}")
    print(f"Model predicted Class Index: {prediction.item()}")

if __name__ == "__main__":
    run_math()
