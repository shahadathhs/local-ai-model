from transformers import pipeline
import torch

# Check if GPU is available
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# Load the T5 model and move it to the GPU if available
qa_pipeline = pipeline('text2text-generation', model='t5-small', device=0 if device == "cuda" else -1)

# Interactive Q&A loop
print("Ask a question! Type 'exit' to quit.")
while True:
    # Get user input
    user_input = input("You: ")
    
    # Exit the loop if the user types 'exit'
    if user_input.lower() == "exit":
        print("Goodbye!")
        break
    
    # Generate and print the AI's answer
    output = qa_pipeline(user_input)
    print(f"AI: {output[0]['generated_text']}\n")