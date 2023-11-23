# Code Llama
Code Llama is an open-source family of LLMs based on Llama 2 providing SOTA performance on code tasks. It consists of:

https://ai.meta.com/llama/get-started/#code-llama
Foundation models (Code Llama)
Python specializations (Code Llama - Python), and
Instruction-following models (Code Llama - Instruct)with 7B, 13B and 34B parameters each.

![alt text](https://scontent-lhr6-1.xx.fbcdn.net/v/t39.8562-6/394231456_1410045372879284_6990178093086367329_n.png?_nc_cat=111&ccb=1-7&_nc_sid=f537c7&_nc_ohc=0L7yNmoz5G0AX_QgGkp&_nc_ht=scontent-lhr6-1.xx&oh=00_AfDVJIUkdDylMB9G6_TqE2cXbQXCCyiLqdJ8DXvF8-yWrw&oe=6564AF6C "Code Llama")
The different stages of fine-tuning annotated with the number of tokens seen during training. Source

One of the best ways to try out and integrate with Code Llama is using Hugging Face ecosystem by following the [blog](https://huggingface.co/blog/codellama), which has:

- Demo links for Code Llama 13B, 13B-Instruct (chat), and 34B.
- Working inference code for code completion
- Working inference code for code infilling between code prefix and suffix as inputs
- Working inference code to do 4-bit loading of the 32B model so it can fit on consumer GPUs
- Guide on how to write prompts for the instruction models to have multi-turn conversations about coding
- Guide on how to use Text Generation Inference for model deployment in production
- Guide on how to integrate code autocomplete as an extension with VSCode
- Guide on how to evaluate Code Llama models

If the model does not perform well on your specific task, for example if none of the Code Llama models (7B/13B/34B) generate the correct answer for a text to SQL task, fine-tuning should be considered. This is a complete guide and notebook on how to fine-tune Code Llama using the 7B model hosted on Hugging Face. It uses the LoRA fine-tuning method and can run on a single GPU.As shown in the Code Llama References (here), fine-tuning improves the performance of Code Llama on SQL code generation, and it can be critical that LLMs are able to interoperate with structured data and SQL, the primary way to access structured data - we are developing demo apps in LangChain and RAG with Llama 2 to show this.
