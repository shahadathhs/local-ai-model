# Local AI Model Chat

A guide to running AI models locally for interactive chat. This project supports models like GPT-2, GPT-Neo, T5, and others using Hugging Face Transformers.

## Folder Structure
```
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

## Prerequisites
- **Linux/macOS** (Windows support requires minor adjustments).
- **Python 3.8+**.
- `pip` (Python package manager).

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/shahadathhs/local-ai-model.git
cd local-ai-model
```

### 2. Set Up the Virtual Environment
```bash
python3 -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

### 3. Install Dependencies
Install required libraries:
```bash
pip install torch transformers
```

To save dependencies for later use:
```bash
pip freeze > requirements.txt
```

---

## Usage

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
Pre-written shell scripts in `run-scripts/` automate the process:
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

### 1. Use a Different Model
Modify the scripts to use models like `EleutherAI/gpt-neo-1.3B` or `facebook/bart-large`:
```python
# In chat_gpt2.py, change this line:
generator = pipeline('text-generation', model='gpt2')

# To:
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')
```

### 2. Adjust Response Parameters
Control response length, randomness, and quality:
```python
output = generator(
    user_input,
    max_length=100,          # Longer responses
    temperature=0.7,         # Lower = more deterministic
    top_k=50,                # Limit word choices
    truncation=True
)
```

---

## Troubleshooting

### 1. Model Not Downloading
- Ensure you have internet access.
- Check Hugging Face’s [Model Hub](https://huggingface.co/models) for the correct model name.

### 2. Out-of-Memory Errors
- Reduce `max_length`.
- Use a smaller model (e.g., `gpt2` instead of `gpt-neo`).

### 3. Slow Performance
- Use a GPU by installing CUDA-compatible PyTorch:
  ```bash
  pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113
  ```

## Script 1: `chat_gpt2.py` (GPT-2 Chat Script)

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

### How to edit with `nano` or `vim`:
1. Open the script in `nano`:
   ```bash
   nano chat-scripts/chat_gpt2.py
   ```
   - Use arrow keys to navigate.
   - Type your changes.
   - Save and exit by pressing `CTRL + X`, then `Y`, and `Enter`.

2. Use `vim` for advanced editing:
   ```bash
   vim chat-scripts/chat_gpt2.py
   ```
   - To edit, press `i` to enter insert mode, then make your changes.
   - To save and exit, press `ESC`, then type `:wq`, and press Enter.

---

## Script 2: `chat_t5.py` (T5 Question Answering Script)

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

---

## Script 3: `run_gpt2.sh` (Shell Script to Run GPT-2)

```bash
#!/bin/bash

# Activate the virtual environment
source myenv/bin/activate

# Run the GPT-2 script
python chat-scripts/chat_gpt2.py

# Deactivate the virtual environment
deactivate
```

### How to use:
1. Make it executable:
   ```bash
   chmod +x run-scripts/run_gpt2.sh
   ```
2. Run the script:
   ```bash
   ./run-scripts/run_gpt2.sh
   ```

---

## Script 4: `run_t5.sh` (Shell Script to Run T5)

```bash
#!/bin/bash

# Activate the virtual environment
source myenv/bin/activate

# Run the T5 script
python chat-scripts/chat_t5.py

# Deactivate the virtual environment
deactivate
```

### How to use:
1. Make it executable:
   ```bash
   chmod +x run-scripts/run_t5.sh
   ```
2. Run the script:
   ```bash
   ./run-scripts/run_t5.sh
   ```

---

## How to Edit Scripts Using `nano` or `vim`

### 1. Open a file with `nano`:
```bash
nano <path-to-your-file>
```
- Use the arrow keys to move around.
- Type your changes.
- To save and exit, press `CTRL + X`, then `Y`, and `Enter`.

### 2. Open a file with `vim`:
```bash
vim <path-to-your-file>
```
- Press `i` to enter insert mode and make changes.
- Press `Esc` to exit insert mode.
- To save and exit, type `:wq` and press `Enter`.
- To exit without saving, type `:q!` and press `Enter`.

---

## Customizing the Scripts

### 1. Change the Model:
For example, to use `EleutherAI/gpt-neo-1.3B` instead of GPT-2, modify the model loading line:
```python
# Original line
generator = pipeline('text-generation', model='gpt2')

# Modified line
generator = pipeline('text-generation', model='EleutherAI/gpt-neo-1.3B')
```

### 2. Adjust Response Parameters:
You can adjust response quality, length, and randomness:
```python
output = generator(
    user_input,
    max_length=100,          # Increase for longer responses
    temperature=0.7,         # Lower for more deterministic outputs
    top_k=50,                # Limit word choices for better responses
    truncation=True          # Handle long inputs gracefully
)
```
