# Quickstart to using Llama 2
This page describes how to interact with the Llama 2 large language model (LLM) locally using Python, without requiring internet, registration, or API keys. We will deliver prompts to the model and get AI-generated chat responses using the llama-cpp-python package.

## Step 1: Download a Large Language Model
The Llama 2 model can be downloaded in [GGML format](https://github.com/ggerganov/ggml) from Hugging Face:

Model I’m using: llama-2-7b-chat.Q8_0.gguf (7 GB)

All models: [Llama-2-7B-Chat-GGML/tree/main](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main)

Model descriptions: [Readme](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML#provided-files)

It is 7 GB in size and requires 10 GB of ram to run. Developers should experiment with different models, as simpler models may run faster and produce similar results for less complex tasks.

## Step 2: Prepare the Python Environment
- Install the latest version of Python from [python.org](https://www.python.org/) or your favourite package manager

- Create a [virtual environment](https://docs.python.org/3/library/venv.html): ```python -m venv .venv```

- Activate the virtual environment: ```.venv/Scripts/activate```

- Install the llama-cpp-python package: ```pip install llama-cpp-python```

**Installation will fail if a C++ compiler cannot be located.** To get one:

- Windows: Install Visual Studio Community with the “Desktop development with C++” workload. It is free for individuals an open-source developers. See the C++ installation guide for more information.

- Linux: apt install python3-dev

- MacOS: brew install python3-dev

## Step 3: Interact with the Llama 2 large language model
Create a new python script and run it inside the virtual environment:

```Python
# load the large language model file
from llama_cpp import Llama
LLM = Llama(model_path="./llama-2-7b-chat.Q8_0.gguf")

# create a text prompt
prompt = "Q: What are the names of the days of the week? A:"

# generate a response (takes several seconds)
output = LLM(prompt)

# display the response
print(output["choices"][0]["text"])
```
It took my system 7 seconds to generate this response:

**Question:** What are the names of the days of the week?

**Answer:** The names of the days of the week, in order, are: Monday Tuesday Wednesday Thursday Friday Saturday Sunday