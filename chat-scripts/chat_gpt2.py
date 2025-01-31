from transformers import pipeline
import torch

# Check if GPU is available
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Load the GPT-2 model and move it to the GPU if available
generator = pipeline('text-generation', model='gpt2', device=0 if device == "cuda" else -1)

# Interactive chat loop
print("Chat with the AI! Type 'exit' to quit.")
while True:
    # Get user input
    user_input = input("You: ")
    
    # Exit the loop if the user types 'exit'
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    
    # Generate and print the AI's response
    output = generator(user_input, num_return_sequences=1, temperature=0.7, top_k=50, truncation=True)
    print(f"AI: {output[0]['generated_text']}\n")