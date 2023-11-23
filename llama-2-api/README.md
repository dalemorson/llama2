# Hosting Llama 2 as an API
 https://github.com/abetlen/llama-cpp-python
 https://abetlen.github.io/llama-cpp-python/

## Installation

```Python
# Create a virtual environment if required
python -m venv .venv

# Activate the virtual environment
.venv/Scripts/activate

# Install requirements
pip install llama-cpp-python llama-cpp-python[server]
```

## Run the llama-cpp-python Server

```Python
python -m llama_cpp.server --model models/7B/llama-2-7b-chat.Q8_0.gguf
```

## View the OpenAPI Docs

Navigate to http://localhost:8000/docs to see the OpenAPI documentation.