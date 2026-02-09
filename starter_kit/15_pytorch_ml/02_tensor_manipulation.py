import torch

def run_manipulation():
    print("=== 1. Reshaping ===")
    x = torch.arange(12)
    print(f"Original (0-11): {x}")
    
    # Reshape to 3x4
    reshaped = x.reshape(3, 4)
    print(f"Reshaped (3x4):\n{reshaped}")
    
    # Auto-calculate dimension with -1
    auto_reshaped = x.reshape(2, -1)
    print(f"Auto Reshaped (2x6):\n{auto_reshaped}")

    print("\n=== 2. Squeeze & Unsqueeze ===")
    batch = torch.tensor([1, 2, 3])
    print(f"Original shape: {batch.shape}")
    
    unsqueezed = batch.unsqueeze(dim=0)
    print(f"Unsqueezed (dim=0) shape: {unsqueezed.shape}")
    
    squeezed = unsqueezed.squeeze()
    print(f"Back to squeezed shape: {squeezed.shape}")

    print("\n=== 3. Concat & Stack ===")
    a = torch.tensor([[1, 2]])
    b = torch.tensor([[3, 4]])
    
    concatenated = torch.cat((a, b), dim=0) # join on existing dim
    print(f"Concatenated (dim=0):\n{concatenated}")
    
    stacked = torch.stack((a, b)) # join on NEW dim
    print(f"Stacked (Result is 3D):\n{stacked}")
    print(f"Stacked shape: {stacked.shape}")

if __name__ == "__main__":
    run_manipulation()
