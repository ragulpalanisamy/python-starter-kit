import torch
import numpy as np

def run_basics():
    print("=== 1. Tensor Creation ===")
    
    # 1. From a list
    tensor_from_list = torch.tensor([1, 2, 3])
    print(f"List Tensor: {tensor_from_list}")
    
    # 2. Random tensors
    rand_tensor = torch.rand(2, 3) # Shape(2,3)
    print(f"Random (0-1):\n{rand_tensor}")
    
    # 3. Zeros and Ones
    ones_tensor = torch.ones(2, 2)
    print(f"Ones:\n{ones_tensor}")
    
    # 4. From NumPy
    np_arr = np.array([4, 5, 6])
    tensor_from_np = torch.from_numpy(np_arr)
    print(f"From NumPy: {tensor_from_np}")

    print("\n=== 2. Indexing & Slicing ===")
    data = torch.tensor([[1, 2, 3], [4, 5, 6]])
    print(f"Original Tensor:\n{data}")
    print(f"Row 0: {data[0, :]}")
    print(f"Col 1: {data[:, 1]}")
    print(f"Element [1,2]: {data[1, 2]}")

    print("\n=== 3. Attributes ===")
    print(f"Shape: {data.shape}")
    print(f"Type: {data.dtype}")
    print(f"Device: {data.device}")

if __name__ == "__main__":
    run_basics()
