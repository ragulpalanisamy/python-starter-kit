"""
PyTorch Training - A Simple Linear Regression Loop

Demonstrates:
1. Creating a synthetic dataset
2. Defining a simple model (Linear Layer)
3. Defining Loss Function and Optimizer
4. The Training Loop (Forward, Loss, Backward, Step)
"""

try:
    import torch
    import torch.nn as nn
    import torch.optim as optim
except ImportError:
    print("PyTorch not installed. Please install it with 'pip install torch'")
    exit(1)

def main():
    # 1. Create Synthetic Data (y = 2x + 1 + noise)
    X = torch.randn(100, 1) * 10
    y = 2 * X + 1 + torch.randn(100, 1) * 2

    # 2. Define a Simple Model
    # A linear layer with 1 input and 1 output
    model = nn.Linear(1, 1)

    # 3. Define Loss Function (Mean Squared Error) and Optimizer (Stochastic Gradient Descent)
    criterion = nn.MSELoss()
    optimizer = optim.SGD(model.parameters(), lr=0.01)

    # 4. Training Loop
    epochs = 100
    print(f"Starting training for {epochs} epochs...")

    for epoch in range(epochs):
        # Forward pass: Compute predicted y by passing x to the model
        y_pred = model(X)

        # Compute loss
        loss = criterion(y_pred, y)

        # Zero gradients, perform a backward pass, and update the weights.
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if (epoch + 1) % 10 == 0:
            print(f"Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}")

    # 5. Result
    [w, b] = model.parameters()
    print(f"\nTraining Complete!")
    print(f"Final Model: y = {w[0][0]:.4f}x + {b[0]:.4f}")
    print(f"Expected:     y = 2.0000x + 1.0000")

if __name__ == "__main__":
    main()
