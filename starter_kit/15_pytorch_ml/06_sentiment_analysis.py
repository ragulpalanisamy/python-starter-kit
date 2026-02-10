"""
PyTorch NLP - Sentiment Analysis with Transformers

Demonstrates:
- Using a pre-trained model for a high-level NLP task
- High-level 'pipeline' API vs manual tensor operations
"""

try:
    from transformers import pipeline
except ImportError:
    print("Transformers not installed. This example demonstrates high-level NLP.")
    print("Please install with: pip install transformers torch")
    exit(1)

def main():
    print("Initializing Sentiment Analysis pipeline...")
    # This will download the default model if not already present
    classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

    texts = [
        "I love learning new things with the Python Starter Kit!",
        "Struggling with bugs is frustrating, but solving them is great.",
        "The weather is quite dull today."
    ]

    print("\nRunning analysis:")
    for text in texts:
        result = classifier(text)[0]
        label = result['label']
        score = result['score']
        print(f"\nText: {text}")
        print(f"Result: {label} (Confidence: {score:.4f})")

if __name__ == "__main__":
    main()
