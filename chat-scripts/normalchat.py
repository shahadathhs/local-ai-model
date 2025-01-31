from transformers import pipeline
import torch

# Check if GPU is available
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Load the model and move it to the appropriate device
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B', device=0 if device == "cuda" else -1)

# Define a function to generate AI response
def generate_response(user_input):
    output = generator(
        user_input,
        num_return_sequences=1,  # Only one response
        temperature=0.7,  # Less randomness for coherence
        top_k=50,  # Limit word choices for quality
        truncation=True  # Handle long inputs gracefully
    )
    return output[0]['generated_text']

# Interactive chat loop
print("Chat with the AI! Type 'exit' to quit.")
while True:
    # Get user input
    user_input = input("You: ")
    
    # Exit the loop if the user types 'exit'
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    
    # Generate and display the AI's response
    ai_response = generate_response(user_input)
    print(f"AI: {ai_response}\n")
