# LlamaIndex
[LlamaIndex](https://www.llamaindex.ai/) is a data framework for LLM-based applications to ingest, structure, and access private or domain-specific data. It's available in Python (these docs) and Typescript. The GitHub repo [run-llama/llama-index](https://github.com/run-llama/llama_index) provides it own [examples](https://github.com/run-llama/llama_index/tree/main/examples). There is also a great [YouTube channel](https://www.youtube.com/@LlamaIndex) available.

For this lab I've used publically available example log files from [LogHub](https://github.com/logpai/loghub).

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