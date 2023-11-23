# More Examples
Before moving onto [05_fast_api](/05_fast_api/README.md) to learn about hosting Llama 2 as an API, this folder contains some further examples that have been useful for learning Llama 2. 

## Step 1: Install Pre-reqs
- Install [Rust](https://rustup.rs/)
- Install Python 3.11.6 (not 3.12 as its not supported for pytorch on Windows)
- Install dependencies
```Python
pip install llama-cpp-python pypdf sentence-transformers chromadb langchain pypdf torch
```
- Additional help here for [PyTorch](https://gist.github.com/vandbt/62e137881a9e2014d4ded452d3e8e8dd
https://download.pytorch.org/whl/cpu/torch/)

## Step 2: Run Examples
| Example Script | Description |
| ------ | ------| 
| hello_llama_2.py | Simple "Hello World!" script for Llama2. | 
| prompting_llama_2.py | Simple Prompt and Answer technique for Llama 2. |
| who_are_you.py| Ask Llama 2 who it is. | 
| control_who_are_you.py | Load a PDF document that controls Llama 2's response. |