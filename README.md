# :llama: Llama 2

<!-- TOC -->

- [Llama 2](#llama-2)
    - [What is Llama 2?](#what-is-llama-2)
    - [Getting Involved!](#getting-involved)
    - [Try it out!](#try-it-out)
    - [Useful Frameworks and Libraries](#useful-frameworks-and-libraries)
- [CPU vs GPU Comparisons](#cpu-vs-gpu-comparisons)
- [Limitations](#limitations)
- [Additional Resources](#additional-resources)
    - [Getting Started and Reading](#getting-started-and-reading)
    - [Github](#github)
    - [Python](#python)
    - [Performance & Latency](#performance--latency)
    - [Fine Tuning and Chunking](#fine-tuning-and-chunking)
    - [Others](#others)
- [Glossary](#glossary)

<!-- /TOC -->

## What is Llama 2?
Llama 2 is Meta's open source large language model (LLM). It's basically the Facebook parent company's response to OpenAI's GPT models and Google's AI models like PaLM 2—but with one key difference: it's freely available for almost anyone to use for research and commercial purposes.

Meta have a great [Getting Started](https://ai.meta.com/llama/get-started/) page as well as a [Getting to Know LLama](https://github.com/facebookresearch/llama-recipes/blob/main/examples/Getting_to_know_Llama.ipynb) Juypter book.

## Getting Involved!
- Please raise a pull request if you'd like to contribute to this repo.
- Or, raise an Issue if you'd like request new scripts, demos etc.

## Try it out!
I've provided some getting started scripts in this repo covering various topics, frameworks and libraries.
| Links | Description |
| ------ | ------ |
| [quick_start](/quick_start/README.md) | Learn the basics of Llama 2 with a question and answer response locally using Python, without requiring internet, registration, or API keys. |
| [local_data_ingestion](/local_data_ingestion/README.md) | Following on from the quick start, this example will use locally ingested data. Use [Llama Hub](https://llamahub.ai/) for more custom data sources and plugins for [LlamaIndex](https://www.llamaindex.ai/) and [LangChain](https://www.langchain.com/). | 
| [more_examples](/more_examples/README.md) | Some further examples like HelloLlama, using prompts, who are you? and loading a PDF document. | 
| [llamaindex](/llamaindex/README.md) | Learn how to use [LlamaIndex](https://www.llamaindex.ai/) to ingest and index log data from [LogHub](https://github.com/logpai/loghub). |
| [langchain](/langchain/README.md) | [LangChain](https://www.langchain.com/) is an open source framework for building LLM powered applications. |
| [chunking](/chunking/README.md) | Chunking data with LlamaIndex. | 
| [performance_fine_tuning](/performance_fine_tuning/README.md) | How to improve memory and computing limitations running Llama 2 locally.  | 
| [cloud_hosting](/cloud_hosting/README.md) | A look into cloud hosting options for Llama 2. | 
| [summarisation](/summarisation/README.md) | A deeper look into summarising data. |
| [fast_api](/fast_api/README.md) | Serve Llama 2 as a hosted Rest API using the [FastAPI](https://fastapi.tiangolo.com/) framework. |
| [hosting_llm_api](/hosting_llm_api/README.md) | Other options for hosting Llama 2 as an API. |
| [code_llama](/code_llama/README.md) | Code Llama is an AI model built on top of Llama 2, fine-tuned for generating and discussing code. |
| [soar_insights_api](/soar_insights_api/README.md) | An experimental Llama 2 REST API to provide summarisation of SOAR data and provide insights. | 

## Useful Frameworks and Libraries
| Links | Description |
| ------ | ------ |
| [Llama Hub](https://llamahub.ai/) | Connect custom data sources to your LLM with one or more of these plugins (via LlamaIndex or LangChain. ) |
| [LangChain](https://www.langchain.com/) | Build context-aware, reasoning applications with LangChain’s flexible abstractions and AI-first toolkit. |
| [Llama-cpp-python](https://github.com/abetlen/llama-cpp-python) | Simple Python bindings for @ggerganov's llama.cpp library.  | 
| [vLLM](https://github.com/vllm-project/vllm) | Easy, fast, and cheap LLM serving for everyone. |
| [HuggingFace](https://huggingface.co/) | The platform where the machine learning community collaborates on models, datasets, and applications. |
| [FastAPI](https://fastapi.tiangolo.com/) | FastAPI framework, high performance, easy to learn, fast to code, ready for production | 
| [Code Llama](https://about.fb.com/news/2023/08/code-llama-ai-for-coding/) | Code Llama is an AI model built on top of Llama 2, fine-tuned for generating and discussing code. |

# CPU vs GPU Comparisons
With a decent CPU but without any GPU assistance, expect output on the order of 1 token per second, and excruciatingly slow prompt ingestion. Any decent Nvidia GPU will dramatically speed up ingestion, but for fast generation, you need 48GB VRAM to fit the entire model. That means 2x RTX 3090 or better.

| Azure Virtual Machine Size      | CPU | GPU | Time to Response in ms |
| ----------- | ----------- | ----------- | ----------- |
| Standard_D4s_v4 | Intel(R) Xeon(R) Platinum 8272CL CPU @ 2.60GHz | None | xxxx ms |
| NC4as_T4_v3   | Intel(R) Xeon(R) Platinum 8272CL CPU @ 2.60GHz | 16GB Nvidia Tesla T4 GPU | xxxx ms |

# Limitations


# Additional Resources

## Getting Started and Reading
| Link | Description |
| ------ | ------ |
| [Official Meta AI Page](https://ai.meta.com/llama/get-started/) | Start here to start learning Llama 2. |
| [Learn Llama 2, LangChain and LlamaIndex](https://llama-2.ai/getting-started-with-llama-2/) | Great read on Llama 2, LangChain and LlamaIndex. |
| [HackerNoon](https://hackernoon.com/my-experience-with-llama2-both-as-a-developer-and-a-hacker) | My Experience With LLama2 Both as a Developer and a Hacker| 

## Github
| Repo | Description |
| ------ | ------ |
| [facebookresearch/llama](https://github.com/facebookresearch/llama) | Main Llama 2 repo |
| [facebookresearch/llama-recipes](https://github.com/facebookresearch/llama-recipes/)| Llama 2 Fine-tuning / Inference Recipes, Examples and Demo Apps |
| [mirpo/fastapi-gen](https://github.com/mirpo/fastapi-gen/) | Create LLM-enabled FastAPI applications without build configuration. |
| [Dicklesworthstone/swiss_army_llama](https://github.com/Dicklesworthstone/swiss_army_llama) | The Swiss Army Llama is designed to facilitate and optimize the process of working with local LLMs by using FastAPI to expose convenient REST endpoints for various tasks. |
| [mowa-ai/llm-as-a-service](https://github.com/mowa-ai/llm-as-a-service) | Simple FastAPI service for LLAMA-2 7B chat model. |
| [chrisswhitneyy/desert-llama](https://github.com/chrisswhitneyy/desert-llama)| This repo contains the code for the a toy project called Desert Llama that is a simple web app to interact with the Llama lanuage model. The code is split into two parts: the backend and the frontend. The backend is written in Python and FastAPI. The frontend is written in Javascript using React and Next.js. | 
| [unconv/llama2-flask-api](https://github.com/unconv/llama2-flask-api)| This is a simple HTTP API for the Llama 2 LLM. |
| [mudler/LocalAI](https://github.com/mudler/LocalAI) | LocalAI is a drop-in replacement REST API that's compatible with OpenAI API specifications for local inferencing.  |
 
## Python
| Links | Description |
| ------ | ------ |
| [venv](https://docs.python.org/3/library/venv.html) | The venv module supports creating lightweight “virtual environments”, each with their own independent set of Python packages installed in their site directories. |

## Performance & Latency
| Links | Description |
| ------ | ------ |
| [Hamel's Blog](https://hamel.dev/notes/llm/inference/03_inference.html) | Optimizing and testing latency for LLMs |
| [Continuous Batching](https://www.anyscale.com/blog/continuous-batching-llm-inference) | How continuous batching enables 23x throughput in LLM inference while reducing p50 latency |
| [Paper - Cornell University](https://arxiv.org/abs/2305.11186) |  Improving performance of compressed LLMs with prompt engineering |
| [Llama2 vs GPT 4 Cost comparison](https://promptengineering.org/how-does-llama-2-compare-to-gpt-and-other-ai-language-models/#:~:text=Surprisingly%2C%20we%20found%20the%20largest%20Llama%202%20model,efficient%20tokenization%2C%20Llama-2-70b%20was%2030x%20cheaper%20than%20GPT-4.) | How Does Llama-2 Compare to GPT-4/3.5 and Other AI Language Models |

## Fine Tuning and Chunking
| Links | Description |
| ------ | ------ |
| [deci.ai](https://deci.ai/blog/fine-tune-llama-2-with-lora-for-question-answering/) | How to Fine-tune Llama 2 with LoRA for Question Answering: A Guide for Practitioners |
| [databricks.com](https://www.databricks.com/blog/efficient-fine-tuning-lora-guide-llms) | Efficient Fine-Tuning with LoRA: A Guide to Optimal Parameter Selection for Large Language Models |
| [pinecone.io](https://www.pinecone.io/learn/chunking-strategies/) | Chunking Strategies for LLM Applications |
| [dev.to](https://dev.to/peterabel/what-chunk-size-and-chunk-overlap-should-you-use-4338) | What chunk size and chunk overlap should you use? |

## Others
| Links | Description |
| ------ | ------ |
| [MicroWebSrv](https://github.com/jczic/MicroWebSrv) | MicroWebSrv is a micro HTTP Web server that supports WebSockets, html/python language templating and routing handlers, for MicroPython (principally used on ESP32 and Pycom modules. Now supports all variants of Pyboard D-series from the makers of Micropython) |

# Glossary

| Term | Description
| ------- | ------ |
| Token | The basic unit of text that the model can process (characters, words, punctuation marks, etc). | 