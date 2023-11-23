# LlamaIndex
[LlamaIndex](https://www.llamaindex.ai/) is a data framework for LLM-based applications to ingest, structure, and access private or domain-specific data. It's available in Python (these docs) and Typescript. The GitHub repo [run-llama/llama-index](https://github.com/run-llama/llama_index) provides it own [examples](https://github.com/run-llama/llama_index/tree/main/examples). There is also a great [YouTube channel](https://www.youtube.com/@LlamaIndex) available.

For this lab I've used publically available example log files from [LogHub](https://github.com/logpai/loghub).

LlamaIndex is another popular open source framework for building LLM applications. Like LangChain, LlamaIndex can also be used to build RAG applications by easily integrating data not built-in the LLM with LLM. There are three key tools in LlamaIndex:

- **Connecting Data:** connect data of any type - structured, unstructured or semi-structured - to LLM
- **Indexing Data:** Index and store the data
- **Querying LLM:** Combine the user query and retrieved query-related data to queryLLM and return data-augmented answer

## Return data-augmented answer

LlamaIndex is mainly a data framework for connecting private or domain-specific data with LLMs, so it specializes in RAG, smart data storage and retrieval, while LangChain is a more general purpose framework which can be used to build agents connecting multiple tools. The integration of the two may provide the best performant and effective solution to building real world RAG powered Llama apps.

For an example usage of how to integrate LlamaIndex with Llama 2, see [here](https://github.com/run-llama/llama_index#-example-usage). We also published a completed [demo app](https://github.com/facebookresearch/llama-recipes/blob/main/demo_apps/LiveData.ipynb) showing how to use LlamaIndex to chat with Llama 2 about live data via the you.com API.

It’s worth noting that LlamaIndex has implemented many RAG powered LLM evaluation tools to easily measure the quality of retrieval and response, including:

- **Question Generation:** Call LLM to auto generate questions to create an evaluation dataset.
- **FaithfulnessEvaluator:** Evaluate if the generated answer is faithful to the retrieved context or if there’s hallucination.
- **CorrectnessEvaluator:** Evaluate if the generated answer matches the reference answer.
- **RelevancyEvaluator:** Evaluate if the answer and the retrieved context is relevant and consistent for the given query.

# LLamaIndex Demo

[log_ingestion.py](/llama_index/log_ingestion.py)

## Step 1: Install LlamaIndex

```Python
pip install llama-index
```

## Step 2: Run log_ingestion.py

- Update the `log_ingestion.py` script to point to the local directory of where your log files are stored.
- Update `response = query_engine.query("which IP address failed to login using root?")` with your desired question.
- Run `python log_ingestion.py`

Using [OpenSSH_2k.log_structured.csv](https://github.com/logpai/loghub/blob/master/OpenSSH/OpenSSH_2k.log_structured.csv) as an example structured CSV file, Llama 2 was able to provide the following correct response:

**Question:** which IP address failed to login using root?

**Response:** The IP address that failed to login using root is 106.5.5.195