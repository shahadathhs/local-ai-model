import torch
from transformers import pipeline

# Check if GPU is available
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}\n")

# Load the pipeline model and move it to the appropriate device
generator = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B", device=0 if device == "cuda" else -1, trust_remote_code=True)

# Initialize chat memory
chat_history = []

def chat():
    print("\nChatbot is ready! Type 'exit' to quit.\n")
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        
        # Append user message to chat history
        chat_history.append({"role": "user", "content": user_input})
        
        # Generate response
        response = generator(user_input, max_length=150, num_return_sequences=1)[0]['generated_text']
        
        # Append chatbot response to chat history
        chat_history.append({"role": "assistant", "content": response})
        
        print(f"Chatbot: {response}\n")

if __name__ == "__main__":
    chat()
