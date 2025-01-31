# Local AI Model Chat Guide

This guide provides detailed instructions on how to set up, run, and customize AI models locally for interactive chat. It supports models like GPT-2, GPT-Neo, T5, and others using the Hugging Face Transformers library.

## Folder Structure

```plaintext
local-ai-model/
├── myenv/                   # Virtual environment (excluded via .gitignore)
├── chat-scripts/            # Python scripts for interacting with models
│   ├── chat_gpt2.py         # Example: GPT-2 chat script
│   └── chat_t5.py           # Example: T5 question-answering script
├── run-scripts/             # Shell scripts to activate and run models
│   ├── run_gpt2.sh          # Script to run GPT-2
│   └── run_t5.sh            # Script to run T5
├── .gitignore               # Ignores myenv/, downloaded models, and cache
└── README.md                # This guide
```

---

## Prerequisites

- **Operating System**: Linux/macOS (Windows requires minor adjustments).
- **Python**: Version 3.8 or higher.
- **Package Manager**: `pip` for installing Python libraries.

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/shahadathhs/local-ai-model.git
cd local-ai-model
```

### 2. Set Up the Virtual Environment
Create a Python virtual environment to isolate dependencies:
```bash
python3 -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

### 3. Install Dependencies
Install the required libraries (`torch` and `transformers`):
```bash
pip install torch transformers
```

To save the dependencies for future reference:
```bash
pip freeze > requirements.txt
```

---

## Running the Scripts Locally

### 1. Run a Chat Script

#### Example: GPT-2
- **Script**: `chat-scripts/chat_gpt2.py`
- **Run Command**:
  ```bash
  # Activate the virtual environment
  source myenv/bin/activate
  
  # Run the script
  python chat-scripts/chat_gpt2.py
  
  # Deactivate the virtual environment
  deactivate
  ```

#### Example: T5 (Question Answering)
- **Script**: `chat-scripts/chat_t5.py`
- **Run Command**:
  ```bash
  python chat-scripts/chat_t5.py
  ```

### 2. Use Run Scripts (Optional)
Pre-written shell scripts in `run-scripts/` automate the process of activating the environment and running the models:
```bash
# Make scripts executable
chmod +x run-scripts/*.sh

# Run GPT-2
./run-scripts/run_gpt2.sh

# Run T5
./run-scripts/run_t5.sh
```

---

## Customization

### 1. Switch to a Different Model
You can modify the scripts to use alternative models like `EleutherAI/gpt-neo-1.3B` or `facebook/bart-large` by changing the model name in the script:
```python
# In chat_gpt2.py, change this line:
generator = pipeline('text-generation', model='gpt2')

# To:
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')
```

### 2. Adjust Response Parameters
You can fine-tune the responses by adjusting parameters like response length, temperature (randomness), and top-k sampling:
```python
output = generator(
    user_input,
    max_length=100,          # Increase for longer responses
    temperature=0.7,         # Lower for more deterministic outputs
    top_k=50,                # Limit word choices for better responses
    truncation=True
)
```

---

## Troubleshooting

### 1. Model Not Downloading
- Ensure that your internet connection is stable.
- Check the correct model name on Hugging Face’s [Model Hub](https://huggingface.co/models).

### 2. Out-of-Memory Errors
- Reduce the `max_length` parameter to avoid excessive memory usage.
- Switch to a smaller model (e.g., use `gpt2` instead of `gpt-neo`).

### 3. Slow Performance
- Install the CUDA-compatible version of PyTorch if you have a GPU:
  ```bash
  pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113
  ```

---

## Scripts Overview

### Script 1: `chat_gpt2.py` (GPT-2 Chat Script)

This script uses the GPT-2 model for generating responses interactively.

```python
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
```

### Script 2: `chat_t5.py` (T5 Question Answering Script)

This script uses the T5 model for answering questions based on user input.

```python
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
```

### Script 3: `run_gpt2.sh` (Shell Script to Run GPT-2)

This shell script automates the process of activating the environment and running the GPT-2 script.

```bash
#!/bin/bash

# Activate the virtual environment
source myenv/bin/activate

# Run the GPT-2 script
python chat-scripts/chat_gpt2.py

# Deactivate the virtual environment
deactivate
```

### Script 4: `run_t5.sh` (Shell Script to Run T5)

This shell script automates the process of activating the environment and running the T5 script.

```bash
#!/bin/bash

# Activate the virtual environment
source myenv/bin/activate

# Run the T5 script
python chat-scripts/chat_t5.py

# Deactivate the virtual environment
deactivate
```

---

## How to Edit Scripts Using `nano` or `vim`

### 1. Edit with `nano`:
To edit a script with `nano`, run:
```bash
nano <path-to-your-file>
```
- Use arrow keys to move around.
- Type your changes.
- Save and exit by pressing `CTRL + X`, then `Y`, and `Enter`.

### 2. Edit with `vim`:
To edit a script with `vim`, run:
```bash
vim <path-to-your-file>
```
- Press `i` to enter insert mode and make changes.
- Press `Esc` to exit insert mode.
- To save and exit, type `:wq` and press Enter.
- To exit without saving, type `:q!` and press Enter.

---

## Customizing the Scripts

### 1. Switch Models:
To use a different model, simply update the model name:
```python
# Change this line
generator = pipeline('text-generation', model='gpt2')

# To use a different model
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')
```

### 2. Adjust Response Parameters:
Control response length, randomness, and quality:
```python
output = generator(
    user_input,
    max_length=100,          # Increase for longer responses
    temperature=0.7,         # Lower for more deterministic outputs
    top_k=50,                # Limit word choices for better responses
    truncation=True          # Handle long inputs gracefully
)
```

By following this guide, you can run AI models locally, customize them for your needs, and troubleshoot common issues.